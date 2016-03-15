# -*- coding: utf-8 -*-
import length as _l

def _getNames(lengthNames):
    shortName = lengthNames[0]
    names = [shortName + u'²']
    # Full name ("square meter") must be at the start
    for lengthName in lengthNames[1:] + [shortName]:
        names.append('square ' + lengthName)
        names.append('sq ' + lengthName)
        names.append(lengthName + '^2')
        names.append(lengthName + u'²')

    names.append(shortName + '2')
    return names


NANOMETER_SQUARE =  (_l.NANOMETER[0]**2,  _getNames(_l.NANOMETER[1]), 'MILLIMETER_SQUARE')
MILLIMETER_SQUARE = (_l.MILLIMETER[0]**2, _getNames(_l.MILLIMETER[1]), 'CENTIMETER_SQUARE')
CENTIMETER_SQUARE = (_l.CENTIMETER[0]**2, _getNames(_l.CENTIMETER[1]), 'METER_SQUARE')
DECIMETER_SQUARE =  (_l.DECIMETER[0]**2,  _getNames(_l.DECIMETER[1]), 'METER_SQUARE')
METER_SQUARE =      (_l.METER[0]**2,      _getNames(_l.METER[1]), 'KILOMETER_SQUARE')
HECTARE =           (_l.HECTOMETER[0]**2, ['ha', 'hectare', 'hectares', 'hectar', 'hectars'] + _getNames(_l.HECTOMETER[1]), 'METER_SQUARE')
KILOMETER_SQUARE =  (_l.KILOMETER[0]**2,  _getNames(_l.KILOMETER[1]), 'METER_SQUARE')

INCH_SQUARE = (_l.INCH[0]**2, _getNames(_l.INCH[1]), 'CENTIMETER_SQUARE')
FOOT_SQUARE = (_l.FOOT[0]**2, _getNames(_l.FOOT[1]), 'CENTIMETER_SQUARE')
YARD_SQUARE = (_l.YARD[0]**2, _getNames(_l.YARD[1]), 'METER_SQUARE')
ACRE =        (YARD_SQUARE[0] * 4840, ['ac', 'acre', 'acres'], 'METER_SQUARE')
MILE_SQUARE = (_l.MILE[0]**2, _getNames(_l.MILE[1]), 'KILOMETER_SQUARE')


_BASE = 'METER_SQUARE'
