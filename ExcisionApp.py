# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 18:52:28 2015

@author: jessime
"""

from flask import Flask, render_template, send_file, request, redirect
from subprocess import check_call, CalledProcessError

from pick_file import pick


class Data():
    """Resposible for keeping track of the state of the app."""

    submission_form = None
    script = None

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
        Data.submission_form = next(request.form.keys())
        Data.script = pick()
        cmd = 'python {} ATATATATGGGGGC'.format(Data.script)
        result = None
        try:
            result = check_call(cmd.split())
        except CalledProcessError:
            print(type(result))
        return redirect('/tutorial')
    return render_template('tutorial.html')




@app.route('/pollution_npy')
def pollution_npy():
    return send_file('data/pollution_npy.zip',
                     mimetype='application/zip',
                     attachment_filename='pollution_npy.zip',
                     as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
