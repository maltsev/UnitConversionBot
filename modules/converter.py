# -*- coding: utf-8 -*-
def convertUnit(fromValueUnit, toUnit):
    fromUnit = fromValueUnit['unit']

    if fromUnit['category'] != toUnit['category']:
        errorMessage = u"Sorry, I can't convert {} to {} (at least in this universe).".format(
            fromUnit['baseName'],
            toUnit['baseName']
        )
        raise IncompatibleCategoriesException(errorMessage)

    if fromUnit['category'] == 'temperature':
        baseUnitToValue = fromUnit['convertToBase'](fromValueUnit['value'])
        toValue = toUnit['convertFromBase'](baseUnitToValue)
    else:
        toValue = (fromValueUnit['value'] * fromUnit['value']) / toUnit['value']

    toValueUnit = {
        'value': toValue,
        'unit': toUnit
    }

    return toValueUnit



class IncompatibleCategoriesException(Exception):
    pass
