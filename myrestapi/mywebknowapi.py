"""
Rest-ful webservice to make accessible API through Amazon EC2
Author: Syed Saif ur Rahman
"""
from flask import Flask, jsonify, render_template #For my REST API
import pymongo #For MongoDB
import re #For Regular expression used in search matching records
import ssl #For ssl based connectivity with cloud mongodb
#For logging whats happening
import logging
from logging.handlers import RotatingFileHandler

app = Flask(__name__)

"""
My API
"""

#Call to welcome page
@app.route("/")
def welcomepage():
    mymsg = [{'message': 'Welcome to mywebknow REST API'}]
    return jsonify(mymsg)

#If not value passed return error
@app.route('/find/', methods=['GET'])
@app.route('/findauthor/', methods=['GET'])
@app.route('/findlabel/', methods=['GET'])
@app.route('/finddatetime/', methods=['GET'])
@app.route('/findheadline/', methods=['GET'])
@app.route('/findurl/', methods=['GET'])
@app.route('/findstandfirstinfo/', methods=['GET'])
def errorparam():
    mymsg = [{'error': 'No parameter passed. Please refer to API documentation'}]
    app.logger.error(mymsg)
    return jsonify(mymsg)  # Because API user can parse it

#To fetch all data from mongodb
@app.route('/all', methods=['GET'])
def alldata():
    items = []

    try:
        uri = getdbclienturi()
        # Client to mongodb database
        client = pymongo.MongoClient(uri)
        # Selecting the database
        db = client['mywebknow']
        # Selecting the collection
        collection = db['articles']
        #Removing the ids, as these are internal to our storage and also cause problem with jsonify
        docs = collection.find({}, {'_id': False})

        #Create a list of all data
        for doc in docs:
            items.append(doc)

    except Exception as e:
        mymsg = [{'error': 'Problem fetching data'},{'exception': e.message}]
        app.logger.error(mymsg)
        return jsonify(mymsg)  # Because API user can parse it

    #Return data in json format to caller
    return jsonify(items)

"""
This method will facilitate the search of all data with existence of any keyword
Keyword will be passed as value
"""
@app.route('/find/<value>', methods=['GET'])
def finddata(value):
    items = []

    try:
        uri = getdbclienturi()
        # Client to mongodb database
        client = pymongo.MongoClient(uri)
        # Selecting the database
        db = client['mywebknow']
        # Selecting the collection
        collection = db['articles']
        #Generate the regular expression to fetch any data containing the value anywhere
        regx = re.compile("[\w]*" + value + "[\w]*", re.IGNORECASE)
        #Fetch the abody data that satisfies the regular expression
        docs = collection.find({'abody': regx}, {'_id': False})

        #Create a list of found articles
        for doc in docs:
            items.append(doc)

    except Exception as e:
        mymsg = [{'error': 'Problem fetching data'},{'exception': e.message}]
        app.logger.error(mymsg)
        return jsonify(mymsg)  # Because API user can parse it

    #Return data in json format to caller
    return jsonify(items)

"""
This method will facilitate the search of all authors articles with existence of keyword
Keyword will be passed as value
"""
@app.route('/findauthor/<author>', methods=['GET'])
def findauthor(author):
    items = []

    try:
        uri = getdbclienturi()
        # Client to mongodb database
        client = pymongo.MongoClient(uri)
        # Selecting the database
        db = client['mywebknow']
        # Selecting the collection
        collection = db['articles']
        #Generate the regular expression to fetch articles written  by any author  with name containing the value anywhere
        regx = re.compile("[\w]*" + author + "[\w]*", re.IGNORECASE)
        #Fetch the author article that satisfies the regular expression
        docs = collection.find({'author': regx}, {'_id': False})

        #Create a list of found articles
        for doc in docs:
            items.append(doc)

    except Exception as e:
        mymsg = [{'error': 'Problem fetching author'},{'exception': e.message}]
        app.logger.error(mymsg)
        return jsonify(mymsg)  # Because API user can parse it

    #Return data in json format to caller
    return jsonify(items)

"""
This method will facilitate the search of all labels with existence of keyword
Keyword will be passed as label
"""
@app.route('/findlabel/<label>', methods=['GET'])
def findlabel(label):
    items = []

    try:
        uri = getdbclienturi()
        # Client to mongodb database
        client = pymongo.MongoClient(uri)
        # Selecting the database
        db = client['mywebknow']
        # Selecting the collection
        collection = db['articles']
        #Generate the regular expression to fetch any arcticle with label containing the value
        regx = re.compile("[\w]*" + label + "[\w]*", re.IGNORECASE)
        #Fetch the label that satisfies the regular expression
        docs = collection.find({'albl': regx}, {'_id': False})

        #Create a list of found articles
        for doc in docs:
            items.append(doc)

    except Exception as e:
        mymsg = [{'error': 'Problem fetching articles with label'},{'exception': e.message}]
        app.logger.error(mymsg)
        return jsonify(mymsg)  # Because API user can parse it

    #Return data in json format to caller
    return jsonify(items)

