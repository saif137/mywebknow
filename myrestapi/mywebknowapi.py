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
Keyworkd will be passed as value
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