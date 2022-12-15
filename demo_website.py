# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 00:40:00 2022

@author: andko
"""

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world ():
    return "Hello World, this is going to a web browser"

app.run()