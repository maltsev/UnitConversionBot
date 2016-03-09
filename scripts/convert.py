# -*- coding: utf-8 -*-
import sys
sys.path.append('.')

from modules.parser import parseExpression
from modules.converter import convertUnit
from modules.formatter import formatValueUnit

if len(sys.argv) < 2:
    expressions = [line.strip().decode('utf-8') for line in sys.stdin]
else:
    expressions = [' '.join(sys.argv[1:]).decode('utf-8').strip()]

for expression in expressions:
    try:
        units = parseExpression(expression)
        toValueUnit = convertUnit(units['fromValueUnit'], units['toUnit'])
        print formatValueUnit(toValueUnit).encode('utf-8')
    except Exception as error:
        sys.stderr.write(u'{:32s} {}\n'.format(error.__class__.__name__, expression).encode('utf-8'))
