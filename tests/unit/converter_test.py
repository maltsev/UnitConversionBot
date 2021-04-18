import pytest
from chalicelib.modules.converter import convertUnit
from chalicelib import units


def test_convertUnit():
    cases = [
        # Length
        ((1,    'FOOT'),              (0.3048,     'METER')),
        ((13,   'NAUTICAL_MILE'),     (24.076,     'KILOMETER')),
        ((10,   'ANGSTROM'),          (1,          'NANOMETER')),
        ((1000, 'ASTRONOMICAL_UNIT'), (0.0048,     'PARSEC')),
        ((1,    'LIGHT_YEAR'),        (63241.0771, 'ASTRONOMICAL_UNIT')),

        # Area
        ((50.5, 'FOOT_SQUARE'),       (4.6916, 'METER_SQUARE')),
        ((100,  'KILOMETER_SQUARE'),  (38.6102, 'MILE_SQUARE')),

        # Volume
        ((1.2,  'METER_CUBIC'),     (1200, 'LITER')),
        ((1234, 'MILLILITER'),      (1.234, 'LITER')),
        ((12,   'IMPERIAL_GALLON'), (54.5531, 'LITER')),
        ((1,    'CUP'),             (250, 'MILLILITER')),
        ((1,    'TEASPOON'),        (5, 'MILLILITER')),
        ((1,    'TABLESPOON'),      (15, 'MILLILITER')),
        ((1,    'US_FLUID_OUNCE'),  (29.5735, 'MILLILITER')),
        ((1,    'US_GILL'),         (118.2941, 'MILLILITER')),
        ((1,    'US_PINT'),         (473.1765, 'MILLILITER')),
        ((1,    'US_QUART'),        (946.3529, 'MILLILITER')),
        ((1,    'US_GALLON'),       (3.7854, 'LITER')),


        # Currencies
        ((2,     'USD'), (2,       'USD')),
        ((10.2,  'USD'), (8.5778,    'EUR')),
        ((10.3,  'GBP'), (13.2894,  'USD')),

        # Mass
        ((1.2, 'POUND'), (544.3108, 'GRAM')),
        ((500, 'OUNCE'), (31.25, 'POUND')),

        # Speed
        ((1,   'METER_PER_SECOND'),     (3.6, 'KILOMETER_PER_HOUR')),
        ((100, 'MILE_PER_HOUR'),        (86.8976, 'KNOT')),
        ((1,   'KILOMETER_PER_SECOND'), (2236.9363, 'MILE_PER_HOUR')),

        # Time
        ((1, 'YEAR'),   (365.2425, 'DAY')),
        ((1, 'MILLISECOND'), (1000000, 'NANOSECOND')),

        # Temperature
        ((12,     'CELSIUS'),     (12,        'CELSIUS')),
        ((294.5,  'KELVIN'),      (21.35,     'CELSIUS')),
        ((0,      'CELSIUS'),    (273.15,    'KELVIN')),
        ((3284.9, 'FAHRENHEIT'), (1807.1667, 'CELSIUS')),
        ((394.5,  'CELSIUS'),    (742.1,     'FAHRENHEIT')),

        # Density
        ((19.5, 'GRAM_PER_CENTIMETER_CUBIC'), (19500, 'KILOGRAM_PER_METER_CUBIC')),

        # Information
        ((1, 'GIGABYTE'), (1024, 'MEGABYTE')),
        ((1, 'BYTE'),     (8, 'BIT')),
        ((1, 'TERABYTE'), (1073741824, 'KILOBYTE')),

        # Pressure
        ((1, 'BAR'), (100000, 'PASCAL')),
        ((1, 'TECHNICAL_ATMOSPHERE'), (98.0665, 'KILOPASCAL')),
        ((1, 'STANDARD_ATMOSPHERE'), (1013.25, 'HECTOPASCAL')),
        ((1, 'TORR'), (133.3224, 'PASCAL')),
        ((1, 'POUND_PER_SQUARE_INCH'), (6894.7238, 'PASCAL')),
        ((1, 'KILOBAR'), (14503.8443, 'POUND_PER_SQUARE_INCH')),
        ((1, 'MEGABAR'), (986923.2667, 'STANDARD_ATMOSPHERE')),

        # Fuel consumption
        ((1, 'MILE_PER_US_GALLON'), (0.4251, 'KILOMETER_PER_LITER')),
        ((1, 'MILE_PER_US_GALLON'), (0.2642, 'MILE_PER_LITER')),
        ((1, 'MILE_PER_US_GALLON'), (1.6093, 'KILOMETER_PER_US_GALON')),

        # Power
        ((1, 'KILOWATT'), (1000, 'WATT')),
        ((1, 'METRIC_HORSEPOWER'), (735.4987, 'WATT')),
        ((1, 'MECHANICAL_HORSEPOWER'), (745.6999, 'WATT')),

        # Torque
        ((1, 'NEWTON_METER'), (0.7376, 'POUND_FOOT')),
        ((1, 'POUND_FOOT'), (1.3558, 'NEWTON_METER')),
    ]

    unitsIndex = units.getIndex()

    # Invalid case
    with pytest.raises(Exception) as cm:
        convertUnit(
            {'value': 1.0, 'unit': unitsIndex['FOOT']},
            unitsIndex['GRAM']
        )
        assert str(cm.exception) == "Sorry, I can't convert foot to gram (at least in this universe)."

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

        assert result == toValueUnit


def test_defaultUnits():
    skipCategories = ['currencies', 'temperature']
    skipUnits = ['METER_SQUARE', 'NANOMETER_SQUARE', 'NANOMETER_CUBIC', 'NANOSECOND']

    categoriesIndex = units.getCategoriesIndex()
    for categoryName, category in categoriesIndex.items():
        if categoryName in skipCategories:
            continue

        for unit in category.values():
            if unit['key'] in skipUnits:
                continue

            fromValueUnit = {
                'value': 1.0,
                'unit': unit
            }

            result = convertUnit(fromValueUnit, unit['defaultToUnit'])
            errorMessage = f"{unit['key']} and {unit['defaultToUnitKey']} are too different"
            assert 0.00001 < result['value'], errorMessage
