import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    Tenure = int(request.form['Tenure'])
    TotalCharges = float(request.form['TotalCharges'])
    MonthlyCharges = float(request.form['MonthlyCharges'])
   
    Contract = request.form['contract']
    if Contract=='Yes':
        Contract=1
    else:
        Contract=0

    Payment_Method_Electric = request.form['Payment_Method_Electric']
    if Payment_Method_Electric=='Yes':
        Payment_Method_Electric=1
    else:
        Payment_Method_Electric=0

    prediction=model.predict([[Tenure,Contract,Payment_Method_Electric,MonthlyCharges,TotalCharges]])
    output = prediction[0]
    if output == 1:
        return render_template('index.html',pred='Your Customer will leave ')

    else:
        return render_template('index.html',pred='Your customer will stay ')

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)