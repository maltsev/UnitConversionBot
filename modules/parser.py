import re


def parseRawExpression(rawExpression):
    if rawExpression.find(' to ') is -1:
        return [None, None]

    (fromRawUnit, toRawUnit) = rawExpression.split(' to ')
    fromUnit = parseRawFromUnit(fromRawUnit)
    toUnit = parseRawToUnit(toRawUnit)

    return (fromUnit, toUnit)



def parseRawFromUnit(rawFromUnit):
    (value, name) = rawFromUnit.split(' ')
    return {
        'value': int(value),
        'name': name.strip()
    }


def parseRawToUnit(rawToUnit):
    return {
        'value': None,
        'name': rawToUnit.strip()
    }


def parseMessageText(messageText):
    parts = re.split('/(\w+) ', messageText)
    if len(parts) is 1:
        rawExpression = messageText.strip()
        return (rawExpression, None)
    else:
        command = parts[1].strip()
        rawExpression = parts[2].strip()
        return (rawExpression, command)
