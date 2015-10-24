# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 18:52:28 2015

@author: jessime
"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

@app.route('/story')
def story():
    return render_template('story.html')
    
if __name__ == "__main__":
    app.run(debug=True)