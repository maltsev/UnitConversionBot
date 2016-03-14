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

            # Currencies
            ((2,     'USD'), (2,       'USD')),
            ((10.2,  'USD'), (21.42,   'EUR')),
            ((10.3,  'GBP'), (3.1212,  'USD')),

            # Mass
            ((1.2, 'POUND'), (544.3108, 'GRAM')),
            ((500, 'OUNCE'), (31.25, 'POUND')),

            # Speed
            ((1,   'METER_PER_SECOND'),     (3.6, 'KILOMETER_PER_HOUR')),
            ((100, 'MILE_PER_HOUR'),        (86.8976, 'KNOT')),
            ((1,   'KILOMETER_PER_SECOND'), (2236.9363, 'MILE_PER_HOUR')),

            # Time
            ((1,   'YEAR'), (365.2425, 'DAY')),

            # Temperature
            ((12,     'CELSIUS'),     (12,        'CELSIUS')),
            ((294.5,  'KELVIN'),      (21.35,     'CELSIUS')),
            ((0,      'CELSIUS'),    (273.15,    'KELVIN')),
            ((3284.9, 'FAHRENHEIT'), (1807.1667, 'CELSIUS')),
            ((394.5,  'CELSIUS'),    (742.1,     'FAHRENHEIT')),

            # Density
            ((19.5, 'GRAM_PER_CENTIMETER_CUBIC'), (19500, 'KILOGRAM_PER_METER_CUBIC'))
        ]

        unitsIndex = units.getIndex(True, stubExchangeRate=True, currenciesExchangeRates={
            'EUR': 2.1,
            'GBP': 3.3
        })

        # Invalid case
        with self.assertRaises(Exception) as cm:
            convertUnit(
                {'value': 1.0, 'unit': unitsIndex['FOOT']},
                unitsIndex['GRAM']
            )
        self.assertEqual(str(cm.exception), "Sorry, I can't convert foot to gram (at least in this universe).")


        # Valid cases
        for fromUnit, toUnit in cases:
            fromValueUnit = {
                'value': float(fromUnit[0]),
                'unit': unitsIndex[fromUnit[1]]
            }

            toValueUnit = {
                'value': float(toUnit[0]),
                'unit': unitsIndex[toUnit[1]]
            }

            result = convertUnit(fromValueUnit, toValueUnit['unit'])
            result['value'] = round(result['value'], 4)

            self.assertEqual(
                result,
                toValueUnit
            )
