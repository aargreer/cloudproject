from typing import Text
from flask import Flask, render_template , request ,flash
from model import read
import os
import argparse
import subprocess
import logging
from flask import Flask, request, jsonify, render_template, url_for, flash, redirect
from werkzeug.exceptions import abort
from flask_cors import CORS

import signal
import datetime
import sys
import shlex



app = Flask(__name__)

@app.route('/')
def index():
    
 return render_template('base2.html')

@app.route('/about')
def about():
 return render_template('group.html')

#inference
@app.route('/inference', methods=['POST', 'GET'])
def inference():
    if request.method == 'POST':
        sex = request.form['sex']
        smoker =request.form['smoker']
        bmi = request.form['bmi']
        region = request.form['region']
        age=request.form['age']
        children = request.form['kid']

        if not sex:
            flash('enter male or female')
        else:
            expense = read(sex,smoker,region,age, bmi,children)
            return render_template('inter.html',expense = expense)
    return render_template('inter.html')

if __name__ == "__main__":    
      app.run(debug=True, host='0.0.0.0', port=8080)
