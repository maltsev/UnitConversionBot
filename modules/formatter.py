# -*- coding: utf-8 -*-
def formatValueUnit(valueUnit):
    strValue = u'{:,.3f}'.format(valueUnit['value']).rstrip('0').rstrip('.')
    strUnit = valueUnit['unit']['shortName']

    return strValue + ' ' + strUnit




def formatAvailableUnits(unitsIndex):
    unitsByCategories = {}
    for unit in unitsIndex.values():
        unitCategory = unit['category']
        if unitCategory not in unitsByCategories:
            unitsByCategories[unitCategory] = {
                'category': unit['category'],
                'units': {}
            }

        unitsByCategories[unitCategory]['units'][unit['baseName']] = unit

    unitsList = u'*Full list of available units:*\n'
    for categoryUnits in unitsByCategories.values():
        unitsList += u'*{}*\n'.format(categoryUnits['category'].capitalize())

        units = categoryUnits['units'].values()
        if categoryUnits['category'] == 'currencies':
            units.sort(key=lambda x: x['baseName'])
        else:
            units.sort(key=lambda x: x['value'])

        for unit in units:
            safeShortName = unit['shortName'].replace(u'µ', 'u').replace(u'²', '2').replace(u'³', '3')
            unitsList += u'- {} `{}`\n'.format(unit['baseName'], safeShortName)

        unitsList += '\n'

    return unitsList.strip()
