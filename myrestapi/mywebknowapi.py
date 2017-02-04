"""
Rest-ful webservice to make accessible API through Amazon EC2
Author: Syed Saif ur Rahman
"""
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return 'yes, its working'

if __name__ == '__main__':
    app.run(debug=True)