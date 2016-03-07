# -*- coding: utf-8 -*-
import length as _l
import time as _t

def _getNames(base, lengthNames):
    return [name + ' ' + base for name in lengthNames[1:]]


_HOUR_VALUE = float(_t.HOUR[0])
_SECOND_VALUE = float(_t.SECOND[0])

METER_PER_SECOND =   (      _l.METER[0] / _SECOND_VALUE, ['m/s'] + _getNames('per second', _l.METER[1]))
KILOMETER_PER_HOUR = (    _l.KILOMETER[0] / _HOUR_VALUE, ['km/h'] + _getNames('per hour', _l.KILOMETER[1]) + ['km/hr'])
MILE_PER_HOUR =      (         _l.MILE[0] / _HOUR_VALUE, ['mph'] + _getNames('per hour', _l.MILE[1]) + ['mi/h', 'mi/hr'])
KNOT =               (_l.NAUTICAL_MILE[0] / _HOUR_VALUE, ['kn', 'knot', 'knots', 'kt'])
FOOT_PER_SECOND =    (       _l.FOOT[0] / _SECOND_VALUE, ['ft/s'] + _getNames('per second', _l.FOOT[1]))


_BASE = METER_PER_SECOND
_TYPE = 'speed'
