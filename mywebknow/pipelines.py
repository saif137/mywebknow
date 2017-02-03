# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
import ssl

from scrapy.conf import settings

class MywebknowPipeline(object):
    def process_item(self, item, spider):
        return item

class MongoDBPipeline(object):

    def __init__(self):

        #Connecting to mongodb instance at componse
        # uri = 'mongodb://myuser:mypass@sl-aus-syd-1-portal.2.dblayer.com:15439/admin?ssl=true'
        # connection = pymongo.MongoClient(uri, ssl_cert_reqs = ssl.CERT_NONE)

        #Connecting to local mongodb intance
        connection = pymongo.MongoClient(
            settings['MONGODB_SERVER'],
            settings['MONGODB_PORT']
        )
        db = connection[settings['MONGODB_DB']]
        self.collection = db[settings['MONGODB_COLLECTION']]
        self.collection.drop()

    def process_item(self, item, spider):
        valid = True
        for data in item:
            if not data:
                valid = False
                raise DropItem("Missing {0}!".format(data))
        if valid:
            self.collection.insert(dict(item))
        return item