# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 18:42:58 2019

@author: USER
"""

import flask
from flask import jsonify
import pandas as pd

app = flask.Flask(__name__)
app.config["DEBUG"] = True
app.config["JSON_AS_ASCII"] = False

# test data
tpe = {
    "id": 0,
    "city_name": "Taipei",
    "country_name": "Taiwan",
    "is_capital": True,
    "location": {
        "longitude": 121.569649,
        "latitude": 25.036786
    }
}
    
nyc = {
    "id": 1,
    "city_name": "New York",
    "country_name": "United States",
    "is_capital": False,
    "location": {
        "longitude": -74.004364,
        "latitude": 40.710405
    }
}
    
ldn = {
    "id": 2,
    "city_name": "London",
    "country_name": "United Kingdom",
    "is_capital": True,
    "location": {
        "longitude": -0.114089,
        "latitude": 51.507497
    }
}
    
cities = [tpe, nyc, ldn]
#print(cities)

'''
@app.route('/', methods=['GET'])
def home():
    return "<h1>Hello Flask!</h1>"
'''

@app.route('/cities/all', methods=['GET'])
def cities_all():
    return jsonify(cities)


app.run



#cd C:\Users\USER\gapminder-api
#set FLASK_APP=api_sample2.py
#flask run

#http://127.0.0.1:5000/
#http://127.0.0.1:5000/cities/all