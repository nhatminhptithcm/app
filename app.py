# python -m streamlit run app.py
import numpy as np
import pandas as pd
import streamlit as st
st.title('Khách hàng sẽ rời bỏ dịch vụ viễn thông?')

import pickle
filename = 'model.sav'
model = pickle.load(open(filename, 'rb'))

passengerid = st.text_input("Input Passenger ID", '123456') 
pclass = st.selectbox("Choose class", [1,2,3])
name  = st.text_input("Input Passenger Name", 'John Smith')
sex = st.select_slider("Choose sex", ['male','female'])
age = st.slider("Choose age",0,100)
sibsp = st.slider("Choose siblings",0,10)
parch = st.slider("Choose parch",0,2)
ticket = st.text_input("Input Ticket Number", "12345") 
fare = st.number_input("Input Fare Price", 0,1000)
cabin = st.text_input("Input Cabin", "C52") 
embarked = st.select_slider("Did they Embark?", ['S','C','Q'])

def predict():

    row = np.array([1, 0, 0, 0, 0.056338, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0.668159, 0.046977, False, True, False, True, False, False, False, True, False, False])
    row = np.array([0,0,1,1,0.253521,1,0,0,0,0,0,0,0,0,0.016418,0.039107,False,False,True,False,True,False,False,False,False,True]) 
    columns = ['gender', 'SeniorCitizen', 'Partner', 'Dependents', 'tenure', 'PhoneService', 'MultipleLines', 'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies', 'PaperlessBilling', 'MonthlyCharges', 'TotalCharges', 'InternetService_DSL', 'InternetService_Fiber optic', 'InternetService_No', 'Contract_Month-to-month', 'Contract_One year', 'Contract_Two year', 'PaymentMethod_Bank transfer (automatic)', 'PaymentMethod_Credit card (automatic)', 'PaymentMethod_Electronic check', 'PaymentMethod_Mailed check']
    sample_test = pd.DataFrame([row], columns = columns)
    prediction = model.predict(sample_test)

    if prediction[0] == 1: 
        st.error('Khách hàng sẽ rời bỏ')    
    else: 
        st.success('Khách hàng sẽ ở lại')

trigger = st.button('Predict', on_click=predict)
