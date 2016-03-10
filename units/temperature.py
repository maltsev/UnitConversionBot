# -*- coding: utf-8 -*-
CELSIUS =    (                       1, ['°C', 'Celsius', 'C'])
FAHRENHEIT = (lambda c: (c * 1.8) + 32, ['°F', 'Fahrenheit', 'F'])
KELVIN =     (lambda c:     c + 273.15, ['K', 'Kelvin', 'K'])

_BASE = CELSIUS
