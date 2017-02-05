# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
import ssl

from scrapy.conf import settings
from scrapy.exceptions import CloseSpider, DropItem

#This is the default pipeline, we overridden this one with the one for use of MongDB
class MywebknowPipeline(object):
    def process_item(self, item, spider):
        return item
"""
This pipeline is in use. We increased its priority in settings.py : set through ITEM_PIPELINES
"""
class MongoDBPipeline(object):

    connection = None
    def open_spider(self, spider):

        #Connecting to mongodb instance at componse
        # uri = 'mongodb://myuser:mypass@sl-aus-syd-1-portal.2.dblayer.com:15439/admin?ssl=true' #URI for compose mongodb connection
        # connection = pymongo.MongoClient(uri, ssl_cert_reqs = ssl.CERT_NONE) #Connecting to compose mongodb

        #Connecting to local mongodb intance
        self.connection = pymongo.MongoClient(
            settings['MONGODB_SERVER'], #Server ip
            settings['MONGODB_PORT']    #Server port
        )
        db = self.connection[settings['MONGODB_DB']] #Creating the connection
        self.collection = db[settings['MONGODB_COLLECTION']] #Getting the collection
        try:
            self.collection.drop() #Droping the collection, we currently have limited cloud resources, to be improved
        except:
            raise CloseSpider('Problem with MongDB connectivity')

    def close_spider(self, spider):
        #Do something that needs to be done while closing spider
        pass

    def process_item(self, item, spider):
        valid = True
        for data in item:
            if not data:
                valid = False
                #To stop processing of item
                raise DropItem("Missing {0}!".format(data))
        if valid:
            #Inserting data into MongoDB
            self.collection.insert(dict(item))
        #Data is also written on local directory output for development debugging
        return item