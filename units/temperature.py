# -*- coding: utf-8 -*-
CELSIUS =    (lambda C: C,              lambda C: C,
[u'°C', 'Celsius', 'Degree Celsius', 'Degrees Celsius', 'Celsius Degree', 'Celsius Degrees', 'C'], 'FAHRENHEIT')

FAHRENHEIT = (lambda C: (C * 1.8) + 32, lambda F: (F - 32) * 5/9,
[u'°F', 'Fahrenheit', 'Degree Fahrenheit', 'Degrees Fahrenheit', 'Fahrenheit Degree', 'Fahrenheit Degrees', 'F'], 'CELSIUS')

KELVIN =     (lambda C: C + 273.15,     lambda K: K - 273.15,
[u'K', 'Kelvin', 'Degree Kelvin', 'Degrees Kelvin', 'Kelvin Degree', 'Kelvin Degrees', 'K'], 'CELSIUS')

#RANKINE =    (lambda C: (C + 273.15) * 5/9, lambda R: (R - 491.67) * 5/9, [])
#DELISLE =    (lambda C: (100 - C) * 3/2,    lambda De: 100 - (De * 2/3),  [])

_BASE = 'CELSIUS'
