# -*- coding: utf-8 -*-
import logging
import unittest
from testfixtures import log_capture
from base import FunctionalTestCase, requestTemplate, responseTemplate


class ConvertCommandTests(FunctionalTestCase):
    @log_capture(level=logging.INFO)
    def test_convertWithoutCommand(self, logs):
        requestJson = requestTemplate({
            'text': '1,2 LB TO Gram',
            'chat': {
                'id': 928
            }
        })

        expectedResponseJson = responseTemplate({
            'chat_id': 928,
            'text': '544.311 g'
        })

        self.assertRequest(requestJson, expectedResponseJson)
        self.checkLogs(logs, ('INFO', "{'type': 'success', 'command': 'convert', 'expression': u'1,2 LB TO Gram', 'response': u'544.311 g'}"))




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
        self.checkLogs(logs, ('INFO', "{'type': 'success', 'command': 'convert', 'expression': u'1 ft\\xb2 to m\\xb2', 'response': u'0.093 m\\xb2'}"))




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
            'text': '100 m/s to km/h\n10 fl.oz to litres',
            'chat': {
                'id': 19
            }
        })

        expectedResponseJson = responseTemplate({
            'chat_id': 19,
            'text': '360 km/h'
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
            'text': "Sorry, I don't understand your question. I'm just a bot :-( Please ask something simple like '100 ft to m'."
        })

        self.assertRequest(requestJson, expectedResponseJson)
        self.checkLogs(logs, ('INFO', "{'type': 'invalidExpressionError', 'command': 'convert', 'expression': u'1 \\u0444\\u0443\\u0442 \\u0432 \\u043c\\u0435\\u0442\\u0440\\u044b'}"))




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
        self.checkLogs(logs, ('INFO', "{'type': 'incompatibleCategoriesError', 'command': 'convert', 'expression': u'1 ft to g'}"))




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
            'text': u"Sorry, I'm just a stupid bot :-( I don't know what does '1 blablagram²' mean. But my master probably does. I'd ask him to teach me."
        })

        self.assertRequest(requestJson, expectedResponseJson)
        self.checkLogs(logs, ('INFO', "{'type': 'invalidUnitError', 'command': 'convert', 'expression': u'1 blablagram\\xb2 to gram'}"))




    def test_convertNotExistsUnits(self):
        requestJson = requestTemplate({
            'text': '1.2 blablagram to wtfgram',
            'chat': {
                'id': 9
            }
        })

        expectedResponseJson = responseTemplate({
            'chat_id': 9,
            'text': "Sorry, I'm just a stupid bot :-( I don't know what does '1.2 blablagram' and 'wtfgram' mean. But my master probably does. I'd ask him to teach me."
        })

        self.assertRequest(requestJson, expectedResponseJson)




    def test_convertInvalidUnitValue(self):
        requestJson = requestTemplate({
            'text': 'one ft to m',
            'chat': {
                'id': 8
            }
        })

        expectedResponseJson = responseTemplate({
            'chat_id': 8,
            'text': "Sorry, I'm just a stupid bot :-( I don't know what does 'one ft' mean. But my master probably does. I'd ask him to teach me."
        })

        self.assertRequest(requestJson, expectedResponseJson)
