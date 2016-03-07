# -*- coding: utf-8 -*-
NANOMETER =  (   1e-9,  ['nm', 'nanometer', 'nanometers', 'nanometre', 'nanometres'])
# Main symbol — µ (U+00B5), second — μ (U+03BC)
MICROMETER = (   1e-6,  [u'µm', 'micrometer', 'micrometers', 'micrometre', 'micrometres', u'μm', 'um'])
MILLIMETER = (   0.001, ['mm', 'millimeter', 'millimeters', 'millimetre', 'millimetres'])
CENTIMETER = (   0.01,  ['cm', 'centimeter', 'centimeters', 'centimetre', 'centimetres'])
DECIMETER =  (   0.1,   ['dm', 'decimeter', 'decimeters', 'decimetre', 'decimetres'])
METER =      (   1,     ['m',  'meter', 'meters', 'metre', 'metres'])
HECTOMETER = ( 100,     ['hm', 'hectometer', 'hectometers', 'hectometre', 'hectometres'])
KILOMETER =  (1000,     ['km', 'kilometer', 'kilometers', 'kilometre', 'kilometres'])

INCH = (0.0254,         ['in', 'inch', 'inches'])
FOOT = (INCH[0] * 12,   ['ft', 'foot', 'feet'])
YARD = (INCH[0] * 36,   ['yd', 'yard', 'yards'])
MILE = (FOOT[0] * 5280, ['mi', 'mile', 'miles'])

NAUTICAL_MILE = (1852, ['nmi', 'nautical mile', 'nautical miles'])

_BASE = METER
_TYPE = 'length'
