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
    Total_Year = int(request.form['Total_Year'])
    Power = int(request.form['Power'])
    Kilometers_Driven = int(request.form['Kilometers_Driven'])
    Seats= int(request.form['Kilometers_Driven'])
    Mileage = float(request.form['Miles'])
    ## Location 
    Location = request.form['Location']
    if Location=='Bangalore':
        Location_Bangalore=1
        Location_Chennai=0
        Location_Coimbatore=0
        Location_Delhi=0
        Location_Hyderabad=0
        Location_Jaipur=0
        Location_Kochi=0
        Location_Kolkata=0
        Location_Mumbai=0
        Location_Pune=0
    elif Location=='Chennai':
        Location_Bangalore=0
        Location_Chennai=1
        Location_Coimbatore=0
        Location_Delhi=0
        Location_Hyderabad=0
        Location_Jaipur=0
        Location_Kochi=0
        Location_Kolkata=0
        Location_Mumbai=0
        Location_Pune=0
    elif Location=='Coimbatore':
        Location_Bangalore=0
        Location_Chennai=0
        Location_Coimbatore=1
        Location_Delhi=0
        Location_Hyderabad=0
        Location_Jaipur=0
        Location_Kochi=0
        Location_Kolkata=0
        Location_Mumbai=0
        Location_Pune=0
    elif Location=='Delhi':
        Location_Bangalore=0
        Location_Chennai=0
        Location_Coimbatore=0
        Location_Delhi=1
        Location_Hyderabad=0
        Location_Jaipur=0
        Location_Kochi=0
        Location_Kolkata=0
        Location_Mumbai=0
        Location_Pune=0
    elif Location=='Hyderabad':
        Location_Bangalore=0
        Location_Chennai=0
        Location_Coimbatore=0
        Location_Delhi=0
        Location_Hyderabad=1
        Location_Jaipur=0
        Location_Kochi=0
        Location_Kolkata=0
        Location_Mumbai=0
        Location_Pune=0
    elif Location=='Jaipur':
        Location_Bangalore=0
        Location_Chennai=0
        Location_Coimbatore=0
        Location_Delhi=0
        Location_Hyderabad=0
        Location_Jaipur=1
        Location_Kochi=0
        Location_Kolkata=0
        Location_Mumbai=0
        Location_Pune=0
    elif Location=='Kochi':
        Location_Bangalore=0
        Location_Chennai=0
        Location_Coimbatore=0
        Location_Delhi=0
        Location_Hyderabad=0
        Location_Jaipur=0
        Location_Kochi=1
        Location_Kolkata=0
        Location_Mumbai=0
        Location_Pune=0
    elif Location=='Kolkata':
        Location_Bangalore=0
        Location_Chennai=0
        Location_Coimbatore=0
        Location_Delhi=0
        Location_Hyderabad=0
        Location_Jaipur=0
        Location_Kochi=0
        Location_Kolkata=1
        Location_Mumbai=0
        Location_Pune=0
    elif Location=='Mumbai':
        Location_Bangalore=0
        Location_Chennai=0
        Location_Coimbatore=0
        Location_Delhi=0
        Location_Hyderabad=0
        Location_Jaipur=0
        Location_Kochi=0
        Location_Kolkata=0
        Location_Mumbai=1
        Location_Pune=0
    elif Location=='Pune':
        Location_Bangalore=0
        Location_Chennai=0
        Location_Coimbatore=0
        Location_Delhi=0
        Location_Hyderabad=0
        Location_Jaipur=0
        Location_Kochi=0
        Location_Kolkata=0
        Location_Mumbai=0
        Location_Pune=1
    else:
        Location_Bangalore=0
        Location_Chennai=0
        Location_Coimbatore=0
        Location_Delhi=0
        Location_Hyderabad=0
        Location_Jaipur=0
        Location_Kochi=0
        Location_Kolkata=0
        Location_Mumbai=0
        Location_Pune=0
    
     ## Owner Type
    Owner_Type = request.form['Owner_Type']
  
    if Owner_Type=='First':
       Owner_Type_Others=0
    else:
        Owner_Type_Others=1
        
    ## Transmission
    Transmission = request.form['Transmission']
    if Transmission == 'Manual':
        Transmission_Manual=1
    else:
        Transmission_Manual=0
    ## Fuel_Type
    Fuel_Type = request.form['Fuel_Type']
    if Fuel_Type == 'Petrol':
        Fuel_Type_Petrol=1
        Fuel_Type_LPG=0
        Fuel_Type_CNG=0
    elif Fuel_Type == 'Diesel':
        Fuel_Type_Petrol=1
        Fuel_Type_LPG=0
        Fuel_Type_CNG=0
    elif Fuel_Type == 'LPG':
        Fuel_Type_Petrol=0
        Fuel_Type_LPG=1
        Fuel_Type_CNG=0
    else:
        Fuel_Type_Petrol=0
        Fuel_Type_LPG=0
        Fuel_Type_CNG=0


   

    prediction=model.predict([[Location_Bangalore, Location_Chennai, Location_Coimbatore,
       Location_Delhi, Location_Hyderabad, Location_Jaipur,
       Location_Kochi, Location_Kolkata, Location_Mumbai,
       Location_Pune, Fuel_Type_LPG, Fuel_Type_Petrol,
       Transmission_Manual, Owner_Type_Others, Total_Year,
       Kilometers_Driven, Mileage, Power, Seats]])
    output = round(prediction[0],2)
    
    return render_template('index.html',pred= 'Car Price = {}'.format(output))

    

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)