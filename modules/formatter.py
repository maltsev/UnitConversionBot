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
        baseName = unit['baseName']
        formatTemplate = u'- {} `{}`\n'

        if isCurrencies:
            # Hack: use short name of currency (e.g., "forint" instead of "Hungarian Forint") in help
            safeShortName = unit['names'][-2] if len(unit['names']) > 3 else unit['shortName']

            # Telegram message's text must be less than 4096 chars.
            # The currencies list is big, so we've to shorten it somehow.
            baseName = baseName.replace('United Arab Emirates', 'UAE')
            if safeShortName.isupper() or len(safeShortName) < 3:
                formatTemplate = u'- {} {}\n'

        else:
            safeShortName = massReplace(unit['shortName'], {
                u'µ': 'u',
                u'²': '2',
                u'³': '3',
                u'°': ''
            })
        unitsList += formatTemplate.format(baseName, safeShortName)

    return unitsList.strip()



def massReplace(string, replace):
    for fromStr, toStr in replace.iteritems():
        string = string.replace(fromStr, toStr)

    return string