"""
This method will facilitate the search of all articles containing date time part passed
Keyword will be passed as datetimepart
"""
@app.route('/finddatetime/<datetimepart>', methods=['GET'])
def finddatetime(datetimepart):
    items = []

    try:
        uri = getdbclienturi()
        # Client to mongodb database
        client = pymongo.MongoClient(uri)
        # Selecting the database
        db = client['mywebknow']
        # Selecting the collection
        collection = db['articles']
        #Generate the regular expression to fetch any arcticle with given date time part
        regx = re.compile("[\w]*" + datetimepart + "[\w]*", re.IGNORECASE)
        #Fetch the articles that satisfies the regular expression
        docs = collection.find({'adt': regx}, {'_id': False})

        #Create a list of found articles
        for doc in docs:
            items.append(doc)

    except Exception as e:
        mymsg = [{'error': 'Problem fetching article with date time part'},{'exception': e.message}]
        app.logger.error(mymsg)
        return jsonify(mymsg)  # Because API user can parse it

    #Return data in json format to caller
    return jsonify(items)

"""
This method will facilitate the search of all articles containing parameter in headline
Keyword will be passed as headline
"""
@app.route('/findheadline/<headline>', methods=['GET'])
def findheadline(headline):
    items = []

    try:
        uri = getdbclienturi()
        # Client to mongodb database
        client = pymongo.MongoClient(uri)
        # Selecting the database
        db = client['mywebknow']
        # Selecting the collection
        collection = db['articles']
        #Generate the regular expression to fetch any arcticle with given value in headline
        regx = re.compile("[\w]*" + headline + "[\w]*", re.IGNORECASE)
        #Fetch the articles that satisfies the regular expression
        docs = collection.find({'ahead': regx}, {'_id': False})

        #Create a list of found articles
        for doc in docs:
            items.append(doc)

    except Exception as e:
        mymsg = [{'error': 'Problem fetching article with headline part'},{'exception': e.message}]
        app.logger.error(mymsg)
        return jsonify(mymsg)  # Because API user can parse it

    #Return data in json format to caller
    return jsonify(items)

"""
This method will facilitate the search of all articles containing parameter in url
Keyword will be passed as url
"""
@app.route('/findurl/<url>', methods=['GET'])
def findurl(url):
    items = []

    try:
        uri = getdbclienturi()
        # Client to mongodb database
        client = pymongo.MongoClient(uri)
        # Selecting the database
        db = client['mywebknow']
        # Selecting the collection
        collection = db['articles']
        #Generate the regular expression to fetch any arcticle with given value in headline
        regx = re.compile("[\w]*" + url + "[\w]*", re.IGNORECASE)
        #Fetch the articles that satisfies the regular expression
        docs = collection.find({'url': regx}, {'_id': False})

        #Create a list of found articles
        for doc in docs:
            items.append(doc)

    except Exception as e:
        mymsg = [{'error': 'Problem fetching article with url part'},{'exception': e.message}]
        app.logger.error(mymsg)
        return jsonify(mymsg)  # Because API user can parse it

    #Return data in json format to caller
    return jsonify(items)

"""
This method will facilitate the search of all articles containing parameter in stand first information
Keyword will be passed as url
"""
@app.route('/findstandfirstinfo/<sfi>', methods=['GET'])
def findstandfirstinfo(sfi):
    items = []

    try:
        uri = getdbclienturi()
        # Client to mongodb database
        client = pymongo.MongoClient(uri)
        # Selecting the database
        db = client['mywebknow']
        # Selecting the collection
        collection = db['articles']
        #Generate the regular expression to fetch any arcticle with given value in stand first information
        regx = re.compile("[\w]*" + sfi + "[\w]*", re.IGNORECASE)
        #Fetch the articles that satisfies the regular expression
        docs = collection.find({'asfi': regx}, {'_id': False})

        #Create a list of found articles
        for doc in docs:
            items.append(doc)

    except Exception as e:
        mymsg = [{'error': 'Problem fetching article with stand first information part'},{'exception': e.message}]
        app.logger.error(mymsg)
        return jsonify(mymsg)  # Because API user can parse it

    #Return data in json format to caller
    return jsonify(items)

"""
My REST API Error Handlers
"""
@app.errorhandler(404)
def page_not_found(e):
    mymsg = [{'error': 'Page not found'}]
    app.logger.error(mymsg)
    return jsonify(mymsg) #Because API user can parse it

"""
My custom function
"""
def getdbclienturi():
    # URI to local mongodb database
    uri = 'mongodb://localhost:27017'
    #URI to compose mongodb database
    #uri = 'mongodb://myuser:mypass@sl-aus-syd-1-portal.2.dblayer.com:15439/admin?ssl=true'
    return uri

if __name__ == '__main__':
    #Initialize the logging handler
    myloghandler = RotatingFileHandler('mywebknow.log', maxBytes=10000, backupCount=1)
    #Set the logging level
    myloghandler.setLevel(logging.INFO)
    #Add handler to app
    app.logger.addHandler(myloghandler)
    #Run the application, don't forget to make debug = False for deployment
    app.run(host='0.0.0.0', port=5000, debug=True)