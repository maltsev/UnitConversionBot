# -*- coding: utf-8 -*-
def formatValueUnit(valueUnit):
    strValue = u'{:,.3f}'.format(valueUnit['value']).rstrip('0').rstrip('.')
    strUnit = valueUnit['unit']['shortName']

    return strValue + ' ' + strUnit




def formatAvailableUnits(unitsIndex):
    unitsByTypes = {}
    for unit in unitsIndex.values():
        unitType = unit['type']
        if unitType not in unitsByTypes:
            unitsByTypes[unitType] = {
                'type': unit['type'],
                'units': {}
            }

        unitsByTypes[unitType]['units'][unit['baseName']] = unit

    unitsList = u'*Full list of available units:*\n'
    for typeUnits in unitsByTypes.values():
        unitsList += u'*{}*\n'.format(typeUnits['type'].capitalize())

        units = typeUnits['units'].values()
        if typeUnits['type'] == 'currencies':
            units.sort(key=lambda x: x['baseName'])
        else:
            units.sort(key=lambda x: x['value'])

        for unit in units:
            safeShortName = unit['shortName'].replace(u'µ', 'u').replace(u'²', '2').replace(u'³', '3')
            unitsList += u'- {} `{}`\n'.format(unit['baseName'], safeShortName)

        unitsList += '\n'

    return unitsList.strip()
