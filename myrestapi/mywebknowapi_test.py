"""
Rest-ful webservice API test cases
Author: Syed Saif ur Rahman
"""
import unittest
import pymongo
import ssl

class mywebknowapi_test(unittest.TestCase):
    #Is local database available?
    def test_mongodb_con_local(self):
        connection = pymongo.MongoClient(
            'localhost',    #Must make it to read from config file
            27017           #Must configure it to read from config file
        )
        self.assertTrue(connection is not None)
        db = connection['mywebknow']
        collection = db['articles1']
        connection.close()

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
        connection.close()

if __name__ == '__main__':
    unittest.main()