# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 18:42:58 2019

@author: USER

如何以 Python  Flask 在本機（localhost）設置 Web API 分享手動創建的資料 
cities（是一個 list of dictionaries）
與現成的 CSV 檔案 gapminder.csv（以 pandas 讀入為 DataFrame），
暸解如何解決繁體中文顯示、NumPy 資料型態以及查詢部分資料集的問題
https://medium.com/datainpoint/web-scraping-with-python/home
"""

import flask
from flask import jsonify, request
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

gapminder = pd.read_csv("gapminder.csv")
gapminder_list = []
nrows = gapminder.shape[0]
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


@app.route('/', methods=['GET'])
def home():
    return "<h1>Hello Flask!</h1>"


@app.route('/cities/all', methods=['GET'])
def cities_all():
    return jsonify(cities)


@app.route('/cities', methods=['GET'])
def city_name():
    if 'city_name' in request.args:
        city_name = request.args['city_name']
    else:
        return "Error: No city_name provided. Please specify a city_name."
    results = []

    for city in cities:
        if city['city_name'] == city_name:
            results.append(city)

    return jsonify(results)


@app.route('/gapminder/all', methods=['GET'])
def gapminder_all():
    return jsonify(gapminder_list)


@app.route('/gapminder', methods=['GET'])
def country():
    if 'country' in request.args:
        country = request.args['country']
    else:
        return "Error: No country provided. Please specify a country."
    results = []

    for elem in gapminder_list:
        if elem['country'] == country:
            results.append(elem)

    return jsonify(results)


app.run()

#cd C:\Users\USER\gapminder-api
#set FLASK_APP=api_sample2.py
#flask run

#http://127.0.0.1:5000/
#http://127.0.0.1:5000/cities/all
#http://127.0.0.1:5000/gapminder/all

#http://127.0.0.1:5000/cities?city_name=台北
#http://127.0.0.1:5000/gapminder?country=Taiwan