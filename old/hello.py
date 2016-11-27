# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 20:11:07 2015

@author: jessime
"""

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()