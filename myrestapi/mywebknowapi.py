"""
Rest-ful webservice to make accessible API through Amazon EC2
Author: Syed Saif ur Rahman
"""
from flask import Flask, jsonify
import pymongo
import re
import ssl

app = Flask(__name__)

@app.route("/")
def welcomepage():
    return "Welcome to our web API"

@app.route('/all', methods=['GET'])
def alldata():
    connection = pymongo.MongoClient(
        'localhost',
        27017
    )
    db = connection['mywebknow']
    collection = db['articles']
    docs = collection.find({}, {'_id': False})
    connection.close()
    items = []
    for doc in docs:
        items.append(doc)
        #print(">>>"),
        #items['_id'] = str(items['_id'])
        #print("<<<")
    return jsonify(items)


@app.route('/find/<value>', methods=['GET'])
def finddata(value):
    connection = pymongo.MongoClient(
        'localhost',
        27017
    )
    db = connection['mywebknow']
    collection = db['articles']
    regx = re.compile("[\w]*"+value+"[\w]*", re.IGNORECASE)
    docs = collection.find({'abody': regx}, {'_id': False})
    connection.close()
    items = []
    print ("You passed:" + value)
    for doc in docs:
        items.append(doc)
        #print(">>>"),
        #items['_id'] = str(items['_id'])
        #print("<<<")
    return jsonify(items)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)