# -*- coding: utf-8 -*-
import unittest
from converter_test import ConverterTests
from parser_test import ParserTests
from formatter_test import FormatterTests

tests = [
    unittest.TestLoader().loadTestsFromTestCase(ParserTests),
    unittest.TestLoader().loadTestsFromTestCase(ConverterTests),
    unittest.TestLoader().loadTestsFromTestCase(FormatterTests)
]
