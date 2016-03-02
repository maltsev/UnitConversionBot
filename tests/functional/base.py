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
    def checkLogs(self, logs, *expectedLogs):
        if os.environ['RUN_ON_INSTANCE']:
            return

        expectedLogs = [('root', type, message) for type, message in expectedLogs]
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




def responseTemplate(responseJson):
    template = {
        'method': 'sendMessage',
        'disable_notification': True
    }

    template.update(responseJson)
    return template


def requestTemplate(messageJson):
    return {
        'update_id': random.randint(1, sys.maxint),
        'message': messageJson
    }
