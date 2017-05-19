# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 18:52:28 2015

@author: jessime
"""

import sys
import markdown

from flask import Flask, Markup, render_template, redirect, request


from pick_file import pick
from state import Tutorial, Data
from level_markdown import parse

from webbrowser import open_new_tab

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
    sections = {k:markup_str(v) if (k not in no_markup) else v for k,v in sections.items()}
    sections['hint_solved1'] = True
    sections['hint_solved2'] = True
    sections['hint_solved3'] = True

    return render_template('level_content.html', **sections)

@app.route('/story')
def story():
    return render_template('story.html')

@app.route('/tutorial', methods=['GET', 'POST'])
def tutorial():
    if request.method == 'POST':
        Tutorial.script = pick()
        if Tutorial.script is not None:
            Tutorial.process_post(next(request.form.keys()))
        if Tutorial.semantics_error2 == 'Good job! There was no error!':
            return redirect('launch')

    return render_template('tutorial.html', **vars(Tutorial))

if __name__ == "__main__":
    if sys.version_info[0] != 3:
        assert False, 'Python version must be 3.x'
    url = 'http://127.0.0.1:5000'
    open_new_tab(url)
    app.run(debug=True)
