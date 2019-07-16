# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 18:42:58 2019

@author: USER
"""

import flask
from flask import jsonify
import numpy as np
import pandas as pd

app = flask.Flask(__name__)
app.config["DEBUG"] = True
app.config["JSON_AS_ASCII"] = False

# test data
tpe = {
    "id": 0,
    "city_name": "台北",
    "country_name": "台灣",
    "is_capital": True,
    "location": {
        "longitude": 121.569649,
        "latitude": 25.036786
    }
}
nyc = {
    "id": 1,
    "city_name": "紐約",
    "country_name": "美國",
    "is_capital": False,
    "location": {
        "longitude": -74.004364,
        "latitude": 40.710405
    }
}
ldn = {
    "id": 2,
    "city_name": "倫敦",
    "country_name": "英國",
    "is_capital": True,
    "location": {
        "longitude": -0.114089,
        "latitude": 51.507497
    }
}
    
cities = [tpe, nyc, ldn]
#print(cities)

gapminder = pd.read_csv("gapminder.csv")
gapminder_list = []
nrows = gapminder.shape[0] #row of your input data from csv

for i in range(nrows):
    ser = gapminder.loc[i, :]
    row_dict = {}
    for idx, val in zip(ser.index, ser.values):
        if type(val) is str:
            row_dict[idx] = val
        elif type(val) is np.int64:
            row_dict[idx] = int(val)
        elif type(val) is np.float64:
            row_dict[idx] = float(val)
    gapminder_list.append(row_dict)

'''
將觀測值由DataFrame出來的時候是 pd.Series 的資料結構，
裡頭的整數資料型態並不是 Python 的 int 而是 NumPy 中的 numpy.int64；
浮點數資料型態也不是 float 而是 numpy.float64，因此需要資料型態的轉換來解決。
'''


@app.route('/', methods=['GET'])
def home():
    return "<h1>Hello Flask!</h1>"


@app.route('/cities/all', methods=['GET'])
def cities_all():
    return jsonify(cities)


@app.route('/gapminder/all', methods=['GET'])
def gapminder_all():
    return jsonify(gapminder_list)

app.run(debug=False)

#cd C:\Users\USER\gapminder-api
#set FLASK_APP=api_sample2.py
#flask run

#http://127.0.0.1:5000/
#http://127.0.0.1:5000/cities/all

# http://127.0.0.1:5000/gapminder/all