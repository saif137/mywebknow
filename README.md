This project will enable user to scarp content from web and then make is available for search to end-users.

This project make use of MongoDB instance on Compose.

Developed By:
Syed Saif ur Rahman

API:

Welcome message:
http://localhost:5000/

Fetching all documents:
http://localhost:5000/all

Searching article body for a keyword:
http://localhost:5000/find/<keyword>

Searching articles by author name:
http://localhost:5000/findauthor/<keyword>

Searching articles by their labels:
http://localhost:5000/findlabel/<keyword>

Searching articles by their date time parts:
http://localhost:5000/finddatetime/<keyword>

Searching articles by headline content:
http://localhost:5000/findheadline/<keyword>

Searching articles by URL part:
http://localhost:5000/findurl/<keyword>

Searching articles by stand first information content:
http://localhost:5000/findstandfirstinfo/<keyword>

Files with my source code:

items.py -> Holds the field information that we scrap and store

pipelines.py -> Holds the MongoDB pipeline handling source

spiders/au_com_theguardian_spider.py -> Scraper for theguardian.com/au

myrestapi/mywebknowapi.py -> Contains the implementation of REST-ful API

myrestapi/mywebknowapi_test.py -> Contains the implementation of REST-ful API testing

Reference Used:

Scrapy Tutorial: https://doc.scrapy.org/en/latest/intro/tutorial.html

Flask Testing: http://flask.pocoo.org/docs/0.12/testing/

Related Work:

Newspaper: Article scraping & curation http://newspaper.readthedocs.io/en/latest/

approximate and phonetic matching of strings https://pypi.python.org/pypi/jellyfish

ISO country, subdivision, language, currency and script definitions and their translations https://pypi.python.org/pypi/pycountry

Beautiful Soup: Library for screen-scraping https://www.crummy.com/software/BeautifulSoup/

Loading tesing tool http://locust.io/
