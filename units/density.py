# -*- coding: utf-8 -*-
import volume as _v
import length as _l
import mass as _m


def _getNames(massNames, volumeNames, lengthNames=[]):
    volumeShortName = volumeNames[0]
    massShortName = massNames[0]
    names = [
        massShortName + '/' + volumeShortName, # kg/m³
    ]

    volumeAllNames = volumeNames[1:] + [volumeShortName] + lengthNames
    massAllNames = massNames[1:] + [massShortName]
    # Full name ("kilogram per cubic meter") must be at the start
    for massName in massAllNames:
        for volumeName in volumeAllNames:
            names.append(massName + ' per ' + volumeName)
            if ' ' not in massName and ' ' not in volumeName:
                names.append(massName + '/' + volumeName)

    return names


GRAM_PER_CENTIMETER_CUBIC = (_m.GRAM[0] / _v.CENTIMETER_CUBIC[0], _getNames(_m.GRAM[1], _v.CENTIMETER_CUBIC[1], _l.CENTIMETER[1]))
KILOGRAM_PER_METER_CUBIC =  (_m.KILOGRAM[0] / _v.METER_CUBIC[0],  _getNames(_m.KILOGRAM[1], _v.METER_CUBIC[1], _l.METER[1]))
KILOGRAM_PER_LITER =        (_m.KILOGRAM[0] / _v.LITER[0],        _getNames(_m.KILOGRAM[1], _v.LITER[1]))
GRAM_PER_MILLILITER =       (_m.GRAM[0] / _v.MILLILITER[0],       _getNames(_m.GRAM[1], _v.MILLILITER[1]))
TONNE_PER_METER_CUBIC =     (_m.TONNE[0] / _v.METER_CUBIC[0],     _getNames(_m.TONNE[1], _v.METER_CUBIC[1], _l.METER[1]))

_BASE = KILOGRAM_PER_METER_CUBIC
