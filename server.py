# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 16:06:56 2019

@author: Erick
"""

from waitress import serve

#from os import environ
from flask import Flask

app = Flask(__name__)
#app.run(host= '0.0.0.0', port=environ.get('PORT'))

#app = Flask(__name__)
serve(app, listen='*:8080')
app.run()
