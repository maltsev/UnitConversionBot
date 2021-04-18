import os
import json
import hashlib
import traceback
from chalicelib.modules.parser import parseMessageText, parseExpression, InvalidExpressionException
from chalicelib.modules.converter import convertUnit, IncompatibleCategoriesException
from chalicelib.modules.formatter import formatValueUnit, formatAvailableUnits
from chalicelib.modules.helpers import logger
from chalicelib import units


FEEDBACK_TEXT = """
If you have an issue or just want to say thanks, feel free to contact my master @kirillmaltsev or rate me at https://storebot.me/bot/unitconversionbot
Thank you for chatting with me :-)
""".strip()


CRITICAL_ERROR_MESSAGE = "Sorry, I'm broken :-( My master will fix me as soon as possible."

BOT_NAME = '@UnitConversionBot'


def sendMessage(updateData):
    try:
        messageText = getMessageText(updateData)
        if not messageText:
            return {}

        chatId = getChatId(updateData)
        if not chatId:
            error = 'Chat ID is empty'
            logger.warning(error)
            return {'error': error}

        response = {
            'method': 'sendMessage',
            'chat_id': chatId,
            'disable_web_page_preview': True,
            'disable_notification': True
        }

        messageParts = parseMessageText(messageText)
        expression = messageParts['expression']
        command = messageParts['command']

        if command == 'convert' or not command:
            if expression:
                response['text'] = command_convert(expression)
            else:
                response['text'] = command_shortHelp()
        elif command == 'start':
            response['text'] = command_start()
        elif command == 'help':
            response['text'] = command_help(expression)
            response['parse_mode'] = 'Markdown'
        else:
            response['text'] = command_notFound()
    except Exception as error:
        logger.critical(error)
        response['text'] = CRITICAL_ERROR_MESSAGE
        if os.environ.get('DEBUG'):
            traceback.print_exc()

    return response


def answerInlineQuery(updateData):
    inlineQuery = updateData.get('inline_query')
    if not inlineQuery:
        return {}

    inlineQueryId = inlineQuery.get('id')
    if not inlineQueryId:
        return {}

    response = {
        'method': 'answerInlineQuery',
        'inline_query_id': inlineQueryId,
        'cache_time': 60*60*12,
        'is_personal': False,
        'results': []
    }

    try:
        messageText = inlineQuery.get('query', '').strip()
        if not messageText:
            response['results'] = getInlineResult({
                'title': '10 ft to m',
                'message_text': '10 ft = 3.048 m',
                'description': 'Please type a convert expression (e.g., "10 ft to m").'
            })
            return response

        expression = parseMessageText(messageText)['expression']
        response['results'] = getInlineResult(command_convertInline(expression))
    except Exception as error:
        logger.critical(error)
        response['results'] = getInlineResult({
            'title': 'Error',
            'message_text': BOT_NAME,
            'description': CRITICAL_ERROR_MESSAGE
        })
        if os.environ.get('DEBUG'):
            traceback.print_exc()

    return response


def getInlineResult(inlineResultArticle):
    inlineResultArticle['type'] = 'article'
    inlineResultArticle['id'] = hashlib.md5(inlineResultArticle['title'].encode('utf-8')).hexdigest()
    return json.dumps([inlineResultArticle], sort_keys=True)


def command_notFound():
    return "Sorry, I don't understand your command."


def command_start():
    startInfo = """Hi!

My name is @UnitConversionBot. I can convert from one unit to another.
Just type something like "100 ft to m" (in private chat with me) or "/convert 1 km2 to m2" (in group chats). For more info type /help"""

    startInfo += "\n\n" + FEEDBACK_TEXT

    return startInfo.strip()


def command_shortHelp():
    return 'Please type something like "/convert 100 ft to m"'


def command_help(unitsCategoryName):
    if unitsCategoryName:
        return command_listAvailableUnits(unitsCategoryName)
    else:
        return command_defaultHelp()


