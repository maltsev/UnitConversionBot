# -*- coding: utf-8 -*-
import unittest
from modules.parser import parseMessageText, parseExpression, normalizeExpression, InvalidExpressionException
import units


class ParserTests(unittest.TestCase):
    maxDiff = None

    def test_parseMessageText(self):
        cases = [
            ('1 ft to m', '1 ft to m', ''),
            ("'1 ft to m'", '1 ft to m', ''),
            ('/start', '', 'start'),
            ('/start start', 'start', 'start'),
            ('/convert@UnitConversionBot 1 day to hours.', '1 day to hours', 'convert'),
            ('@UnitConversionBot 1 in to meter', '1 in to meter', ''),
            ('@UnitConversionBot 1 m/s to km/h', '1 m/s to km/h', ''),
            ('/ foob', '/ foob', ''),
            (u'/convert "1 фут в метры"', u'1 фут в метры', 'convert'),
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
            # Length
            ('1 ft to m', 1, 'FOOT', 'METER'),
            ('10 meters to kilometer', 10, 'METER', 'KILOMETER'),
            ('1.5 km in hour', 1.5, 'KILOMETER', 'HOUR'),
            ('100,000m to ft', 100000, 'METER', 'FOOT'),
            ('93ft', 93, 'FOOT', 'METER'),
            ('38 meters to', 38, 'METER', 'FOOT'),

            # Area
            (u'10 ft² to m²', 10, 'FOOT_SQUARE', 'METER_SQUARE'),
            ('100 km2 to m^2', 100, 'KILOMETER_SQUARE', 'METER_SQUARE'),
            ('1 sq cm to square m', 1, 'CENTIMETER_SQUARE', 'METER_SQUARE'),
            ('1sq centimeters', 1, 'CENTIMETER_SQUARE', 'METER_SQUARE'),

            # Volume
            (u'10 fl. oz. to dm³', 10, 'IMPERIAL_FLUID_OUNCE', 'DECIMETER_CUBIC'),
            (u'10 fl oz to dm³', 10, 'IMPERIAL_FLUID_OUNCE', 'DECIMETER_CUBIC'),
            (u'10 fl.oz to dm³', 10, 'IMPERIAL_FLUID_OUNCE', 'DECIMETER_CUBIC'),
            ('12 in^3=m3', 12, 'INCH_CUBIC', 'METER_CUBIC'),
            ('10 cubic m to cu dm', 10, 'METER_CUBIC', 'DECIMETER_CUBIC'),
            ('1 meter^3', 1, 'METER_CUBIC', 'CENTIMETER_CUBIC'),

            # Currencies
            (u'100 $ to ₽', 100, 'USD', 'RUB'),
            ('100 fr to yen', 100, 'CHF', 'JPY'),
            (u'100.50 Nicaraguan Córdoba to rubles', 100.5, 'NIO', 'RUB'),
            ('12 nuevo sol to won', 12, 'PEN', 'KRW'),
            ('1 eur', 1, 'EUR', 'USD'),
            ('1 CZK', 1, 'CZK', 'EUR'),
            ('$1 to CZK', 1, 'USD', 'CZK'),
            (u'£ 100', 100, 'GBP', 'USD'),

            # Mass
            ('0.45 KG to G', 0.45, 'KILOGRAM', 'GRAM'),
            ('1 pound', 1, 'POUND', 'GRAM'),

            # Speed
            ('12 km/hr to ft/s', 12, 'KILOMETER_PER_HOUR', 'FOOT_PER_SECOND'),
            ('1 m/s to km/h to mph', 1, 'METER_PER_SECOND', 'MILE_PER_HOUR'),
            ('12 m/s', 12, 'METER_PER_SECOND', 'KILOMETER_PER_HOUR'),

            # Time
            ('100 d to yr', 100, 'DAY', 'YEAR'),
            ('1230s go', 1230, 'SECOND', 'MILLISECOND'),
            ('100 yr =', 100, 'YEAR', 'DAY'),

            # Temperature
            (u'100.5 °C to F', 100.5, 'CELSIUS', 'FAHRENHEIT'),
            ('34 K = C', 34, 'KELVIN', 'CELSIUS'),
            ('100 C', 100, 'CELSIUS', 'FAHRENHEIT'),
            ('23 K', 23, 'KELVIN', 'CELSIUS'),

            # Density
            (u'100 g/cm³ to kg/m³', 100, 'GRAM_PER_CENTIMETER_CUBIC', 'KILOGRAM_PER_METER_CUBIC'),
            ('19 gram per cubic cm to kilograms per cu metre', 19, 'GRAM_PER_CENTIMETER_CUBIC', 'KILOGRAM_PER_METER_CUBIC'),
            ('10 kg per m to grams per centimeters', 10, 'KILOGRAM_PER_METER_CUBIC', 'GRAM_PER_CENTIMETER_CUBIC'),
            ('1 g/cm to kg/m3', 1, 'GRAM_PER_CENTIMETER_CUBIC', 'KILOGRAM_PER_METER_CUBIC'),
            ('1 kg/m to g/ml', 1, 'KILOGRAM_PER_METER_CUBIC', 'GRAM_PER_MILLILITER'),
            ('1 g/cm', 1, 'GRAM_PER_CENTIMETER_CUBIC', 'KILOGRAM_PER_METER_CUBIC')
        ]

        invalidExpressionError = "Sorry, I don't understand your question. I'm just a bot :-( Please ask something simple like '100 ft to m'."
        invalidValueErrorTemplate = u"Sorry, I don't understand the number '{}'. Please type it in a more ordinary way, like 100 or 12.5"
        invalidUnitErrorTemplate = u"Sorry, I'm just a stupid bot :-( I don't know what does '{}' mean. But my master probably does. I'd ask him to teach me."

        invalidTestCases = [
            (u'1 фут в метры', invalidUnitErrorTemplate.format(u'фут')),
            (u'1/4 inch to cm', invalidValueErrorTemplate.format('1/4'))
        ]

        unitsIndex = units.getIndex()
        for expression, value, fromUnitName, toUnitName in cases:
            self.assertEqual(parseExpression(expression, unitsIndex), {
                'fromValueUnit': {
                    'value': value,
                    'unit': unitsIndex[fromUnitName]
                },
                'toUnit': unitsIndex[toUnitName]
            })

        for expression, errorMessage in invalidTestCases:
            with self.assertRaises(InvalidExpressionException) as cm:
                parseExpression(expression, unitsIndex)
            self.assertEqual(unicode(cm.exception), errorMessage)




    def test_normalizeExpression(self):
        cases = [
            ('Convert 100,000M to cubic foot', u'100000 m to ft³'),
            (u'100.1fl oz = m²', u'100.1 fl.oz = m²'),
            (u'1/4€ in ₽', u'1/4 € in ₽')
        ]

        unitsIndex = units.getIndex()
        for expression, expectedNormalizedExpression in cases:
            self.assertEqual(normalizeExpression(expression, unitsIndex), expectedNormalizedExpression)
