# -*- coding: utf-8 -*-
import logging
import unittest
from testfixtures import log_capture
from webtest import TestApp
from app import app
from base import FunctionalTestCase, requestTemplate, responseTemplate


class WebHookTests(FunctionalTestCase):
    def test_commandNotFound(self):
        requestJson = requestTemplate({
            'text': '/someCommand 1 m² to ft',
            'chat': {
                'id': 469
            }
        })

        expectedResponseJson = responseTemplate({
            'chat_id': 469,
            'text': "Sorry, I don't understand your command."
        })

        self.assertRequest(requestJson, expectedResponseJson)




    def test_noMessageText(self):
        requestJson = requestTemplate({
            'chat': {
                'id': 860
            }
        })

        self.assertRequest(requestJson, {})




    @log_capture(level=logging.WARNING)
    def test_noChatId(self, logs):
        requestJson = requestTemplate({
            'text': '/someCommand 1 m² to ft',
        })

        self.assertRequest(requestJson, {'error': 'Chat ID is empty'})
        self.checkLogs(logs, ('WARNING', 'Chat ID is empty'))



    @log_capture(level=logging.WARNING)
    def test_requestWithInvalidJson(self, logs):
        response = TestApp(app).post('/api/webhook', '{')

        self.assertEqual(response.status, '200 OK')
        self.assertEqual(response.content_type, 'application/json')
        self.assertEqual(response.json, {})
        logs.check(('root', 'WARNING', 'Expecting object: line 1 column 1 (char 0)'))
