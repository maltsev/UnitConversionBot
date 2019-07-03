# -*- coding: utf-8 -*-
from __future__ import division as _
import length as _l
import volume as _v
from modules.helpers import generateCompositeNames as _getNames

MILE_PER_US_GALLON = (
    _l.MILE[0] / float(_v.US_GALLON[0]),
    _getNames(_l.MILE[1], _v.US_GALLON[1], 'mpg'),
    'KILOMETER_PER_LITER'
)

MILE_PER_LITER = (
    _l.MILE[0] / float(_v.LITER[0]),
    _getNames(_l.MILE[1], _v.LITER[1]),
    'MILE_PER_US_GALLON'
)

KILOMETER_PER_LITER = (
    _l.KILOMETER[0] / float(_v.LITER[0]),
    _getNames(_l.KILOMETER[1], _v.LITER[1]),
    'MILE_PER_US_GALLON'
)

KILOMETER_PER_US_GALON = (
    _l.KILOMETER[0] / float(_v.US_GALLON[0]),
    _getNames(_l.KILOMETER[1], _v.US_GALLON[1]),
    'MILE_PER_US_GALLON'
)


_BASE = 'KILOMETER_PER_LITER'



# Requires lambda for conversion
# LITER_PER_100_KM = (
#     100 / KILOMETER_PER_LITER[0],
#     _getNames(_v.LITER[1], ['100 ' + _x for _x in _l.KILOMETER[1]], 'l/100km', 'liter per 100 kilometers'),
#     'KILOMETER_PER_LITER'
# )
