import json
import logging
import webapp2
from google.appengine.api import urlfetch
from model import Rates
from config import OPENEXHANGERATES_API_KEY


class UpdateRates(webapp2.RequestHandler):
    def get(self):
        try:
            apiUrl = 'https://openexchangerates.org/api/latest.json?app_id=' + OPENEXHANGERATES_API_KEY
            result = urlfetch.fetch(apiUrl)
            if result.status_code != 200:
                raise Exception(result.content)

            response = json.loads(result.content)
            if 'rates' not in response:
                raise Exception(response)

            Rates(content=response).put()
        except Exception as error:
            logging.error(error)
            self.response.status = 500
            return

        self.response.status = 200
