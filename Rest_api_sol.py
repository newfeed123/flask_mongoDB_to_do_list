import pymongo
from flask import Flask
from flask import request, jsonify
from flask_cors import CORS

database_name = "API"
mongodb_password = "2711Huy1"
myclient = pymongo.MongoClient("mongodb+srv://tranngochuy12ctm1:{}@cluster0.amvoe8u.mongodb.net/{}?retryWrites=true&w=majority&appName=Cluster0".format(mongodb_password, database_name)")