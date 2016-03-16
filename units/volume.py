# -*- coding: utf-8 -*-
from __future__ import division as _
import length as _l

def _getNames(lengthNames):
    shortName = lengthNames[0]
    names = [shortName + u'³']
    # Full name ("cubic meter") must be at the start
    for lengthName in lengthNames[1:] + [shortName]:
        names.append('cubic ' + lengthName)
        names.append('cu ' + lengthName)
        names.append(lengthName + '^3')
        names.append(lengthName + u'³')

    names.append(shortName + '3')
    return names


NANOMETER_CUBIC =  ( _l.NANOMETER[0]**3, _getNames(_l.NANOMETER[1]), 'MILLIMETER_CUBIC')
MILLIMETER_CUBIC = (_l.MILLIMETER[0]**3, _getNames(_l.MILLIMETER[1]), 'CENTIMETER_CUBIC')
CENTIMETER_CUBIC = (_l.CENTIMETER[0]**3, _getNames(_l.CENTIMETER[1]) + ['cc'], 'MILLILITER')
DECIMETER_CUBIC =  ( _l.DECIMETER[0]**3, _getNames(_l.DECIMETER[1]), 'MILLILITER')
METER_CUBIC =      (     _l.METER[0]**3, _getNames(_l.METER[1]), 'CENTIMETER_CUBIC')
KILOMETER_CUBIC =  ( _l.KILOMETER[0]**3, _getNames(_l.KILOMETER[1]), 'METER_CUBIC')

LITER =      ( DECIMETER_CUBIC[0], ['l', 'liter', 'liters', 'litre', 'litres', 'lt', 'ltr'], 'MILLILITER')
MILLILITER = (CENTIMETER_CUBIC[0], ['ml', 'milliliter', 'milliliters', 'millilitre', 'millilitres'], 'LITER')

INCH_CUBIC = (_l.INCH[0]**3, _getNames(_l.INCH[1]), 'CENTIMETER_CUBIC')
FOOT_CUBIC = (_l.FOOT[0]**3, _getNames(_l.FOOT[1]), 'METER_CUBIC')
YARD_CUBIC = (_l.YARD[0]**3, _getNames(_l.YARD[1]), 'METER_CUBIC')
MILE_CUBIC = (_l.MILE[0]**3, _getNames(_l.MILE[1]), 'KILOMETER_CUBIC')

IMPERIAL_FLUID_OUNCE = ( MILLILITER[0] * 28.4130625, ['fl.oz', 'imperial fluid ounce', 'imperial fluid ounces', 'fluid ounce', 'fluid ounces'], 'MILLILITER')
IMPERIAL_PINT        = (IMPERIAL_FLUID_OUNCE[0] * 20,         ['pt', 'imperial pint', 'imperial pints', 'pint', 'pints'], 'MILLILITER')
IMPERIAL_QUART       = (IMPERIAL_FLUID_OUNCE[0] * 40,         ['qt', 'imperial quart', 'imperial quarts', 'quart', 'quarts'], 'LITER')
IMPERIAL_GALLON      = (IMPERIAL_FLUID_OUNCE[0] * 160,        ['gal', 'imperial gallon', 'imperial gallons', 'gallon', 'gallons'], 'LITER')


_BASE = 'METER_CUBIC'
