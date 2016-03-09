# -*- coding: utf-8 -*-
import unittest
from modules.parser import parseMessageText, parseExpression, normalizeExpression, InvalidExpressionException
import units


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
            (u'10 ft² to m²\n 100 km\h to m\s', u'10 ft² to m²', ''),
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
            ('1.5 km in hour', 1.5, 'KILOMETER', 'HOUR'),
            ('0.45 KG to G', 0.45, 'KILOGRAM', 'GRAM'),
            (u'10 ft² to m²', 10, 'FOOT_SQUARE', 'METER_SQUARE'),
            ('100 km^2 to m^2', 100, 'KILOMETER_SQUARE', 'METER_SQUARE'),
            (u'100 $ to ₽', 100, 'USD', 'RUB'),
            ('100 fr to yen', 100, 'CHF', 'JPY'),
            (u'10 fl. oz. to dm³', 10, 'IMPERIAL_FLUID_OUNCE', 'DECIMETER_CUBIC'),
            (u'10 fl oz to dm³', 10, 'IMPERIAL_FLUID_OUNCE', 'DECIMETER_CUBIC'),
            (u'10 fl.oz to dm³', 10, 'IMPERIAL_FLUID_OUNCE', 'DECIMETER_CUBIC'),
            ('12 in^3=m^3', 12, 'INCH_CUBIC', 'METER_CUBIC'),
            ('12 km/hr to ft/s', 12, 'KILOMETER_PER_HOUR', 'FOOT_PER_SECOND'),
            ('1 m/s to km/h to mph', 1, 'METER_PER_SECOND', 'MILE_PER_HOUR'),
            ('100,000m to ft', 100000, 'METER', 'FOOT'),
        ]

        invalidExpressionError = "Sorry, I don't understand your question. I'm just a bot :-( Please ask something simple like '100 ft to m'."
        invalidValueErrorTemplate = u"Sorry, I don't understand the number '{}'. Please type it in a more ordinary way, like 100 or 12.5"
        invalidUnitErrorTemplate = u"Sorry, I'm just a stupid bot :-( I don't know what does '{}' mean. But my master probably does. I'd ask him to teach me."

        invalidTestCases = [
            (u'1 фут в метры', invalidUnitErrorTemplate.format(u'фут')),
            (u'1/4 inch to cm', invalidValueErrorTemplate.format('1/4'))
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
            self.assertEqual(unicode(cm.exception), errorMessage)




    def test_normalizeExpression(self):
        cases = [
            ('Convert 100,000M to cubic foot', u'100000 m to ft³'),
            (u'100.1fl oz = m²', u'100.1 fl.oz = m²'),
            (u'1/4€ in ₽', u'1/4 € in ₽')
        ]

        for expression, expectedNormalizedExpression in cases:
            self.assertEqual(normalizeExpression(expression), expectedNormalizedExpression)
