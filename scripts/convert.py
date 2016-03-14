# -*- coding: utf-8 -*-
import sys
import json
sys.path.append('.')

from modules.parser import parseExpression, parseMessageText
from modules.converter import convertUnit
from modules.formatter import formatValueUnit
import units

if len(sys.argv) < 2:
    expressions = [line.strip().decode('utf-8') for line in sys.stdin]
else:
    expressions = [' '.join(sys.argv[1:]).decode('utf-8').strip()]

file = open('./tests/exchangeRates.json', 'r')
exchangeRates = json.loads(file.read())['rates']
file.close()
unitsIndex = units.getIndex(True, currenciesExchangeRates=exchangeRates)
for expression in expressions:
    try:
        units = parseExpression(parseMessageText(expression)['expression'], unitsIndex)
        toValueUnit = convertUnit(units['fromValueUnit'], units['toUnit'])
        print formatValueUnit(toValueUnit).encode('utf-8')
    except Exception as error:
        sys.stderr.write(u'{:32s} {}\n'.format(error.__class__.__name__, expression).encode('utf-8'))
