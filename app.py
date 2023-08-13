# python -m streamlit run app.py
import numpy as np
import pandas as pd
import streamlit as st
import pickle

filename = 'model.sav'
model = pickle.load(open(filename, 'rb'))

st.title('Khách hàng sẽ rời bỏ dịch vụ viễn thông?')

gender=st.selectbox('Giới tính :' , ['Nam', 'Nữ'])
seniorCitizen=st.selectbox('Người cao tuổi :' , ['Có', 'Không'])
partner=st.selectbox('Đối tác :' , ['Có', 'Không'])
dependents=st.selectbox('Người phụ thuộc :' , ['Có', 'Không'])
tenure=st.number_input("Chu kỳ đã sử dụng (0-72)") 
phoneService=st.selectbox('Dịch vụ điện thoại :' , ['Có', 'Không'])
multipleLines=st.selectbox('MultipleLines :' , ['Có', 'Không'])
internetService=st.selectbox('Dịch vụ Intermet :' , ['Không', 'DSL', 'Fiber optic'])
onlineSecurity=st.selectbox('An ninh trực tuyến :' , ['Có', 'Không'])
onlineBackup=st.selectbox('Sao lưu trực tuyến :' , ['Có', 'Không'])
deviceProtection=st.selectbox('Bảo vệ thiết bị :' , ['Có', 'Không'])
techSupport=st.selectbox('Hỗ trợ kỹ thuật :' , ['Có', 'Không'])
streamingTV=st.selectbox('Truyền hình trực tuyến :' , ['Có', 'Không'])
streamingMovies=st.selectbox('Phim trực tuyến :' , ['Có', 'Không'])
contract=st.selectbox('Loại hợp đồng :' , ['Hàng tháng', '1 năm', '2 năm'])
paperlessBilling=st.selectbox('Hóa đơn điện tử :' , ['Có', 'Không'])
paymentMethod=st.selectbox('Phương thức thanh toán :' , ['Thẻ tín dụng', 'Chuyển khoản', 'Gửi mail', 'Thông báo số điện'])
monthlyCharges=st.number_input("Chi phí hàng tháng (18.25-118.75)") 
totalCharges=st.number_input("Tổng chi phí (18.8-8684.8)")

def predict():
    param_gender = 1 if gender == 'Nữ' else 0
    param_SeniorCitizen = 1 if seniorCitizen == 'Có' else 0
    param_Partner = 1 if partner == 'Có' else 0
    param_Dependents = 1 if dependents == 'Có' else 0
    param_tenure = tenure/72
    param_PhoneService = 1 if phoneService == 'Có' else 0
    param_MultipleLines = 1 if multipleLines == 'Có' else 0
    param_OnlineSecurity = 1 if onlineSecurity == 'Có' else 0
    param_OnlineBackup = 1 if onlineBackup == 'Có' else 0
    param_DeviceProtection = 1 if deviceProtection == 'Có' else 0 
    param_TechSupport = 1 if techSupport == 'Có' else 0 
    param_StreamingTV = 1 if streamingTV == 'Có' else 0 
    param_StreamingMovies = 1 if streamingMovies == 'Có' else 0 
    param_PaperlessBilling = 1 if paperlessBilling == 'Có' else 0 
    param_MonthlyCharges = (monthlyCharges -18.25)/(118.75-18.25)
    param_TotalCharges = (totalCharges-18.8)/(8684.8-18.8)
    param_InternetService_DSL = 1 if internetService == 'DSL' else 0
    param_InternetService_Fiber = 1 if internetService == 'Fiber optic' else 0
    param_InternetService_No = 1 if internetService == 'No' else 0
    param_Contract_Month = 1 if contract == 'Hàng tháng' else 0
    param_Contract_One = 1 if contract == '1 năm' else 0
    param_Contract_Two = 1 if contract == '2 năm' else 0
    param_PaymentMethod_Bank = 1 if paymentMethod == 'Chuyển khoản' else 0 
    param_PaymentMethod_Credit = 1 if paymentMethod == 'Thẻ tín dụng' else 0 
    param_PaymentMethod_Electronic = 1 if paymentMethod == 'Thông báo số điện' else 0 
    param_PaymentMethod_Mailed = 1 if paymentMethod == 'Gửi mail' else 0

    # row = np.array([1,0,0,0,0.056338,1,0,0,0,0,1,0,1,1,0.668159,0.046977,False,True,False,True,False,False,False,True,False,False]) # churn
    # row = np.array([0,0,1,1,0.253521,1,0,0,0,0,0,0,0,0,0.016418,0.039107,False,False,True,False,True,False,False,False,False,True]) # no churn
    row = np.array([param_gender, param_SeniorCitizen, param_Partner, param_Dependents, param_tenure, param_PhoneService, param_MultipleLines, param_OnlineSecurity, param_OnlineBackup, param_DeviceProtection, param_TechSupport, param_StreamingTV, param_StreamingMovies, param_PaperlessBilling, param_MonthlyCharges, param_TotalCharges, param_InternetService_DSL, param_InternetService_Fiber, param_InternetService_No, param_Contract_Month, param_Contract_One, param_Contract_Two, param_PaymentMethod_Bank, param_PaymentMethod_Credit, param_PaymentMethod_Electronic, param_PaymentMethod_Mailed])
    
    columns = ['gender', 'SeniorCitizen', 'Partner', 'Dependents', 'tenure', 'PhoneService', 'MultipleLines', 'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies', 'PaperlessBilling', 'MonthlyCharges', 'TotalCharges', 'InternetService_DSL', 'InternetService_Fiber optic', 'InternetService_No', 'Contract_Month-to-month', 'Contract_One year', 'Contract_Two year', 'PaymentMethod_Bank transfer (automatic)', 'PaymentMethod_Credit card (automatic)', 'PaymentMethod_Electronic check', 'PaymentMethod_Mailed check']
    sample = pd.DataFrame([row], columns = columns)
    prediction = model.predict(sample)

    if prediction[0] == 1: 
        st.error('Khách hàng sẽ rời bỏ')    
    else: 
        st.success('Khách hàng sẽ ở lại')

trigger = st.button('Predict', on_click=predict)