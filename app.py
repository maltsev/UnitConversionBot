# -*- coding: utf-8 -*-
import webapp2
from controller.WebHook import WebHook

app = webapp2.WSGIApplication([
    ('/api/webhook', WebHook),
], debug=True)
