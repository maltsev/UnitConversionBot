# -*- coding: utf-8 -*-
from __future__ import division as _

MILLISECOND = (           0.001,   ['ms', 'millisecond', 'milliseconds', 'millisec', 'msec'], 'SECOND')
SECOND =      (           1,       ['s', 'second', 'seconds', 'sec'], 'MILLISECOND')
MINUTE =      (          60,       ['min', 'minute', 'minutes'], 'SECOND')
HOUR =        (       60*60,       ['h', 'hour', 'hours', 'hr'], 'MINUTE')
DAY =         (HOUR[0] * 24,       ['d', 'day', 'days'], 'HOUR')
WEEK =        (  DAY[0] * 7,       ['wk', 'week', 'weeks'], 'DAY')
MONTH =       (DAY[0] * 30.436875, ['mon', 'month', 'months'], 'DAY')
YEAR =        (DAY[0] * 365.2425,  ['yr', 'year', 'years', 'y'], 'DAY')


_BASE = 'SECOND'
