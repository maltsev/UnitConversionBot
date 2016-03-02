# -*- coding: utf-8 -*-
def convertUnit(fromValueUnit, toUnit):
    fromUnit = fromValueUnit['unit']

    if fromUnit['type'] != toUnit['type']:
        errorMessage = u"Sorry, I can't convert {} to {} (at least in this universe).".format(
            fromUnit['baseName'],
            toUnit['baseName']
        )
        raise IncompatibleCategoriesException(errorMessage)

    toValue = (fromValueUnit['value'] * fromUnit['value']) / toUnit['value']

    toValueUnit = {
        'value': toValue,
        'unit': toUnit
    }

    return toValueUnit



class IncompatibleCategoriesException(Exception):
    pass
