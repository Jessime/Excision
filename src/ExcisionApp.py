# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 18:52:28 2015

@author: jessime
"""

import sys
import os
import markdown
import subprocess as sp
import json

from webbrowser import open_new_tab
from flask import Flask, Markup, render_template, redirect, request, jsonify
from pprint import pprint

#from pick_file import pick
from play_levels import State
from tutorial import Tutorial
from level_markdown import parse


app = Flask(__name__)

def markup_str(string):
    """Prepares a markdown formatted string for insertion into jinja template."""
    markup = Markup(markdown.markdown(string))
    return markup

@app.route("/")
def index():
    return render_template('index.html', lvl_title=State.lvl_title)

@app.route('/play/<title>')
def play(title):
    titles_name_map = json.load(open('static/story/all_titles.md'))
    lvl_num = titles_name_map[title]
    State.lvl_num_active = lvl_num
    completed_titles = [k for k, v in titles_name_map.items() if v <= State.lvl_num_top]
    infile = 'static/story/level{}.md'.format(lvl_num)
    no_markup = {'title', 'subtitle', 'img'}
    sections = parse(infile)
    sections = {k:markup_str(v) if (k not in no_markup) else v for k,v in sections.items()}

    return render_template('level_content.html',
                           completed_titles=completed_titles,
                           **sections)

@app.route('/story')
def story():
    return render_template('story.html', lvl_title=State.lvl_title)

@app.route('/about')
def about():
    return render_template('about.html', lvl_title=State.lvl_title)

@app.route('/level_button')
def level_button():
    result=False
    success=None
    error=None
    State.script = get_script_path()
    button = request.args['button']
    if State.script is not None:
        success, error = State.process_request(button)
        if success and button == 'problem' and State.lvl_num_top == State.lvl_num_active:
            State.update_config()
    print('success:', success)
    print('error:', error)
    return jsonify(success=success, error=error, next_url=State.lvl_title)

@app.route('/tutorial_button')
def tutorial_button(): #TODO Merge into level_button?
    result=False
    success=None
    error=None
    Tutorial.script = get_script_path() #TODO need to save?
    if Tutorial.script is not None:
        success, error = Tutorial.process_request(request.args['button'])
    return jsonify(success=success, error=error, next_url=State.lvl_title)

@app.route('/tutorial')
def tutorial():
    return render_template('tutorial.html', lvl_title=State.lvl_title) #TODO Do I still need to pass vars?

def assert_py3():
    assert sys.version_info[0] == 3, 'Python version must be 3.x'

def get_script_path():
    cmd = 'python pick_file.py'.split() #HACK Macs don't like running PyQT in this program.
    p = sp.Popen(cmd, stdout=sp.PIPE)
    path = p.communicate()[0].decode('utf-8').strip()
    return path

def make_results_dir():
    results = os.path.join(State.PACKAGE, 'results')
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
    app.run(debug=False)
