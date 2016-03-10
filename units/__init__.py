# -*- coding: utf-8 -*-
import sys
import length, mass, time, currencies, area, volume, speed


def addToIndex(index, units):
    for unitKey in dir(units):
        if unitKey[0] == '_':
            continue

        packedUnit = getattr(units, unitKey)
        unit = unpackUnit(packedUnit, unitKey, units._TYPE)
        if ' ' in unit['shortName']:
            sys.exit('The unit\'s "{}" shortName contains a whitespace'.format(unitName))

        allUnitNames = unit['names'] + [name.lower() for name in unit['names']]
        # unitNames could have duplicates, therefore use set()
        for unitName in set(allUnitNames):
            if unitName in index:
                sys.exit(u'The unit "{}" is already defined'.format(unitName))

            index[unitName] = unit

    return index




def unpackUnit(packedUnit, unitKey, type):
    try:
        unitNames = packedUnit[1]
    except TypeError as err:
        print packedUnit
        raise err

    unitNames.append(unitKey)

    return {
        'value': packedUnit[0],
        'type': type,
        'shortName': unitNames[0],
        'baseName': unitNames[1],
        'names': unitNames
    }


index = {}
index = addToIndex(index, currencies)
index = addToIndex(index, length)
index = addToIndex(index, area)
index = addToIndex(index, volume)
index = addToIndex(index, mass)
index = addToIndex(index, time)
index = addToIndex(index, speed)
