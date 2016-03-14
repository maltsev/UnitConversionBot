# -*- coding: utf-8 -*-
import sys
import os
import random
import json
import requests
import unittest
from webtest import TestApp
from app import app

class FunctionalTestCase(unittest.TestCase):
    maxDiff = None

    def checkLogs(self, logs, *expectedLogs):
        if os.environ['RUN_ON_INSTANCE']:
            return

        expectedLogs = [('root', type, unicode(message)) for type, message in expectedLogs]
        logs.check(*expectedLogs)




    def makeRequest(self, requestJson):
        responseData = {}
        if os.environ['RUN_ON_INSTANCE']:
            responseData['response'] = response = requests.post('http://localhost:8080/api/webhook', json.dumps(requestJson))
            responseData['contentType'] = response.headers['content-type']
            responseData['json'] = response.json()
        else:
            responseData['response'] = response = TestApp(app).post_json('/api/webhook', requestJson)
            responseData['contentType'] = response.content_type
            responseData['json'] = response.json

        return responseData




    def assertRequest(self, requestJson, expectedResponseJson):
        responseData = self.makeRequest(requestJson)
        self.assertEqual(responseData['response'].status_code, 200)
        self.assertEqual(responseData['contentType'], 'application/json')
        self.assertEqual(responseData['json'], expectedResponseJson)
        if 'text' in responseData['json']:
            responseTextLength = len(responseData['json']['text'])
            self.assertTrue(responseTextLength < 4096, 'Response text contains {} chars'.format(responseTextLength))




def responseTemplate(response):
    template = {
        'method': 'sendMessage',
        'disable_notification': True
    }

    template.update(response)
    return template


def requestTemplate(message):
    return {
        'update_id': random.randint(1, sys.maxint),
        'message': message
    }
