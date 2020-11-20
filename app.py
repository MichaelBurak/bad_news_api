from flask import Flask, jsonify, request
from flask_cors import CORS
import requests
import os
from dotenv import load_dotenv
import pymongo
load_dotenv()

KEY = os.getenv('KEY')
MONGO_URL = os.getenv('MONGO_URL')
client = pymongo.MongoClient(MONGO_URL)
db = client["badnews"]
collection = db["articles"]

# initialize Flask application

app = Flask(__name__, static_folder='../client/dist/',    static_url_path='/')


CORS(app, resources={r'/*': {'origins': '*'}})


@app.route("/article", methods=["GET"])
def entry():
    data = collection.find_one(
        sort=[('_id', pymongo.DESCENDING)]
    )['title']
    return jsonify(str(data))


if __name__ == '__main__':
    app.run()
