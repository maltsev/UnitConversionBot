# -*- coding: utf-8 -*-
import json
import webapp2
import logging
from modules.parser import parseMessageText, parseExpression, InvalidExpressionException, InvalidUnitException
from modules.converter import convertUnit, IncompatibleCategoriesException
from modules.formatter import formatValueUnit, formatAvailableUnits
import units


FEEDBACK_TEXT = """
If you have an issue or just want to say thanks, feel free to contact my master @kirillmaltsev
Thank you for chatting with me :-)
""".strip()


class WebHook(webapp2.RequestHandler):
    def post(self):
        chatId = 0
        requestBody = self.request.body

        try:
            logging.debug(requestBody)
            updateData = json.loads(requestBody)
        except ValueError as error:
            logging.warning(error)
            return self.output({})

        try:
            messageText = self.getMessageText(updateData)
            if not messageText:
                return self.output({})

            chatId = self.getChatId(updateData)
            if not chatId:
                error = 'Chat ID is empty'
                logging.warning(error)
                return self.output({'error': error})

            response = {
                'method': 'sendMessage',
                'chat_id': chatId,
                'disable_notification': True
            }

            messageParts = parseMessageText(messageText)
            expression = messageParts['expression']
            command = messageParts['command']

            if command == 'convert' or not command:
                if expression:
                    responseText = self.command_convert(expression)
                else:
                    responseText = self.command_shortHelp()
            elif command == 'start':
                responseText = self.command_start()
            elif command == 'help':
                responseText = self.command_help()
                response['parse_mode'] = 'Markdown'
            else:
                responseText = self.command_notFound()
        except Exception as error:
            logging.critical(error)
            responseText = "Sorry, I'm broken :-( My master will fix me as soon as possible."

        if not chatId:
            self.output({})

        logging.debug(responseText)
        response['text'] = responseText
        self.output(response)




    def command_notFound(self):
        return "Sorry, I don't understand your command."




    def command_start(self):
        startInfo = """Hi!

My name is @UnitConversionBot. I can convert from one units to another. Just type something like "100 ft to m" (in private chat with me) or "/convert 1 km2 to m2" (in group chats). For more info type /help"""

        startInfo += "\n\n" + FEEDBACK_TEXT

        return startInfo.strip()




    def command_shortHelp(self):
        return 'Please type something like "/convert 100 ft to m"'




    def command_help(self):
        helpInfo = formatAvailableUnits(units.index)

        helpInfo += u"""\n\n
While asking me a question tet-a-tet you can omit a command. Just type:
- 100 $ to €
- 1 sq foot to m2
- 1 year to hours

While asking me a question in a group please add the command "convert" (if I'm a group member too) or my username "UserConversionBot":
- /convert 10 yr to mon
- @UserConversionBot 1 ms to second

You can use both short (`m2`) and full unit names (square meter).\n\n\n"""

        helpInfo += FEEDBACK_TEXT

        return helpInfo.strip()




    def command_convert(self, expression):
        try:
            units = parseExpression(expression)
            toValueUnit = convertUnit(units['fromValueUnit'], units['toUnit'])
            responseMessage = formatValueUnit(toValueUnit)
            responseType = 'success'
        except IncompatibleCategoriesException as error:
            responseMessage = error.args[0]
            responseType = 'incompatibleCategoriesError'
        except InvalidUnitException as error:
            responseMessage = error.args[0]
            responseType = 'invalidUnitError'
        except InvalidExpressionException as error:
            responseMessage = error.args[0]
            responseType = 'invalidExpressionError'
        except Exception:
            responseMessage = InvalidExpressionException.defaultErrorMessage
            responseType = 'invalidExpressionError'

        log = {
            'command': 'convert',
            'type': responseType,
            'expression': expression
        }

        if responseType == 'success':
            log['response'] = responseMessage

        logging.info(log)
        return responseMessage




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
