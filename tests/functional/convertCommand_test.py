# -*- coding: utf-8 -*-
import os
import json
import datetime
import logging
import unittest
from testfixtures import log_capture
from google.appengine.ext import ndb
from google.appengine.ext import testbed
from base import FunctionalTestCase, requestTemplate, responseTemplate
from model import Rates

file = open('./tests/exchangeRates.json')
testExchangeRates = json.loads(file.read())
file.close()


class ConverMixin(object):
    def setUp(self):
        if os.environ.get('RUN_ON_INSTANCE'):
            return

        self.testbed = testbed.Testbed()
        self.testbed.activate()
        self.testbed.init_datastore_v3_stub()
        self.testbed.init_memcache_stub()

        ndb.get_context().clear_cache()
        Rates(content=testExchangeRates).put()




    def tearDown(self):
        if not os.environ.get('RUN_ON_INSTANCE'):
            self.testbed.deactivate()




class ConvertCommandTests(ConverMixin, FunctionalTestCase):
    @log_capture(level=logging.INFO)
    def test_convertWithoutCommand(self, logs):
        requestJson = requestTemplate({
            'text': '1.2 LB TO Gram',
            'chat': {
                'id': 928
            }
        })

        expectedResponseJson = responseTemplate({
            'chat_id': 928,
            'text': '544.311 g'
        })

        self.assertRequest(requestJson, expectedResponseJson)
        self.checkLogs(logs, ('INFO', {'command': 'convert', 'type': 'success', 'expression': u'1.2 LB TO Gram', 'response': u'544.311 g'}))




    def test_convertWithoutCommandAndWithBotName(self):
        requestJson = requestTemplate({
            'text': '@UnitConversionBot 1 m/s to km/h',
            'chat': {
                'id': 900
            }
        })

        expectedResponseJson = responseTemplate({
            'chat_id': 900,
            'text': '3.6 km/h'
        })

        self.assertRequest(requestJson, expectedResponseJson)




    def test_convertCurrencies(self):
        responseMessage = '2.014 CZK'
        if not os.environ['RUN_ON_INSTANCE']:
            # Add recent exchange rates
            anotherTestExchangeRates = testExchangeRates.copy()
            anotherTestExchangeRates['rates']['CZK'] = 1000000.0
            futureDate = datetime.datetime.now() + datetime.timedelta(days=1)
            Rates(content=anotherTestExchangeRates, date=futureDate).put()
            responseMessage = '82,693.184 CZK'

        requestJson = requestTemplate({
            'text': u'10.5 Icelandic Króna to Kč',
            'chat': {
                'id': 901
            }
        })

        expectedResponseJson = responseTemplate({
            'chat_id': 901,
            'text': responseMessage
        })

        self.assertRequest(requestJson, expectedResponseJson)




    @log_capture(level=logging.INFO)
    def test_convert(self, logs):
        requestJson = requestTemplate({
            'text': u'/convert 1 ft² to m²',
            'chat': {
                'id': 536
            }
        })

        expectedResponseJson = responseTemplate({
            'chat_id': 536,
            'text': u'0.093 m²'
        })

        self.assertRequest(requestJson, expectedResponseJson)
        self.checkLogs(logs, ('INFO', {'command': 'convert', 'type': 'success', 'expression': u'1 ft² to m²', 'response': u'0.093 m²'}))




    def test_emptyConvertExpression(self):
        requestJson = requestTemplate({
            'text': '/convert ',
            'chat': {
                'id': 96
            }
        })

        expectedResponseJson = responseTemplate({
            'chat_id': 96,
            'text': 'Please type something like "/convert 100 ft to m"'
        })

        self.assertRequest(requestJson, expectedResponseJson)




    def test_convertWithBotName(self):
        requestJson = requestTemplate({
            'text': '/convert@UnitConversionBot 1 day to hours',
            'chat': {
                'id': 11
            }
        })

        expectedResponseJson = responseTemplate({
            'chat_id': 11,
            'text': '24 h'
        })

        self.assertRequest(requestJson, expectedResponseJson)




    def test_convertMultilineExpression(self):
        requestJson = requestTemplate({
            'text': '1000 m/s to km/h\n10 fl.oz to litres',
            'chat': {
                'id': 19
            }
        })

        expectedResponseJson = responseTemplate({
            'chat_id': 19,
            'text': '3,600 km/h'
        })

        self.assertRequest(requestJson, expectedResponseJson)




    @log_capture(level=logging.INFO)
    def test_invalidExpression(self, logs):
        requestJson = requestTemplate({
            'text': u'1 фут в метры',
            'chat': {
                'id': 113
            }
        })

        expectedResponseJson = responseTemplate({
            'chat_id': 113,
            'text': u"Sorry, I'm just a stupid bot :-( I don't know what does 'фут' mean. But my master probably does. I'd ask him to teach me."
        })

        self.assertRequest(requestJson, expectedResponseJson)
        self.checkLogs(logs, ('INFO', {'command': 'convert', 'type': 'InvalidUnitException', 'expression': u'1 фут в метры'}))




    @log_capture(level=logging.INFO)
    def test_convertIncompatibleUnitCategories(self, logs):
        requestJson = requestTemplate({
            'text': '1 ft to g',
            'chat': {
                'id': 110
            }
        })

        expectedResponseJson = responseTemplate({
            'chat_id': 110,
            'text': "Sorry, I can't convert foot to gram (at least in this universe)."
        })

        self.assertRequest(requestJson, expectedResponseJson)
        self.checkLogs(logs, ('INFO', {'command': 'convert', 'type': 'IncompatibleCategoriesException', 'expression': u'1 ft to g'}))




    @log_capture(level=logging.INFO)
    def test_convertNotExistsFromUnit(self, logs):
        requestJson = requestTemplate({
            'text': '1 blablagram² to gram',
            'chat': {
                'id': 11
            }
        })

        expectedResponseJson = responseTemplate({
            'chat_id': 11,
            'text': u"Sorry, I'm just a stupid bot :-( I don't know what does 'blablagram²' mean. But my master probably does. I'd ask him to teach me."
        })

        self.assertRequest(requestJson, expectedResponseJson)
        self.checkLogs(logs, ('INFO', {'command': 'convert', 'type': 'InvalidUnitException', 'expression': u'1 blablagram² to gram'}))




    def test_convertNotExistsUnits(self):
        requestJson = requestTemplate({
            'text': '1.2 blablagram to wtfgram',
            'chat': {
                'id': 9
            }
        })

        expectedResponseJson = responseTemplate({
            'chat_id': 9,
            'text': "Sorry, I'm just a stupid bot :-( I don't know what does 'blablagram' mean. But my master probably does. I'd ask him to teach me."
        })

        self.assertRequest(requestJson, expectedResponseJson)



    @log_capture(level=logging.INFO)
    def test_convertInvalidUnitValue(self, logs):
        requestJson = requestTemplate({
            'text': 'one ft to m',
            'chat': {
                'id': 8
            }
        })

        expectedResponseJson = responseTemplate({
            'chat_id': 8,
            'text': u"Sorry, I don't understand the number 'one'. Please type it in a more ordinary way, like 100 or 12.5"
        })

        self.assertRequest(requestJson, expectedResponseJson)
        self.checkLogs(logs, ('INFO', {'command': 'convert', 'type': 'InvalidValueException', 'expression': u'one ft to m'}))
