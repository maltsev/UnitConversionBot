# -*- coding: utf-8 -*-
import sys
import json
import logging
import unittest
import hashlib
import random
from testfixtures import log_capture
from base import FunctionalTestCase
from convertCommand_test import ConverMixin


class InlineTests(ConverMixin, FunctionalTestCase):
    @log_capture(level=logging.INFO)
    def test_inlineConvert(self, logs):
        requestJson = requestTemplate({
            'id': '1235',
            'query': u'1000 m² to dm2'
        })

        expectedResponseJson = responseTemplate('1235', {
            'title': u'100,000 dm²',
            'message_text': u'1,000 m² = 100,000 dm²'
        })

        self.assertRequest(requestJson, expectedResponseJson)
        self.checkLogs(logs, ('INFO', { 'command': 'convert', 'type': 'success', 'expression': u'1000 m² to dm2', 'response': u'100,000 dm²', 'fullResponse': u'1,000 m² = 100,000 dm²'}))




    def test_inlineEmpty(self):
        requestJson = requestTemplate({
            'id': '4534',
            'query': ' '
        })

        expectedResponseJson = responseTemplate('4534', {
            'title': '10 ft to m',
            'description': 'Please type a convert expression (e.g., "10 ft to m").',
            'message_text': '10 ft = 3.048 m'
        })

        self.assertRequest(requestJson, expectedResponseJson)




    @log_capture(level=logging.INFO)
    def test_inlineConvertWithoutToUnit(self, logs):
        requestJson = requestTemplate({
            'id': '1235',
            'query': '1 light year'
        })

        expectedResponseJson = responseTemplate('1235', {
            'title': '9,460,730,472,580.801 km',
            'message_text': '1 ly = 9,460,730,472,580.801 km'
        })

        self.assertRequest(requestJson, expectedResponseJson)
        self.checkLogs(logs, ('INFO', { 'command': 'convert', 'type': 'success', 'expression': u'1 light year', 'response': u'9,460,730,472,580.801 km', 'fullResponse': u'1 ly = 9,460,730,472,580.801 km'}))




    def test_invalidInlineConvert(self):
        requestJson = requestTemplate({
            'id': '11',
            'query': '10 blah'
        })

        expectedResponseJson = responseTemplate('11', {
            'title': 'Error',
            'message_text': '@UnitConversionBot',
            'description': "Sorry, I'm just a stupid bot :-( I don't know what does 'blah' mean. But my master probably does. I'd ask him to teach me."
        })

        self.assertRequest(requestJson, expectedResponseJson)




def requestTemplate(inlineQuery):
    return {
        'update_id': random.randint(1, sys.maxint),
        'inline_query': inlineQuery
    }




def responseTemplate(inlineQueryId, result):
    result['type'] = 'article'
    result['id'] = hashlib.md5(result['title'].encode('utf-8')).hexdigest()

    return {
        'method': 'answerInlineQuery',
        'inline_query_id': inlineQueryId,
        'cache_time': 60*60*12,
        'is_personal': False,
        'results': json.dumps([result], sort_keys=True)
    }
