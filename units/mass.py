# -*- coding: utf-8 -*-
# Main symbol — µ (U+00B5), second — μ (U+03BC)
NANOGRAM =  (   1e-9,  [u'µg', 'nanogram', 'nanograms', 'nanogramme', 'nanogrammes', u'μg', 'ug'])
MILLIGRAM = (   0.001, ['mg', 'milligram', 'milligrams', 'milligramme', 'milligrammes'])
GRAM =      (   1,     ['g', 'gram', 'grams', 'gramme', 'grammes'])
KILOGRAM =  (1000,     ['kg', 'kilogram', 'kilograms', 'kilogramme', 'kilogrammes'])
TONNE =     (   1e6,   ['t', 'tonne', 'tonnes', 'megagramm', 'megagramms', 'megagramme', 'megamgrammes'])


POUND = (453.59237,     ['lb', 'pound', 'pounds'])
OUNCE = (POUND[0] / 16, ['oz', 'ounce', 'ounces'])


_BASE = GRAM
_TYPE = 'mass'
