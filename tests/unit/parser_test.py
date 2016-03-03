# -*- coding: utf-8 -*-
import unittest
from modules.parser import parseMessageText, parseExpression, InvalidExpressionException
import units
from units import length, mass, time


class ParserTests(unittest.TestCase):
    def test_parseMessageText(self):
        cases = [
            ('1 ft to m', '1 ft to m', ''),
            ('/start', '', 'start'),
            ('/start start', 'start', 'start'),
            ('/convert@UnitConversionBot 1 day to hours', '1 day to hours', 'convert'),
            ('@UnitConversionBot 1 in to meter', '1 in to meter', ''),
            ('@UnitConversionBot 1 m/s to km/h', '1 m/s to km/h', ''),
            ('/ foob', '/ foob', ''),
            (u'/convert 1 фут в метры', u'1 фут в метры', 'convert'),
            (u'10 ft² to m²', u'10 ft² to m²', ''),
            ('', '', '')
        ]

        for messageText, expression, command in cases:
            self.assertEqual(parseMessageText(messageText), {
                'expression': expression,
                'command': command
            })


    def test_parseExpression(self):
        cases = [
            ('1 ft to m', 1, 'FOOT', 'METER'),
            ('10 meters to kilometer', 10, 'METER', 'KILOMETER'),
            ('1.5 km to hour', 1.5, 'KILOMETER', 'HOUR'),
            ('0,45 KG to G', 0.45, 'KILOGRAM', 'GRAM'),
            (u'10 ft² to m²', 10, 'FOOT_SQUARE', 'METER_SQUARE'),
            (u'100 $ to ₽', 100, 'USD', 'RUB'),
            (u'10 fl.oz to dm³', 10, 'IMPERIAL_FLUID_OUNCE', 'DECIMETER_CUBIC'),
            ('12 km/h to ft/s', 12, 'KILOMETER_PER_HOUR', 'FOOT_PER_SECOND'),
            ('1 m/s to km/h', 1, 'METER_PER_SECOND', 'KILOMETER_PER_HOUR')
        ]

        invalidExpressionError = "Sorry, I don't understand your question. I'm just a bot :-( Please ask something simple like '100 ft to m'."
        invalidUnitErrorTemplate = u"Sorry, I'm just a stupid bot :-( I don't know what does {} mean. But my master probably does. I'd ask him to teach me."

        invalidTestCases = [
            ('10m to ft', invalidUnitErrorTemplate.format("'10m'")),
            ('10m=ft', invalidExpressionError),
            (u'1 фут в метры', invalidExpressionError)
        ]

        for expression, value, fromUnitName, toUnitName in cases:
            self.assertEqual(parseExpression(expression), {
                'fromValueUnit': {
                    'value': value,
                    'unit': units.index[fromUnitName]
                },
                'toUnit': units.index[toUnitName]
            })

        for expression, errorMessage in invalidTestCases:
            with self.assertRaises(InvalidExpressionException) as cm:
                parseExpression(expression)
            self.assertEqual(str(cm.exception), errorMessage)
