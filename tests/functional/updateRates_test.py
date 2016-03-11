import json
import unittest
import logging
from google.appengine.ext import ndb
from google.appengine.ext import testbed
from google.appengine.api import apiproxy_stub
from google.appengine.api import apiproxy_stub_map
from testfixtures import log_capture
from webtest import TestApp
from app import app
import model


class UpdateRatesTests(unittest.TestCase):
    url = '/api/rates/update'


    def setUp(self):
        self.testbed = testbed.Testbed()
        self.testbed.activate()
        self.testbed.init_datastore_v3_stub()
        self.testbed.init_memcache_stub()
        ndb.get_context().clear_cache()

        self.urlfetchMock = URLFetchServiceMock()
        apiproxy_stub_map.apiproxy.RegisterStub('urlfetch', self.urlfetchMock)




    def tearDown(self):
        self.testbed.deactivate()



    @log_capture(level=logging.ERROR)
    def test_errorUpdate(self, logs):
        self.urlfetchMock.setReturnValues(content=json.dumps('Some error'), status_code=503)
        response = TestApp(app).get(self.url, status='500 Internal Server Error')
        self.assertEqual(response.status_code, 500)
        logs.check(('root', 'ERROR', '"Some error"'))




    def test_successfulUpdate(self):
        self.urlfetchMock.setReturnValues(content=json.dumps({'rates': {'USD': 1, 'EUR': 2}}))
        response = TestApp(app).get(self.url)
        self.assertEqual(response.status_code, 200)

        rates = model.Rates.query().fetch()
        self.assertEqual(len(rates), 1)
        self.assertEqual(rates[0].content, {'rates': {'USD': 1, 'EUR': 2}})






# Source: http://blog.rebeiro.net/2012/03/mocking-appengines-urlfetch-service-in.html
class URLFetchServiceMock(apiproxy_stub.APIProxyStub):
    """Mock for google.appengine.api.urlfetch."""
    def __init__(self, serviceName='urlfetch'):
        super(URLFetchServiceMock, self).__init__(serviceName)

    def setReturnValues(self, **kwargs):
        self.returnValues = kwargs

    def _Dynamic_Fetch(self, request, response):
        returnValues = self.returnValues
        response.set_content(returnValues.get('content', ''))
        response.set_statuscode(returnValues.get('status_code', 200))
        for headerKey, headerValue in returnValues.get('headers', {}).items():
            newHeader = response.add_header()
            newHeader.set_key(headerKey)
            newHeader.set_value(headerValue)
        response.set_finalurl(returnValues.get('final_url', request.url()))
        response.set_contentwastruncated(returnValues.get('content_was_truncated', False))

        self.request = request
        self.response = response
