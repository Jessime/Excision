# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 18:52:28 2015

@author: jessime
"""

import sys

from flask import Flask, render_template, request

from pick_file import pick
from state import Tutorial, Data

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/elements')
def elements():
    return render_template('elements.html')


@app.route('/launch', methods=['GET','POST'])
def launch():
    if request.method == 'POST':
        pass
    return render_template('launch.html')

@app.route('/story')
def story():
    return render_template('story.html')

@app.route('/tutorial', methods=['GET', 'POST'])
def tutorial():
    if request.method == 'POST':
        Tutorial.script = pick()
        Tutorial.process_post(next(request.form.keys()))
        #return redirect(url_for('.tutorial', error=error))
    return render_template('tutorial.html',
                           syntax_error1=Tutorial.syntax_error1,
                           semantics_error1=Tutorial.semantics_error1,
                           syntax_error2=Tutorial.syntax_error2,
                           semantics_error2=Tutorial.semantics_error2,
                           hint_solved1=Tutorial.hint_solved1,
                           hint_solved2=Tutorial.hint_solved2)

if __name__ == "__main__":
    if sys.version_info[0] != 3:
        assert False, 'Python version must be 3.x'
    app.run(debug=True)
