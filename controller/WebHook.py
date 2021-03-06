# -*- coding: utf-8 -*-
import os
import json
import hashlib
import webapp2
import logging
import traceback
from modules.parser import parseMessageText, parseExpression, InvalidExpressionException
from modules.converter import convertUnit, IncompatibleCategoriesException
from modules.formatter import formatValueUnit, formatAvailableUnits
from model import Rates
import units


FEEDBACK_TEXT = """
If you have an issue or just want to say thanks, feel free to contact my master @kirillmaltsev or rate me at https://storebot.me/bot/unitconversionbot
Thank you for chatting with me :-)
""".strip()


CRITICAL_ERROR_MESSAGE = "Sorry, I'm broken :-( My master will fix me as soon as possible."

BOT_NAME = '@UnitConversionBot'


class WebHook(webapp2.RequestHandler):
    def post(self):
        logging.debug(self.request.body)

        try:
            updateData = json.loads(self.request.body)
        except ValueError as error:
            logging.warning(error)
            return self.output({})

        if 'message' in updateData:
            response = self.sendMessage(updateData)
        elif 'inline_query' in updateData:
            response = self.answerInlineQuery(updateData)
        else:
            response = {}

        logging.debug(response)
        self.output(response)




    def sendMessage(self, updateData):
        try:
            messageText = self.getMessageText(updateData)
            if not messageText:
                return {}

            chatId = self.getChatId(updateData)
            if not chatId:
                error = 'Chat ID is empty'
                logging.warning(error)
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
                    response['text'] = self.command_convert(expression)
                else:
                    response['text'] = self.command_shortHelp()
            elif command == 'start':
                response['text'] = self.command_start()
            elif command == 'help':
                response['text'] = self.command_help(expression)
                response['parse_mode'] = 'Markdown'
            else:
                response['text'] = self.command_notFound()
        except Exception as error:
            logging.critical(error)
            response['text'] = CRITICAL_ERROR_MESSAGE
            if os.environ.get('DEBUG'):
                traceback.print_exc()

        return response




    def answerInlineQuery(self, updateData):
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
                response['results'] = self.getInlineResult({
                    'title': '10 ft to m',
                    'message_text': '10 ft = 3.048 m',
                    'description': 'Please type a convert expression (e.g., "10 ft to m").'
                })
                return response

            expression = parseMessageText(messageText)['expression']
            response['results'] = self.getInlineResult(self.command_convertInline(expression))
        except Exception as error:
            logging.critical(error)
            response['results'] = self.getInlineResult({
                'title': 'Error',
                'message_text': BOT_NAME,
                'description': CRITICAL_ERROR_MESSAGE
            })
            if os.environ.get('DEBUG'):
                traceback.print_exc()

        return response




    def getInlineResult(self, inlineResultArticle):
        inlineResultArticle['type'] = 'article'
        inlineResultArticle['id'] = hashlib.md5(inlineResultArticle['title'].encode('utf-8')).hexdigest()
        return json.dumps([inlineResultArticle], sort_keys=True)




    def command_notFound(self):
        return "Sorry, I don't understand your command."




    def command_start(self):
        startInfo = """Hi!

My name is @UnitConversionBot. I can convert from one unit to another. Just type something like "100 ft to m" (in private chat with me) or "/convert 1 km2 to m2" (in group chats). For more info type /help"""

        startInfo += "\n\n" + FEEDBACK_TEXT

        return startInfo.strip()




    def command_shortHelp(self):
        return 'Please type something like "/convert 100 ft to m"'




    def command_help(self, unitsCategoryName):
        if unitsCategoryName:
            return self.command_listAvailableUnits(unitsCategoryName)
        else:
            return self.command_defaultHelp()




    def command_defaultHelp(self):
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




    def command_listAvailableUnits(self, unitsCategoryName):
        categoriesIndex = units.getCategoriesIndex(True, stubExchangeRate=True)
        if unitsCategoryName not in categoriesIndex:
            return "Sorry, the unit category '{}' is not available. Please type /help to get all unit categories".format(unitsCategoryName)

        helpInfo = u'*The full list of {} units:*\n'.format(unitsCategoryName)
        categoryUnits = categoriesIndex[unitsCategoryName]
        if unitsCategoryName != 'information':
            return helpInfo + formatAvailableUnits(categoryUnits)

        # List bits first, then bytes
        bitUnits = {unitKey: unit for unitKey, unit in categoryUnits.iteritems() if 'BIT' in unit['key']}
        helpInfo += formatAvailableUnits(bitUnits)

        byteUnits = {unitKey: unit for unitKey, unit in categoryUnits.iteritems() if 'BYTE' in unit['key']}
        helpInfo += '\n\n' + formatAvailableUnits(byteUnits)

        return helpInfo




    def command_convert(self, expression):
        log = self.convert(expression)
        responseMessage = log['response']
        if log['type'] != 'success':
            del log['response']

        if 'fullResponse' in log:
            del log['fullResponse']

        logging.info(log)
        return responseMessage




    def command_convertInline(self, expression):
        log = self.convert(expression)

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

        logging.info(log)
        return response




    def convert(self, expression):
        try:
            currenciesExchangeRates = {}
            ratesModels = Rates.query().order(-Rates.date).fetch(1)
            if len(ratesModels) > 0:
                currenciesExchangeRates = ratesModels[0].content.get('rates', {})

            unitsIndex = units.getIndex(True, currenciesExchangeRates=currenciesExchangeRates)
            expressionUnits = parseExpression(expression, unitsIndex)
            toValueUnit = convertUnit(expressionUnits['fromValueUnit'], expressionUnits['toUnit'])
            responseMessage = formatValueUnit(toValueUnit)
            responseType = 'success'
        except (IncompatibleCategoriesException, InvalidExpressionException) as error:
            responseMessage = unicode(error)
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
            log['fullResponse'] = u'{} = {}'.format(formatValueUnit(expressionUnits['fromValueUnit']), formatValueUnit(toValueUnit))

        return log





    def output(self, data, code=200):
        self.response.headers['Content-Type'] = 'application/json'
        self.response.write(json.dumps(data))
        self.response.status = code




    def getChatId(self, updateData):
        message = updateData.get('message')
        if not message:
            return None

        chat = message.get('chat')
        if not chat:
            return None

        return chat.get('id')




    def getMessageText(self, updateData):
        message = updateData.get('message')
        if not message:
            return None

        return message.get('text', '').strip()
