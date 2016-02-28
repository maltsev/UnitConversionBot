import sys
sys.path.append('.')
sys.path.append('/Applications/GoogleAppEngineLauncher.app/Contents/Resources/GoogleAppEngine-default.bundle/Contents/Resources/google_appengine/lib/webapp2-2.3')

from webtest import TestApp
import unittest
from app import app


class WebHookTests(unittest.TestCase):
  def test_messageFromUser(self):
      testApp = TestApp(app)

      chatId = 928

      update = {
          'update_id': 1,
          'message': {
              'chat': {
                  'id': chatId
              },
              'text': '1 m to ft'
          }
      }

      response = testApp.post_json('/api/webhook', update)
      self.assertEqual(response.status, '200 OK')
      self.assertEqual(response.content_type, 'application/json')
      self.assertEqual(response.json, {'chat_id': chatId, 'text': '3.28 ft', 'disable_notification': True})


if __name__ == '__main__':
    unittest.main()
