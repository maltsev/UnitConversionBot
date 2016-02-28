import webapp2
import controller

app = webapp2.WSGIApplication([
    ('/api/webhook', controller.WebHook),
], debug=True)
