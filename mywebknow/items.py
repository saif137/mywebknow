"""
This file identifying the fields that we want to persist
"""
import scrapy
from scrapy.item import Item, Field

class MywebknowItem(scrapy.Item):
    #Holds the title of the artile, however, it got redundant after finding the heading
    title = Field()
    #Holds the url of the article
    url = Field()
    #Holds the heading of the articles
    ahead = Field()
    #Name of the author of the article
    author = Field()
    #Body of the article
    abody = Field()
    # Article date and time information
    adt = Field()
    # Article stand first information
    asfi = Field()
    # Article label
    albl = Field()
    #pass