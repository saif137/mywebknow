"""
Rest-ful webservice API test cases
Author: Syed Saif ur Rahman
"""
import unittest
import pymongo
import ssl
import urllib2

class mywebknowapi_test(unittest.TestCase):

    #Commented as final version was required on cloud based mongdb on compose
    # #Is local database available?
    # def test_mongodb_con_local(self):
    #     connection = pymongo.MongoClient(
    #         'localhost',    #Must make it to read from config file
    #         27017           #Must configure it to read from config file
    #     )
    #     db = connection['mywebknow']
    #     collection = db['articles']
    #     count = collection.count()

    # Is cloud mongodb at compose database available?
    def test_mongodb_con_cloud_compose(self):
        uri = 'mongodb://myuser:mypass@sl-aus-syd-1-portal.2.dblayer.com:15439/admin?ssl=true'
        connection = pymongo.MongoClient(
            uri
            , ssl_cert_reqs = ssl.CERT_NONE
        )
        self.assertTrue (connection is not None)
        db = connection['mywebknow']
        collection = db['articles']
        count = collection.count()

    #IS API Webserver up and running
    def test_server_is_up_and_running(self):
        response = urllib2.urlopen('http://localhost:5000')
        self.assertEqual(response.code, 200)

if __name__ == '__main__':
    unittest.main()