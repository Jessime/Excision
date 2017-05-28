# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 18:52:28 2015

@author: jessime
"""

import sys
import os
import markdown
import subprocess as sp

from webbrowser import open_new_tab
from flask import Flask, Markup, render_template, redirect, request, jsonify
from pprint import pprint

#from pick_file import pick
from state import Tutorial, Data
from level_markdown import parse


def markup_str(string):
    """Prepares a markdown formatted string for insertion into jinja template."""
    markup = Markup(markdown.markdown(string))
    return markup

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
    infile = 'static/story/level1.md'
    no_markup = {'title', 'subtitle', 'img'}
    sections = parse(infile)
    #pprint(sections)
    sections = {k:markup_str(v) if (k not in no_markup) else v for k,v in sections.items()}
    sections['hint_solved1'] = True
    sections['hint_solved2'] = True
    sections['hint_solved3'] = True

    return render_template('level_content.html', **sections)

@app.route('/story')
def story():
    return render_template('story.html')

@app.route('/tutorial_button')
def tutorial_button():
    result = False
    cmd = 'python pick_file.py'.split()
    p = sp.Popen(cmd, stdout=sp.PIPE)
    Tutorial.script = p.communicate()[0].decode('utf-8').strip()
    if Tutorial.script is not None:
        success, error = Tutorial.process_request(request.args['button'])
    return jsonify(success=success, error=error)

@app.route('/tutorial')
def tutorial():
    return render_template('tutorial.html', **vars(Tutorial))

def assert_py3():
    if sys.version_info[0] != 3:
        assert False, 'Python version must be 3.x'

def make_results_dir():
    package = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    results = os.path.join(package, 'results')
    if not os.path.exists(results):
        os.makedirs(results)
        os.makedirs(os.path.join(results, 'tutorial'))

def setup():
    assert_py3()
    make_results_dir()
    url = 'http://127.0.0.1:5000'
    open_new_tab(url)

if __name__ == "__main__":
    setup()
    app.run(debug=True)
