from chalicelib.units import length as _l, time as _t
from chalicelib.modules.helpers import generateCompositeNames as _getNames


_SECOND_VALUE = float(_t.SECOND[0])
_MINUTE_VALUE = float(_t.MINUTE[0])
_HOUR_VALUE = float(_t.HOUR[0])


METER_PER_SECOND = (
    _l.METER[0] / _SECOND_VALUE,
    _getNames(_l.METER[1], _t.SECOND[1]),
    "KILOMETER_PER_HOUR",
)
METER_PER_MINUTE = (
    _l.METER[0] / _MINUTE_VALUE,
    _getNames(_l.METER[1], _t.MINUTE[1]),
    "METER_PER_SECOND",
)
METER_PER_HOUR = (
    _l.METER[0] / _HOUR_VALUE,
    _getNames(_l.METER[1], _t.HOUR[1]),
    "KILOMETER_PER_HOUR",
)

KILOMETER_PER_SECOND = (
    _l.KILOMETER[0] / _SECOND_VALUE,
    _getNames(_l.KILOMETER[1], _t.SECOND[1]),
    "KILOMETER_PER_HOUR",
)
KILOMETER_PER_MINUTE = (
    _l.KILOMETER[0] / _MINUTE_VALUE,
    _getNames(_l.KILOMETER[1], _t.MINUTE[1]),
    "KILOMETER_PER_HOUR",
)
KILOMETER_PER_HOUR = (
    _l.KILOMETER[0] / _HOUR_VALUE,
    _getNames(_l.KILOMETER[1], _t.HOUR[1]) + ["kmph", "kmh", "kph"],
    "METER_PER_SECOND",
)

MILE_PER_SECOND = (
    _l.MILE[0] / _SECOND_VALUE,
    _getNames(_l.MILE[1], _t.SECOND[1]),
    "KILOMETER_PER_HOUR",
)
MILE_PER_MINUTE = (
    _l.MILE[0] / _MINUTE_VALUE,
    _getNames(_l.MILE[1], _t.MINUTE[1]),
    "KILOMETER_PER_HOUR",
)
MILE_PER_HOUR = (
    _l.MILE[0] / _HOUR_VALUE,
    _getNames(_l.MILE[1], _t.HOUR[1], "mph"),
    "KILOMETER_PER_HOUR",
)

FOOT_PER_SECOND = (
    _l.FOOT[0] / _SECOND_VALUE,
    _getNames(_l.FOOT[1], _t.SECOND[1]),
    "METER_PER_SECOND",
)
FOOT_PER_MINUTE = (
    _l.FOOT[0] / _MINUTE_VALUE,
    _getNames(_l.FOOT[1], _t.MINUTE[1]),
    "METER_PER_SECOND",
)
FOOT_PER_HOUR = (
    _l.FOOT[0] / _HOUR_VALUE,
    _getNames(_l.FOOT[1], _t.HOUR[1]),
    "METER_PER_HOUR",
)

KNOT = (
    _l.NAUTICAL_MILE[0] / _HOUR_VALUE,
    ["kn", "knot", "knots", "kt"],
    "KILOMETER_PER_HOUR",
)


_BASE = "METER_PER_SECOND"
