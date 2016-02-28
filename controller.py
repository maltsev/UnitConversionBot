import sys
import json
import webapp2
from modules.parser import parseMessageText
from model.expression import Expression


class WebHook(webapp2.RequestHandler):
    def post(self):
        try:
            updateData = json.loads(self.request.body)
        except ValueError:
            updateData = {}

        chatId = self.getChatId(updateData)
        if not chatId:
            return self.output({'error': 'Chat ID is empty'}, 400)

        messageText = self.getMessageText(updateData)
        if not messageText:
            return self.output({'error': 'Message ID is empty'}, 400)

        (rawExpression, command) = parseMessageText(messageText)
        if command is 'start':
            responseText = self.command_start()
        else:
            responseText = self.command_convert(rawExpression)

        self.output({'chat_id': chatId, 'text': responseText, 'disable_notification': True})



    def command_start(self):
        return 'Hello, my friend!'

    def command_convert(self, rawExpression):
        expression = Expression(rawExpression)
        if not expression.isValid():
            return 'Expression is not valid'

        ONE_METER = 3.28084

        fromUnit = expression.getFromUnit()
        if fromUnit['name'] == 'm':
            return '{:.2f} ft'.format(fromUnit['value'] * ONE_METER)
        else:
            return '{:.2f} m'.format(fromUnit['value'] / ONE_METER)




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
