import splunk
import requests
import json
import sys
import unittest
from xml.dom import minidom

'''
    This unit test checks:
        * The validity of a sample JSON payload intended to
          be sent to Jive.

    Asserts that necessary default values have been changed
    and for the existence of required keys.

    Set values for SPLUNK_URL, SPLUNK_USERNAME & SPLUNK_PASSWORD
    prior to executing unit tests.
'''
class TestJiveClass(unittest.TestCase):
    SPLUNK_URL = ""
    SPLUNK_USERNAME = ""
    SPLUNK_PASSWORD = ""

    @classmethod
    def setUpClass(cls):
        if cls.SPLUNK_URL is "" or cls.SPLUNK_USERNAME is "" or cls.SPLUNK_PASSWORD is "":
            print >> sys.stdout, "Please set Splunk configuration bits before executing test script."
            sys.exit(1)

        try:
            # loading sample payload JSON
            with open('jive_test.json') as data_file:
                cls.payload = json.load(data_file)
                cls.config = cls.payload.get('configuration')

            # obtaining splunk session key
            result = requests.post(url=cls.SPLUNK_URL + "/services/auth/login", data={'username':cls.SPLUNK_USERNAME, 'password':cls.SPLUNK_PASSWORD}, headers={}, verify=False)
            cls.session_key = minidom.parseString(result.text).getElementsByTagName('sessionKey')[0].childNodes[0].nodeValue
        except Exception, e:
            print >> sys.stderr, "ERROR Unable to parse JSON file.  Error: %s" % e

class TestJivePayload(TestJiveClass):
    @classmethod
    def setUpClass(cls):
        super(TestJivePayload, cls).setUpClass()
    # Begin tests for correct values in the sample JSON payload
    def test_app(self):
        self.assertEqual(self.config.get('jive_url'),"https://xxxx.jiveon.com")

if __name__ == '__main__':
    unittest.main()
