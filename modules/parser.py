# -*- coding: utf-8 -*-
import re
import units


def parseExpression(expression):
    expression = expression.lower()
    if expression.find(' to ') == -1:
        raise InvalidExpressionException("Sorry, I don't understand your question. I'm just a bot :-( Please ask something simple like '100 ft to m'.")

    errorUnits = u''

    rawFromValueUnit, rawToUnit = expression.split(' to ')
    fromValueUnit = parseRawFromValueUnit(rawFromValueUnit)
    if not fromValueUnit:
        errorUnits += u"'{}'".format(rawFromValueUnit)

    toUnit = parseRawToUnit(rawToUnit)
    if not toUnit:
        if errorUnits:
            errorUnits += ' and '
        errorUnits += u"'{}'".format(rawToUnit)

    if errorUnits:
        raise InvalidUnitException(u"Sorry, I'm just a stupid bot :-( I don't know what does {} mean. But my master probably does. I'd ask him to teach me.".format(errorUnits))

    return {
        'fromValueUnit': fromValueUnit,
        'toUnit': toUnit
    }



def parseRawFromValueUnit(rawFromValueUnit):
    if rawFromValueUnit.find(' ') == -1:
        return None

    rawValue, rawUnit = rawFromValueUnit.split(' ')
    unit = parseRawUnit(rawUnit)
    if not unit:
        return None

    rawValue = rawValue.replace(',', '.')
    try:
        value = float(rawValue)
    except:
        return None

    return {
        'value': value,
        'unit': unit
    }



def parseRawToUnit(rawToUnit):
    return parseRawUnit(rawToUnit)


def parseRawUnit(rawUnit):
    rawUnit = rawUnit.strip().lower()
    return units.index.get(rawUnit)


def parseMessageText(messageText):
    # Remove @mentions
    messageText = re.sub('@\w+', '', messageText)

    # Add whitespace in case messageText contains only the command
    parts = re.split('^/(\w+) ', messageText + ' ')
    if len(parts) == 1:
        expression = messageText.strip()
        command = ''
    else:
        expression = parts[2].strip()
        command = parts[1].strip()

    return {
        'expression': expression,
        'command': command
    }



class InvalidExpressionException(Exception):
    pass

class InvalidUnitException(InvalidExpressionException):
    pass
