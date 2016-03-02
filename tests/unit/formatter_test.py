# -*- coding: utf-8 -*-
import unittest
from modules.formatter import formatValueUnit, getSender
import units


class FormatterTests(unittest.TestCase):
    def test_formatValueUnit(self):
        cases = [
            (5.23, 'EUR', u'5.23 €'),
            (1, 'FOOT', '1 ft'),
            (3.140, 'METER', '3.14 m'),
            (1.5, 'FOOT_SQUARE', u'1.5 ft²'),
            (1.0/3, 'KILOGRAM', '0.333 kg'),
            (0, 'HOUR', '0 h'),
            (-100, 'DAY', '-100 d'),
            (12, 'IMPERIAL_FLUID_OUNCE', '12 fl.oz'),
            (1.2, 'KILOMETER_PER_HOUR', '1.2 km/h')
        ]

        for value, unitName, formattedValueUnit in cases:
            self.assertEquals(formatValueUnit({
                'value': value,
                'unit': units.index[unitName]
            }), formattedValueUnit)


    def test_getSender(self):
        cases = [
            (None, ('Anonymouse', 'anonymouse')),
            ({'name': '', 'username': '', 'id': 0}, ('Anonymouse', 'anonymouse')),
            ({'name': 'Kirill', 'username': 'Kirill', 'id': 0}, ('Kirill', 'kirill')),
            ({'name': 'Kirill', 'username': 'Kirill', 'id': 36}, ('Kirill', 'kirill36')),
            ({'name': 'Kirill', 'username': '', 'id': 120}, ('Kirill', 'john120'))
        ]

        for user, expected in cases:
            self.assertEqual(getSender(user), expected)
