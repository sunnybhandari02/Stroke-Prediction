# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 16:27:18 2020

@author: User
"""

import numpy as np
import pandas as pd
from flask import Flask, request, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl','rb'))

@app.route('/',methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/index',methods = ['POST'])
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def predict():
    if request.method == 'POST':
        gender = request.form['gender']
        if(gender == 'Male'):
            gender=1
        else:
            gender=0
        age = int(request.form['age'])
        hypertension = request.form['hypertension']
        if(hypertension == 'Yes'):
            hypertension = 1
        else:
            hypertension = 0
        
        heart_disease = request.form['heart_disease']
        if(heart_disease == 'Yes'):
            heart_disease =1
        else:
            heart_disease = 0
        
        ever_married = request.form['martial_status']
        if(ever_married == 'Yes'):
            ever_married = 1
        else:
            ever_married = 0
        
        work_type = request.form['work_type']
        if(work_type == 'Govt-job'):
            work_type = 0
        elif(work_type == 'Never Worked'):
            work_type = 1
        elif(work_type == 'Private'):
            work_type = 2
        elif(work_type == 'Self-employed'):
            work_type = 3
        else:
            work_type = 4
            
        Residence_type = request.form['residence_type']
        if(Residence_type == 'Urban'):
            Residence_type = 1
        else:
            Residence_type = 0
            
        avg_glucose_level = int(request.form['glucose_level'])
        bmi = int(request.form['bmi'])
        
        smoking_status = request.form['smoking_status']
        if(smoking_status == 'Unknown'):
            smoking_status = 0
        elif(smoking_status == 'Formerly Smoked'):
            smoking_status = 1
        elif(smoking_status == 'Never Smoked'):
            smoking_status = 2
        else:
            smoking_status = 3
            
    
        output = model.predict([[gender,age,hypertension,heart_disease,ever_married,work_type,Residence_type,avg_glucose_level,bmi,smoking_status]])
        
        if int(output) == 1 :
            res_val = "Patient has a chances of getting STROKE !!"
        else :
            res_val = "Patient is NORMAL !!"
        
        return render_template('result.html', prediction_text= res_val)
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)