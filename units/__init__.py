# -*- coding: utf-8 -*-
import os
import sys
import logging
import units
import length, area, volume, currencies, mass, speed, time, temperature, density

categories = [
    'length',
    'area',
    'volume',
    'currencies',
    'mass',
    'speed',
    'time',
    'temperature',
    'density'
]


def unpackUnit(packedUnit, unitKey, category, **kwargs):
    unit = {
        'key': unitKey,
        'category': category,
    }

    try:
        if category == 'currencies':
            stubValue = 1.0 if kwargs.get('stubExchangeRate') else None
            value = kwargs.get('currenciesExchangeRates', {}).get(unitKey, stubValue)
            if not value:
                return None
            value = 1 / value
            unitNames = packedUnit
        elif category == 'temperature':
            value = 1
            unitNames = packedUnit[2]
            unit['convertFromBase'] = packedUnit[0]
            unit['convertToBase'] = packedUnit[1]
        else:
            value = packedUnit[0]
            unitNames = packedUnit[1]
    except TypeError as err:
        print packedUnit
        raise err

    unitNames = unitNames[:]
    unitNames.append(unitKey)

    unit['value'] = value
    unit['shortName'] = unitNames[0]
    unit['baseName'] = unitNames[1]
    unit['names'] = unitNames

    return unit



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
