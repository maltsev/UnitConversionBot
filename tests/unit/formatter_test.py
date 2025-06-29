from chalicelib.modules.formatter import formatValueUnit
from chalicelib import units


def test_formatValueUnit():
    cases = [
        (5.23, "EUR", "5.23 €"),
        (123456789, "FOOT", "123,456,789 ft"),
        (3.140, "METER", "3.14 m"),
        (1.5, "FOOT_SQUARE", "1.5 ft²"),
        (1.0 / 3, "KILOGRAM", "0.333 kg"),
        (0, "HOUR", "0 h"),
        (-100, "DAY", "-100 d"),
        (1200, "IMPERIAL_FLUID_OUNCE", "1,200 fl.oz"),
        (1.2, "KILOMETER_PER_HOUR", "1.2 km/h"),
    ]

    unitsIndex = units.getIndex()
    for value, unitName, formattedValueUnit in cases:
        assert (
            formatValueUnit({"value": value, "unit": unitsIndex[unitName]})
            == formattedValueUnit
        )
