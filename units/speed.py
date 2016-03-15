# -*- coding: utf-8 -*-
import length as _l
import time as _t


def _getNames(base, lengthNames):
    return [name + ' ' + base for name in lengthNames[1:]]


_SECOND_VALUE = float(_t.SECOND[0])
_MINUTE_VALUE = float(_t.MINUTE[0])
_HOUR_VALUE = float(_t.HOUR[0])


METER_PER_SECOND = (_l.METER[0] / _SECOND_VALUE, ['m/s'] + _getNames('per second', _l.METER[1]), 'KILOMETER_PER_HOUR')
METER_PER_MINUTE = (_l.METER[0] / _MINUTE_VALUE, ['m/min'] + _getNames('per minute', _l.METER[1]), 'METER_PER_SECOND')
METER_PER_HOUR =   (_l.METER[0] / _HOUR_VALUE,   ['m/h'] + _getNames('per hour', _l.METER[1]) + ['m/hr'], 'KILOMETER_PER_HOUR')

KILOMETER_PER_SECOND = (_l.KILOMETER[0] / _SECOND_VALUE, ['km/s'] + _getNames('per second', _l.KILOMETER[1]), 'KILOMETER_PER_HOUR')
KILOMETER_PER_MINUTE = (_l.KILOMETER[0] / _MINUTE_VALUE, ['km/min'] + _getNames('per minute', _l.KILOMETER[1]), 'KILOMETER_PER_HOUR')
KILOMETER_PER_HOUR =   (_l.KILOMETER[0] / _HOUR_VALUE,   ['km/h'] + _getNames('per hour', _l.KILOMETER[1]) + ['km/hr', 'kmph', 'kmh'], 'METER_PER_SECOND')

MILE_PER_SECOND = (_l.MILE[0] / _SECOND_VALUE, ['mi/s'] + _getNames('per second', _l.MILE[1]), 'KILOMETER_PER_HOUR')
MILE_PER_MINUTE = (_l.MILE[0] / _MINUTE_VALUE, ['mi/min'] + _getNames('per minute', _l.MILE[1]), 'KILOMETER_PER_HOUR')
MILE_PER_HOUR =   (_l.MILE[0] / _HOUR_VALUE,   ['mph'] + _getNames('per hour', _l.MILE[1]) + ['mi/h', 'mi/hr', 'mp/h'], 'KILOMETER_PER_HOUR')

FOOT_PER_SECOND = (_l.FOOT[0] / _SECOND_VALUE, ['ft/s'] + _getNames('per second', _l.FOOT[1]), 'METER_PER_SECOND')
FOOT_PER_MINUTE = (_l.FOOT[0] / _MINUTE_VALUE, ['ft/min'] + _getNames('per minute', _l.FOOT[1]), 'METER_PER_SECOND')
FOOT_PER_HOUR =   (_l.FOOT[0] / _HOUR_VALUE,   ['ft/h'] + _getNames('per hour', _l.FOOT[1]) + ['ft/hr'], 'METER_PER_HOUR')

KNOT = (_l.NAUTICAL_MILE[0] / _HOUR_VALUE, ['kn', 'knot', 'knots', 'kt'], 'KILOMETER_PER_HOUR')


_BASE = 'METER_PER_SECOND'
