import scrapy
from scrapy.selector import Selector
from mywebknow.items import MywebknowItem

class au_com_theguardian_spider(scrapy.Spider):
    #Name of the spider
    name = "theguardian.com/au"

    def __init__ (self, arg1=None, *args, **kwargs):
        super(au_com_theguardian_spider,self).__init__(*args, **kwargs);

    def start_requests(self):
        #URLs to be traversed
        urls = [
            'http://www.theguardian.com/au'
        ]
        #Traverse each URL one by one
        for url in urls:
            yield scrapy.Request(url = url, callback=self.parse)

    #Extracting articles links from headlines
    def parse(self, response):
        #Create the selector
        sel = Selector(response)
        #We are detecting the content according to their CSS class. This will select all articles highlights
        alltitles = sel.xpath('//a[contains(@class,"u-faux-block-link__overlay js-headline-text")]')
        #print(alltitles)
        items = []
        for index, link in enumerate(alltitles):
            #Extract the URL of each article on main page
            url = link.xpath("@href").extract()
            if url <> "" :
                #Call each article url for scraping
                yield scrapy.Request(str(url[0]), callback=self.parsearticle)

    #Extracting articles
    def parsearticle(self, response):
        #This method will be called while scraping each article
        sel = Selector(response)
        #Check for artcile tag
        article = sel.xpath('//article')
        #print(article)
        items = []
        for index, data in enumerate(article):
            #Extract the headline
            ahead = data.xpath('//h1[contains(@class,"content__headline js-score")]/text()').extract()
            #print(ahead)
            #Extract the name of the author
            author = data.xpath('//span[contains(@itemprop,"name")]/text()').extract()
            #print(author)
            #Extract the body of each article, this will need to be futher cleansed
            abody = data.xpath('//div[contains(@class,"content__article-body from-content-api js-article__body")]/p/text()').extract()
            #print(abody)
            #Article date and time information
            adt = data.xpath('//time/@datetime').extract()
            print("-->adt<--"+str(adt))
            #Article stand first information
            asfi = data.xpath('//div[contains(@class,"content__standfirst")]/p/text()').extract()
            print("-->asfi<--"+str(asfi))
            #Article label
            albl = data.xpath('//a[contains(@class,"content__section-label__link")]/text()').extract()
            print("-->albl<--"+str(albl))

            #Put the content in pipeline to get it stored in mongodb
            yield{
                'url': response.url,
                'ahead':ahead,
                'author':author,
                'abody': abody,
                'adt': adt,
                'asfi': asfi,
                'albl': albl
            }
        #return items