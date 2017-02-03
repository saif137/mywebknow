import scrapy
from scrapy.selector import Selector
from mywebknow.items import MywebknowItem

class au_com_theguardian_spider(scrapy.Spider):
    name = "thequardian.com/au"

    def __init__ (self, arg1=None, *args, **kwargs):
        super(au_com_theguardian_spider,self).__init__(*args, **kwargs);
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>...This is my spider constructor")

    def start_requests(self):
        urls = [
            'http://www.theguardian.com/au'
        ]
        for url in urls:
            yield scrapy.Request(url = url, callback=self.parse)

    #Extracting articles links from headlines
    def parse(self, response):
        mymercuryurl = "x-api-key: ySWFGa76Iutwf1HyaRSLgeb5OWYi7ECJHxQzaxFV\" \"https://mercury.postlight.com/parser?url=" + response.url
        print("\n\n\n>>>>>")
        sel = Selector(response)
        alltitles = sel.xpath('//a[contains(@class,"u-faux-block-link__overlay js-headline-text")]')
        print(alltitles)
        items = []
        for index, link in enumerate(alltitles):
            # item = MywebknowItem()
            # item["title"] = link.xpath("./text()").extract()
            # item["url"] = link.xpath("@href").extract()
            # print(str(item["url"][0]))
            # items.append(item)
            url = link.xpath("@href").extract()
            yield{
                'title':link.xpath("./text()").extract(),
                'url':url
            }
            yield scrapy.Request(str(url[0]), callback=self.parsearticle)
        print("<<<<<\n\n\n")
        #return items

    #Extracting articles
    def parsearticle(self, response):
        print("\n\n\n$$$$$")
        sel = Selector(response)
        #Article heading
        article = sel.xpath('//article')
        print(article)
        items = []
        for index, data in enumerate(article):
            ahead = data.xpath('//h1[contains(@class,"content__headline js-score")]/text()').extract()
            print(ahead)
            author = data.xpath('//span[contains(@itemprop,"name")]/text()').extract()
            print(author)
            abody = data.xpath('//div[contains(@class,"content__article-body from-content-api js-article__body")]/p/text()').extract()
            print(abody)
            yield{
                'ahead':ahead,
                'author':author,
                'abody': abody
            }
        print("$$$$$\n\n\n")
        #return items
