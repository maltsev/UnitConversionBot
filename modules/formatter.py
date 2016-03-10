# -*- coding: utf-8 -*-
def formatValueUnit(valueUnit):
    strValue = u'{:,.3f}'.format(valueUnit['value']).rstrip('0').rstrip('.')
    strUnit = valueUnit['unit']['shortName']

    return strValue + ' ' + strUnit




def formatAvailableUnits(unitsIndex):
    units = unitsIndex.values()
    if len(units) == 0:
        return ''

    unitsCategoryName = units[0]['category']
    isCurrencies = unitsCategoryName == 'currencies'
    if isCurrencies:
        units.sort(key=lambda x: x['baseName'])
    else:
        # Some units may have equal value (like dm3 and liter)
        # To make sorting stable we're sorting by value and baseName
        units.sort(key=lambda x: (x['value'], x['baseName']))

    unitsList = ''
    for unit in units:
        if isCurrencies:
            # Hack: use short name of currency (e.g., "forint" instead of "Hungarian Forint") in help
            safeShortName = unit['names'][-2] if len(unit['names']) > 3 else unit['shortName']
        else:
            safeShortName = unit['shortName'].replace(u'µ', 'u').replace(u'²', '2').replace(u'³', '3')
        unitsList += u'- {} `{}`\n'.format(unit['baseName'], safeShortName)

    return unitsList.strip()
