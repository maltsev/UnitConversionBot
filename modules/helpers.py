# -*- coding: utf-8 -*-

def generateCompositeNames(firstUnitNames, lastUnitNames, shortName = None):
    """Generate composite names using "per" and "/"
    (e.g., km/h, kilometers per hour)
    """
    if not shortName:
        shortName = firstUnitNames[0] + '/' + lastUnitNames[0] # e.g., kg/m³

    fullName = firstUnitNames[1] + ' per ' + lastUnitNames[1] # e.g., kilogram per cubic meter

    names = [
        shortName,
        fullName,
    ]

    for firstUnitName in firstUnitNames:
        for lastUnitName in lastUnitNames:
            newFullName = firstUnitName + ' per ' + lastUnitName

            if newFullName not in names:
                names.append(newFullName)

            newShortName = firstUnitName + '/' + lastUnitName
            if ' ' not in newShortName and newShortName not in names:
                names.append(newShortName)

    return names
