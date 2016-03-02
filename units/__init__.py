# -*- coding: utf-8 -*-
import sys
import length, mass, time, currency, area, volume, speed


def addToIndex(index, units):
    for constantName in dir(units):
        if constantName[0] == '_':
            continue

        packedUnit = getattr(units, constantName)
        unit = unpackUnit(packedUnit, units._TYPE)
        unit['names'].append(constantName)

        # unitNames could have duplicates, therefore use set()
        for unitName in set(unit['names']):
            if unitName in index:
                sys.exit(u'The unit "{}" is already defined'.format(unitName))

            index[unitName] = unit

    return index




def unpackUnit(packedUnit, type):
    try:
        unitNames = packedUnit[1]
    except TypeError as err:
        print packedUnit
        raise err

    return {
        'value': packedUnit[0],
        'type': type,
        'shortName': unitNames[0],
        'baseName': unitNames[1],
        'names': unitNames
    }


index = {}
index = addToIndex(index, currency)
index = addToIndex(index, length)
index = addToIndex(index, area)
index = addToIndex(index, volume)
index = addToIndex(index, mass)
index = addToIndex(index, time)
index = addToIndex(index, speed)
