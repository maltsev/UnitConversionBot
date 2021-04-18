from chalicelib.units import volume as _v, length as _l, mass as _m
from chalicelib.modules.helpers import generateCompositeNames as _getNames


GRAM_PER_CENTIMETER_CUBIC = (
    _m.GRAM[0] / _v.CENTIMETER_CUBIC[0],
    _getNames(_m.GRAM[1], _v.CENTIMETER_CUBIC[1] + _l.CENTIMETER[1]),
    'KILOGRAM_PER_METER_CUBIC'
)

GRAM_PER_MILLILITER = (
    _m.GRAM[0] / _v.MILLILITER[0],
    _getNames(_m.GRAM[1], _v.MILLILITER[1]),
    'KILOGRAM_PER_METER_CUBIC'
)

GRAM_PER_METER_CUBIC = (
    _m.GRAM[0] / _v.METER_CUBIC[0],
    _getNames(_m.GRAM[1], _v.METER_CUBIC[1] + _l.METER[1]),
    'KILOGRAM_PER_METER_CUBIC'
)

KILOGRAM_PER_METER_CUBIC = (
    _m.KILOGRAM[0] / _v.METER_CUBIC[0],
    _getNames(_m.KILOGRAM[1], _v.METER_CUBIC[1] + _l.METER[1]),
    'GRAM_PER_CENTIMETER_CUBIC'
)

KILOGRAM_PER_LITER = (
    _m.KILOGRAM[0] / _v.LITER[0],
    _getNames(_m.KILOGRAM[1], _v.LITER[1]),
    'KILOGRAM_PER_METER_CUBIC'
)

TONNE_PER_METER_CUBIC = (
    _m.TONNE[0] / _v.METER_CUBIC[0],
    _getNames(_m.TONNE[1], _v.METER_CUBIC[1] + _l.METER[1]),
    'KILOGRAM_PER_METER_CUBIC'
)

POUND_PER_IMPERIAL_GALLON = (
    _m.POUND[0] / _v.IMPERIAL_GALLON[0],
    _getNames(_m.POUND[1], _v.IMPERIAL_GALLON[1]),
    'KILOGRAM_PER_METER_CUBIC'
)

_BASE = 'KILOGRAM_PER_METER_CUBIC'
