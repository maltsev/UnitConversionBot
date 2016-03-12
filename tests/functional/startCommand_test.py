# -*- coding: utf-8 -*-
import unittest
from base import FunctionalTestCase, requestTemplate, responseTemplate

startMessage = """
Hi!

My name is @UnitConversionBot. I can convert from one unit to another. Just type something like "100 ft to m" (in private chat with me) or "/convert 1 km2 to m2" (in group chats). For more info type /help

If you have an issue or just want to say thanks, feel free to contact my master @kirillmaltsev
Thank you for chatting with me :-)
""".strip()


class StartCommandTests(FunctionalTestCase):
    def test_start(self):
        requestJson = requestTemplate({
            'text': '/start',
            'chat': {
                'id': 861
            }
        })

        expectedResponseJson = responseTemplate({
            'chat_id': 861,
            'text': startMessage
        })

        self.assertRequest(requestJson, expectedResponseJson)
