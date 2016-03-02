# -*- coding: utf-8 -*-
MILLISECOND = (           0.001,   ['ms', 'millisecond', 'milliseconds', 'millisec', 'msec'])
SECOND =      (           1,       ['s', 'second', 'seconds', 'sec'])
MINUTE =      (          60,       ['min', 'minute', 'minutes'])
HOUR =        (       60*60,       ['h', 'hour', 'hours'])
DAY =         (HOUR[0] * 24,       ['d', 'day', 'days'])
WEEK =        (  DAY[0] * 7,       ['wk', 'week', 'weeks'])
MONTH =       (DAY[0] * 30.436875, ['mon', 'month', 'months'])
YEAR =        (DAY[0] * 365.2425,  ['yr', 'year', 'years'])


_BASE = SECOND
_TYPE = 'time'
