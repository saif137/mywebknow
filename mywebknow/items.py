# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field

class MywebknowItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #atext = Field()
    #author = Field()
    #headline = Field()
    title = Field()
    url = Field()
    #pass


class ArticleItem(scrapy.Item):
    ahead = Field()
    autho = Field()
    abody = Field()
    #pass
