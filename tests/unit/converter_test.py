# -*- coding: utf-8 -*-
import unittest
from modules.converter import convertUnit
import units


class ConverterTests(unittest.TestCase):
    def test_convertUnit(self):
        self.maxDiff = None

        cases = [
            # Length
            ((1,  'FOOT'),          (0.3048, 'METER')),
            ((13, 'NAUTICAL_MILE'), (24.076, 'KILOMETER')),

            # Area
            ((50.5, 'FOOT_SQUARE'),       (4.6916, 'METER_SQUARE')),
            ((100,  'KILOMETER_SQUARE'),  (38.6102, 'MILE_SQUARE')),

            # Volume
            ((1.2,  'METER_CUBIC'),     (1200, 'LITER')),
            ((1234, 'MILLILITER'),      (1.234, 'LITER')),
            ((12,   'IMPERIAL_GALLON'), (54.5531, 'LITER')),

            # Speed
            ((1,   'METER_PER_SECOND'), (3.6, 'KILOMETER_PER_HOUR')),
            ((100, 'MILE_PER_HOUR'),    (86.8976, 'KNOT')),

            # Temperature
            #((0, 'CELSIUS'), (273.15, 'KELVIN')),

            # Mass
            ((1.2, 'POUND'), (544.3108, 'GRAM')),
            ((500, 'OUNCE'), (31.25, 'POUND')),

            # Time
            ((1,   'YEAR'), (365.2425, 'DAY')),

            # Currencies
            ((2.1, 'USD'), (2, 'USD')),
            ((10,  'USD'), (9, 'EUR')),
            ((10,  'GBP'), (14, 'USD'))
        ]

        # Invalid case
        with self.assertRaises(Exception) as cm:
            convertUnit(
                {'value': 1.0, 'unit': units.index['FOOT']},
                units.index['GRAM']
            )
        self.assertEqual(str(cm.exception), "Sorry, I can't convert foot to gram (at least in this universe).")


        # Valid cases
        for fromUnit, toUnit in cases:
            fromValueUnit = {
                'value': float(fromUnit[0]),
                'unit': units.index[fromUnit[1]]
            }

            toValueUnit = {
                'value': float(toUnit[0]),
                'unit': units.index[toUnit[1]]
            }

            result = convertUnit(fromValueUnit, toValueUnit['unit'])
            precision = 0 if fromValueUnit['unit']['category'] == 'currencies' else 4
            result['value'] = round(result['value'], precision)

            self.assertEqual(
                result,
                toValueUnit
            )
