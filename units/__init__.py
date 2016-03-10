# -*- coding: utf-8 -*-
import sys
import units
import length, area, volume, currencies, mass, speed, time

categories = ['length', 'area', 'volume', 'currencies', 'mass', 'speed', 'time']



def unpackUnit(packedUnit, unitKey, category):
    try:
        unitNames = packedUnit[1]
    except TypeError as err:
        print packedUnit
        raise err

    unitNames.append(unitKey)

    return {
        'value': packedUnit[0],
        'category': category,
        'shortName': unitNames[0],
        'baseName': unitNames[1],
        'names': unitNames
    }


index = {}
categoriesIndex = {categoryName: {} for categoryName in categories}
localVariables = locals()
for categoryName in categories:
    categoryUnits = localVariables[categoryName]
    for unitKey in dir(categoryUnits):
        if unitKey[0] == '_':
            continue

        packedUnit = getattr(categoryUnits, unitKey)
        unit = unpackUnit(packedUnit, unitKey, categoryName)
        if ' ' in unit['shortName']:
            sys.exit('The unit\'s "{}" shortName contains a whitespace'.format(unitName))

        categoriesIndex[categoryName][unitKey] = unit

        allUnitNames = unit['names'] + [name.lower() for name in unit['names']]
        # unitNames could have duplicates, therefore use set()
        for unitName in set(allUnitNames):
            if unitName in index:
                sys.exit(u'The unit "{}" is already defined'.format(unitName))

            index[unitName] = unit
