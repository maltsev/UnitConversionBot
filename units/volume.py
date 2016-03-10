# -*- coding: utf-8 -*-
import length as _l

def _getNames(lengthNames):
    shortName = lengthNames[0]
    names = [shortName + u'³']
    for lengthName in lengthNames[1:]:
        names.append('cubic ' + lengthName)
        names.append('cu ' + lengthName)

    names.append(shortName + '3')
    names.append(shortName + '^3')
    return names


NANOMETER_CUBIC =  ( _l.NANOMETER[0]**3, _getNames(_l.NANOMETER[1]))
MILLIMETER_CUBIC = (_l.MILLIMETER[0]**3, _getNames(_l.MILLIMETER[1]))
CENTIMETER_CUBIC = (_l.CENTIMETER[0]**3, _getNames(_l.CENTIMETER[1]))
DECIMETER_CUBIC =  ( _l.DECIMETER[0]**3, _getNames(_l.DECIMETER[1]))
METER_CUBIC =      (     _l.METER[0]**3, _getNames(_l.METER[1]))
KILOMETER_CUBIC =  ( _l.KILOMETER[0]**3, _getNames(_l.KILOMETER[1]))

LITER =      ( DECIMETER_CUBIC[0], ['l', 'liter', 'liters', 'litre', 'litres', 'lt', 'ltr'])
MILLILITER = (CENTIMETER_CUBIC[0], ['ml', 'milliliter', 'milliliters', 'millilitre', 'millilitres'])

INCH_CUBIC = (_l.INCH[0]**3, _getNames(_l.INCH[1]))
FOOT_CUBIC = (_l.FOOT[0]**3, _getNames(_l.FOOT[1]))
YARD_CUBIC = (_l.YARD[0]**3, _getNames(_l.YARD[1]))
MILE_CUBIC = (_l.MILE[0]**3, _getNames(_l.MILE[1]))

IMPERIAL_FLUID_OUNCE = ( MILLILITER[0] * 28.4130625, ['fl.oz', 'imperial fluid ounce', 'imperial fluid ounces', 'fluid ounce', 'fluid ounces'])
IMPERIAL_PINT        = (IMPERIAL_FLUID_OUNCE[0] * 20,         ['pt', 'imperial pint', 'imperial pints', 'pint', 'pints'])
IMPERIAL_QUART       = (IMPERIAL_FLUID_OUNCE[0] * 40,         ['qt', 'imperial quart', 'imperial quarts', 'quart', 'quarts'])
IMPERIAL_GALLON      = (IMPERIAL_FLUID_OUNCE[0] * 160,        ['gal', 'imperial gallon', 'imperial gallons', 'gallon', 'gallons'])


_BASE = METER_CUBIC
