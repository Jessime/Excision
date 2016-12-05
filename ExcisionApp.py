# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 18:52:28 2015

@author: jessime
"""

import subprocess as sp

from flask import Flask, render_template, send_file, request

from pick_file import pick

from os.path import isfile

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
    syntax_error = None
    semantics_error = None
    if request.method == 'POST':
        Data.submission_form = next(request.form.keys())
        Data.script = pick()
        cmd = 'python {} ATATATATGGGGGC'.format(Data.script)
        try:
            sp.run(cmd.split(), stderr=sp.PIPE, check=True)
        except sp.CalledProcessError as e:
            syntax_error = e.stderr.decode("utf-8")
        if syntax_error is None:
            if not isfile('results/tutorial/gc.txt'):
                semantics_error = 'Your program did not produce a file in the proper location'
            else:
                with open('results/tutorial/gc.txt') as infile:
                    result = infile.read()
                    if not result:
                        semantics_error = 'There is nothing in the file you created'
                    elif result != '42%\n':
                        semantics_error = 'Your answer is not correct.'
                    else:
                        semantics_error = 'Good job! There was no error!'
        #return redirect(url_for('.tutorial', error=error))
    return render_template('tutorial.html',
                           syntax_error=syntax_error,
                           semantics_error=semantics_error)




#@app.route('/pollution_npy')
#def pollution_npy():
#    return send_file('data/pollution_npy.zip',
#                     mimetype='application/zip',
#                     attachment_filename='pollution_npy.zip',
#                     as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
