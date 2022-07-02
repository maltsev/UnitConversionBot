import re
from chalicelib.modules.formatter import massReplace


def parseExpression(expression, unitsIndex):
    expression = normalizeExpression(expression, unitsIndex)
    expressionParts = expression.split(' ')
    if len(expressionParts) < 2:
        raise InvalidExpressionException(InvalidExpressionException.defaultErrorMessage)

    rawFromValue = expressionParts[0]
    try:
        fromValue = float(rawFromValue)
    except ValueError:
        raise InvalidValueException(InvalidValueException.errorMessage.format(rawFromValue))

    if len(rawFromValue) > 14:
        raise InvalidValueException("Sorry, I can't convert such big numbers.")

    rawFromUnit = expressionParts[1]
    fromUnit = getUnit(rawFromUnit, unitsIndex)

    toUnit = fromUnit['defaultToUnit']
    if len(expressionParts) >= 3:
        rawToUnit = expressionParts[-1]
        if rawToUnit not in ['to', '=', 'go']:
            toUnit = getUnit(rawToUnit, unitsIndex)

    return {
        'fromValueUnit': {
            'value': fromValue,
            'unit': fromUnit
        },
        'toUnit': toUnit
    }


def normalizeExpression(expression, unitsIndex):
    expression = expression.lower()
    expression = massReplace(expression, {
        ',': '',
        'convert': '',
        '=': ' = '
    })
    # Add whitespace after number
    expression = re.sub(r'([\./\d]+)(\D)', r'\1 \2', expression)
    expression = re.sub(r'\s+', ' ', expression, 0, re.UNICODE)
    expression = expression.replace('/ ', '/')
    expression = normalizeUnitsInExpression(expression, unitsIndex)
    expression = expression.strip()

    return expression


def normalizeUnitsInExpression(expression, unitsIndex):
    denormalizedUnitNames = list(filter(lambda n: ' ' in n, unitsIndex.keys()))
    denormalizedUnitNames.sort(key=len, reverse=True)

    for denormalizedUnitName in denormalizedUnitNames:
        shortName = unitsIndex[denormalizedUnitName]['shortName']
        expression = expression.replace(denormalizedUnitName, shortName)

    expression = re.sub(r'(fl\.? ?oz\.? ?|oz\.? ?fl\.? ?)', 'fl.oz ', expression)
    # Place a currency sign after the number
    expression = re.sub(r'([$€£¥₽]) ?([\.\d]+)', r'\2 \1', expression)

    return expression


def getUnit(rawUnit, unitsIndex):
    unit = unitsIndex.get(rawUnit)
    if not unit:
        raise InvalidUnitException(InvalidUnitException.errorMessage.format(rawUnit))

    return unit


def parseMessageText(messageText):
    # Take only the first line
    messageText = messageText.split('\n')[0]

    # Remove @mentions
    messageText = re.sub(r'@\w+', '', messageText)

    # Add whitespace in case messageText contains only the command
    parts = re.split(r'^/(\w+) ', messageText + ' ')
    if len(parts) == 1:
        expression = messageText.strip()
        command = ''
    else:
        expression = parts[2].strip()
        command = parts[1].strip()

    expression = expression.strip('\'".')

    return {
        'expression': expression,
        'command': command
    }


class InvalidExpressionException(Exception):
    defaultErrorMessage = "Sorry, I don't understand your question. I'm just a bot :-( Please ask something simple like '100 ft to m'."


class InvalidValueException(InvalidExpressionException):
    errorMessage = "Sorry, I don't understand the number '{}'. Please type it in a more ordinary way, like 100 or 12.5"


class InvalidUnitException(InvalidExpressionException):
    errorMessage = "Sorry, I'm just a stupid bot :-( I don't know what does '{}' mean. But my master probably does. I'd ask him to teach me."