def command_defaultHelp():
    helpInfo = """
The bot supports following unit categories:
- length (ft to m)
- area (m² to acre)
- volume (litre to pint)
- currencies ($ to €)
- mass (g to lb)
- speed (km/h to mph)
- time (min to ms)
- temperature (°C to °F)
- density (kg/m³ to g/cm³)
- information (MB to Kbit)
- pressure (atm to Pa)
- fuel consumption (mpg to km/l)
- power (horsepower to kW)
- torque (N-m to lbf-ft)

To get all available units of specific category type "/help #category#" ("/help length", for example).

While asking me a question tet-a-tet you can omit a command. Just type:
- 100 $ to €
- 1 sq foot to m2
- 1 year to hours

While asking me a question in a group please add the command "convert" (if I'm a group member too) or my username "UnitConversionBot":
- /convert 10 yr to mon
- @UnitConversionBot 1 ms to second

You can also ask me without adding me to the chat. Just type '@UnitConversionBot 100 ft to m' when you need my help.

You can use both short (`m2`) and full unit names (square meter).\n\n\n"""

    helpInfo += FEEDBACK_TEXT

    return helpInfo.strip()


def command_listAvailableUnits(unitsCategoryName):
    categoriesIndex = units.getCategoriesIndex()
    if unitsCategoryName not in categoriesIndex:
        return f"Sorry, the unit category '{unitsCategoryName}' is not available. Please type /help to get all unit categories"

    helpInfo = f'*The full list of {unitsCategoryName} units:*\n'
    categoryUnits = categoriesIndex[unitsCategoryName]
    if unitsCategoryName != 'information':
        return helpInfo + formatAvailableUnits(categoryUnits)

    # List bits first, then bytes
    bitUnits = {unitKey: unit for unitKey, unit in categoryUnits.items() if 'BIT' in unit['key']}
    helpInfo += formatAvailableUnits(bitUnits)

    byteUnits = {unitKey: unit for unitKey, unit in categoryUnits.items() if 'BYTE' in unit['key']}
    helpInfo += '\n\n' + formatAvailableUnits(byteUnits)

    return helpInfo


def command_convert(expression):
    log = convert(expression)
    responseMessage = log['response']
    if log['type'] != 'success':
        del log['response']

    if 'fullResponse' in log:
        del log['fullResponse']

    logger.info(log)
    return responseMessage


def command_convertInline(expression):
    log = convert(expression)

    if log['type'] == 'success':
        response = {
            'title': log['response'],
            'message_text': log['fullResponse']
        }
    else:
        response = {
            'title': 'Error',
            'message_text': BOT_NAME,
            'description': log['response']
        }

    logger.info(log)
    return response


def convert(expression):
    try:
        unitsIndex = units.getIndex()
        expressionUnits = parseExpression(expression, unitsIndex)
        toValueUnit = convertUnit(expressionUnits['fromValueUnit'], expressionUnits['toUnit'])
        responseMessage = formatValueUnit(toValueUnit)
        responseType = 'success'
    except (IncompatibleCategoriesException, InvalidExpressionException) as error:
        responseMessage = str(error)
        responseType = error.__class__.__name__
    except Exception:
        responseMessage = InvalidExpressionException.defaultErrorMessage
        responseType = InvalidExpressionException.__name__
        if os.environ.get('DEBUG'):
            traceback.print_exc()

    log = {
        'command': 'convert',
        'type': responseType,
        'expression': expression,
        'response': responseMessage
    }

    if responseType == 'success':
        log['fullResponse'] = '{} = {}'.format(formatValueUnit(expressionUnits['fromValueUnit']), formatValueUnit(toValueUnit))

    return log


def getChatId(updateData):
    message = updateData.get('message')
    if not message:
        return None

    chat = message.get('chat')
    if not chat:
        return None

    return chat.get('id')


def getMessageText(updateData):
    message = updateData.get('message')
    if not message:
        return None

    return message.get('text', '').strip()
