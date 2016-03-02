# -*- coding: utf-8 -*-
import os
import unittest
import base64
from google.appengine.ext import testbed
from base import FunctionalTestCase, requestTemplate, responseTemplate


class FeedbackCommandTests(FunctionalTestCase):
    def setUp(self):
        self.testbed = testbed.Testbed()
        self.testbed.activate()
        self.testbed.init_mail_stub()
        self.mailStub = self.testbed.get_stub(testbed.MAIL_SERVICE_NAME)




    def tearDown(self):
        self.testbed.deactivate()




    def test_emptyFeedback(self):
        requestJson = requestTemplate({
            'text': '/feedback',
            'chat': {
                'id': 123
            }
        })

        expectedResponseJson = responseTemplate({
            'chat_id': 123,
            'text': 'Please write some feedback.'
        })

        self.assertRequest(requestJson, expectedResponseJson)




    def test_feedback(self):
        requestJson = requestTemplate({
            'text': u'/feedback Крутое приложение²!',
            'from': {
                'id': 939,
                'first_name': 'Kevin²',
                'last_name': 'Smith',
                'username': 'ksmth'
            },
            'chat': {
                'id': 23
            }
        })

        requestJson['update_id'] = 92838

        expectedResponseJson = responseTemplate({
            'chat_id': 23,
            'text': 'The feedback was sent. Thank you!'
        })

        self.assertRequest(requestJson, expectedResponseJson)
        if os.environ['RUN_ON_INSTANCE']:
            return

        messages = self.mailStub.get_sent_messages(to='dakki1@gmail.com')
        self.assertEqual(1, len(messages))
        message = messages[0]
        self.assertEqual('dakki1@gmail.com', message.to)
        self.assertEqual('Kevin Smith <ksmth939@unitconversionbot.appspotmail.com>', message.sender)
        self.assertEqual('Feedback #92838', message.subject)

        encodedMessage = base64.b64encode('Крутое приложение²')
        self.assertTrue(encodedMessage in str(message.body))
