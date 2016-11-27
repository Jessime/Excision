# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 18:52:28 2015

@author: jessime
"""
import flask as f
from authomatic.adapters import WerkzeugAdapter
from authomatic import Authomatic
from config import CONFIG

app = f.Flask(__name__)
# Instantiate Authomatic.
authomatic = Authomatic(CONFIG, 'your secret string', report_errors=True)

@app.route("/")
def main():
    return f.render_template('index.html')

@app.route('/story')
def story():
    return f.render_template('story.html')

@app.route('/about')
def about():
    return f.render_template('about.html')

@app.route('/elements')
def elements():
    return f.render_template('elements.html')
    
@app.route('/login/<provider_name>/', methods=['GET', 'POST'])
def login(provider_name):
    """
    Login as described at:
    http://peterhudec.github.io/authomatic/examples/flask-simple.html
    """
    response = f.make_response()
    result = authomatic.login(WerkzeugAdapter(f.request, response), provider_name)
    if result:
        if result.user:
            result.user.update()
        return f.render_template('login.html', result=result)    
    return response  
    
@app.route('/launch', methods=['GET','POST'])
def launch():
    if f.request.method == 'POST':
        if f.request.form['p-value'] == '0.1':
            return f.Response('whoot!')
        else:
            return f.Response('whoot!')
    return f.render_template('launch.html')

@app.route('/pollution_npy')
def pollution_npy():
    return f.send_file('data/pollution_npy.zip',
                     mimetype='application/zip',
                     attachment_filename='pollution_npy.zip',
                     as_attachment=True)
    
if __name__ == "__main__":
    app.run(debug=True)
