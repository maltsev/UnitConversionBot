# -*- coding: utf-8 -*-
import unittest

from webhook_test import WebHookTests
from inline_test import InlineTests
from startCommand_test import StartCommandTests
from convertCommand_test import ConvertCommandTests
from helpCommand_test import HelpCommandTests
from updateRates_test import UpdateRatesTests

tests = [
    unittest.TestLoader().loadTestsFromTestCase(WebHookTests),
    unittest.TestLoader().loadTestsFromTestCase(InlineTests),
    unittest.TestLoader().loadTestsFromTestCase(StartCommandTests),
    unittest.TestLoader().loadTestsFromTestCase(ConvertCommandTests),
    unittest.TestLoader().loadTestsFromTestCase(HelpCommandTests),
    unittest.TestLoader().loadTestsFromTestCase(UpdateRatesTests),
]
