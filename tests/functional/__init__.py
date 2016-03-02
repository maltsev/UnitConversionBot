# -*- coding: utf-8 -*-
import unittest

from webhook_test import WebHookTests
from startCommand_test import StartCommandTests
from convertCommand_test import ConvertCommandTests
from helpCommand_test import HelpCommandTests

tests = [
    unittest.TestLoader().loadTestsFromTestCase(WebHookTests),
    unittest.TestLoader().loadTestsFromTestCase(StartCommandTests),
    unittest.TestLoader().loadTestsFromTestCase(ConvertCommandTests),
    unittest.TestLoader().loadTestsFromTestCase(HelpCommandTests)
]
