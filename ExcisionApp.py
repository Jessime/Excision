# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 18:52:28 2015

@author: jessime
"""

from flask import Flask, render_template

app = Flask(__name__)

GOOGLE_ID = '683188869719-rh2ggaee3jovi6vni5k0rebj51o4u1mv.apps.googleusercontent.com'
GOOGLE_SECRET = 'VxRSb62WkhQdse6z7BPe3mR-'

@app.route("/")
def main():
    return render_template('index.html')

@app.route('/story')
def story():
    return render_template('story.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/elements')
def elements():
    return render_template('elements.html')
    
if __name__ == "__main__":
    app.run(debug=True)
