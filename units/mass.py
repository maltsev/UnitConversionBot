# -*- coding: utf-8 -*-
from __future__ import division as _

# Main symbol — µ (U+00B5), second — μ (U+03BC)
NANOGRAM =  (   1e-9,  ['ng', 'nanogram', 'nanograms', 'nanogramme', 'nanogrammes'], 'MICROGRAM')
MICROGRAM = (   1e-6,  [u'µg', 'microgram', 'micrograms', 'microgramme', 'microgrammes', u'μg', 'ug'], 'MILLIGRAM')
MILLIGRAM = (   0.001, ['mg', 'milligram', 'milligrams', 'milligramme', 'milligrammes'], 'GRAM')
GRAM =      (   1,     ['g', 'gram', 'grams', 'gramme', 'grammes'], 'MILLIGRAM')
KILOGRAM =  (1000,     ['kg', 'kilogram', 'kilograms', 'kilogramme', 'kilogrammes'], 'POUND')
TONNE =     (   1e6,   ['t', 'tonne', 'tonnes', 'megagramm', 'megagramms', 'megagramme', 'megamgrammes'], 'KILOGRAM')


POUND = (453.59237,     ['lb', 'pound', 'pounds', 'lbm', 'lbs'], 'GRAM')
OUNCE = (POUND[0] / 16, ['oz', 'ounce', 'ounces'], 'GRAM')


_BASE = 'GRAM'
