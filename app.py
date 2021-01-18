from flask import Flask
from wsgiref import simple_server
from flask import Flask, request, render_template
from flask import Response
import os
from flask_cors import CORS, cross_origin
#import flask_monitoringdashboard as dashboard
import json
#from utils import methods

os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')


app=Flask(__name__)
#dashboard.bind(app)
CORS(app)


@app.route('/', methods=['GET'])
@cross_origin()
def login():
    return render_template('index.html')

@app.route('/register')
@cross_origin()
def register():
    return render_template('register.html')

@app.route('/admin')
@cross_origin()
def admin():
    return render_template('admin.html')

@app.route('/home')
@cross_origin()
def home():
    return render_template('home.html')

@app.route('/profile')
@cross_origin()
def profile():
    return render_template('profile.html')

@app.route('/about')
@cross_origin()
def about():
    return render_template('about.html')

@app.route('/adm_dash')
@cross_origin()
def admin_dashboard():
    return render_template('admdash.html')



if __name__=="__main__":
    app.run(debug=True)

