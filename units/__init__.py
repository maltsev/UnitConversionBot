# -*- coding: utf-8 -*-
import os
import sys
import logging
import units
import length, area, volume, currencies, mass, speed, time
import model

categories = ['length', 'area', 'volume', 'currencies', 'mass', 'speed', 'time']


def unpackUnit(packedUnit, unitKey, category, **kwargs):
    try:
        if category == 'currencies':
            stubValue = 1.0 if kwargs.get('stubExchangeRate') else None
            value = kwargs.get('currenciesExchangeRates', {}).get(unitKey, stubValue)
            if not value:
                return None
            value = 1 / value
            unitNames = packedUnit[:]
        else:
            value = packedUnit[0]
            unitNames = packedUnit[1][:]
    except TypeError as err:
        print packedUnit
        raise err

    unitNames.append(unitKey)

    return {
        'key': unitKey,
        'value': value,
        'category': category,
        'shortName': unitNames[0],
        'baseName': unitNames[1],
        'names': unitNames
    }



def getCategoriesIndex(regenerate=False, **kwargs):
    if not regenerate and hasattr(getCategoriesIndex, 'categoriesIndex'):
        return getCategoriesIndex.categoriesIndex

    index = getIndex(regenerate, **kwargs)
    categoriesIndex = {}
    for unit in index.values():
        unitCategory = unit['category']
        if unitCategory not in categoriesIndex:
            categoriesIndex[unitCategory] = {}

        unitKey = unit['key']
        categoriesIndex[unitCategory][unitKey] = unit

    getCategoriesIndex.categoriesIndex = categoriesIndex
    return categoriesIndex



def getIndex(regenerate=False, **kwargs):
    if not regenerate and hasattr(getIndex, 'index'):
        return getIndex.index

    index = {}
    globalVariables = globals()
    for categoryName in categories:
        categoryUnits = globalVariables[categoryName]
        for unitKey in dir(categoryUnits):
            if unitKey[0] == '_':
                continue

            packedUnit = getattr(categoryUnits, unitKey)
            unit = unpackUnit(packedUnit, unitKey, categoryName, **kwargs)
            if not unit:
                logging.critical('{} is not available'.format(unitKey))
                continue

            if ' ' in unit['shortName']:
                logging.critical("The unit's '{}' shortName contains a whitespace".format(unitName))
                continue

            allUnitNames = unit['names'] + [name.lower() for name in unit['names']]
            # unitNames could have duplicates, therefore use set()
            for unitName in set(allUnitNames):
                if unitName in index:
                    logging.critical(u"The unit '{}' is already defined".format(unitName))

                index[unitName] = unit


    getIndex.index = index
    return index
