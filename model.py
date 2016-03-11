from google.appengine.ext import ndb


class Rates(ndb.Model):
    content = ndb.JsonProperty()
    date = ndb.DateTimeProperty(auto_now_add=True)
