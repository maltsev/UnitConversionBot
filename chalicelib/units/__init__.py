import logging
from chalicelib.modules.helpers import fetchExchangeRates
from chalicelib.units import (  # noqa: F401
    length, area, volume, currencies, mass, speed, time, temperature, density,
    information, pressure, fuel_consumption, power, torque
)

categories = [
    'length',
    'area',
    'volume',
    'currencies',
    'mass',
    'speed',
    'time',
    'temperature',
    'density',
    'information',
    'pressure',
    'fuel_consumption',
    'power',
    'torque',
]


def unpackUnit(packedUnit, unitKey, category, currenciesExchangeRates):
    unit = {
        'key': unitKey,
        'category': category,
    }

    try:
        defaultToUnitKey = packedUnit[-1]
        if category == 'currencies':
            value = currenciesExchangeRates.get(unitKey)
            if not value:
                return None
            value = 1 / value
            unitNames = packedUnit[0]
            defaultToUnitKey = currencies._BASE if len(packedUnit) < 2 else packedUnit[-1]
        elif category == 'temperature':
            value = 1
            unitNames = packedUnit[2]
            unit['convertFromBase'] = packedUnit[0]
            unit['convertToBase'] = packedUnit[1]
        else:
            value = packedUnit[0]
            unitNames = packedUnit[1]
    except TypeError as err:
        print(packedUnit)
        raise err

    unitNames = unitNames[:]
    unitNames.append(unitKey)

    unit['value'] = value
    unit['shortName'] = unitNames[0]
    unit['baseName'] = unitNames[1]
    unit['names'] = unitNames
    unit['defaultToUnitKey'] = defaultToUnitKey

    return unit


def getCategoriesIndex():
    index = getIndex()
    categoriesIndex = {}
    for unit in index.values():
        unitCategory = unit['category'].replace('_', ' ')
        if unitCategory not in categoriesIndex:
            categoriesIndex[unitCategory] = {}

        unitKey = unit['key']
        categoriesIndex[unitCategory][unitKey] = unit
    return categoriesIndex


def getIndex():
    exchange_rates = fetchExchangeRates()
    exchange_rates['MBTC'] = exchange_rates['BTC'] * 1000
    index = {}
    unitKeys = []
    globalVariables = globals()
    for categoryName in categories:
        categoryUnits = globalVariables[categoryName]
        for unitKey in dir(categoryUnits):
            if unitKey[0] == '_':
                continue

            packedUnit = getattr(categoryUnits, unitKey)
            unit = unpackUnit(packedUnit, unitKey, categoryName, exchange_rates)
            if not unit:
                logging.critical('{} is not available'.format(unitKey))
                continue

            if ' ' in unit['shortName']:
                logging.critical("The unit's '{}' shortName contains a whitespace".format(unit['shortName']))
                continue

            unitKeys.append(unitKey)

            allUnitNames = unit['names'] + [name.lower() for name in unit['names']]
            # unitNames could have duplicates, therefore use set()
            for unitName in set(allUnitNames):
                if unitName in index:
                    logging.critical("The unit '{}' is already defined".format(unitName))

                index[unitName] = unit

    for unitKey in unitKeys:
        unit = index[unitKey]
        if 'defaultToUnit' not in unit:
            unit['defaultToUnit'] = index[unit['defaultToUnitKey']]

    getIndex.index = index
    return index
