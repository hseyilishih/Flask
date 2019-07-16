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


@app.route('/', methods=['GET'])
def xxx():
    return "<h1>Hello Flask xxx 5500!</h1>"

#exit
app.run(debug=False, port=5500)

# http://127.0.0.1:5000/

#cd C:\Users\USER\gapminder-api
#set FLASK_APP=api_sample1.py
#flask run