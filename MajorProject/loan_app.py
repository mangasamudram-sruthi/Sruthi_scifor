import streamlit as st
import pandas as pd
import pickle

# Load the trained model, encoders, and scaler
with open('loan_model_svm.pkl', 'rb') as file:
    model = pickle.load(file)

with open('label_encoders_svm.pkl', 'rb') as file:
    encoders = pickle.load(file)

with open('scaler_svm.pkl', 'rb') as file:
    scaler = pickle.load(file)

# Define the Streamlit app
st.title('Loan Prediction System - SVM Model')

# Input fields for user data
gender = st.selectbox('Gender', ['Male', 'Female'])
married = st.selectbox('Married', ['Yes', 'No'])
dependents = st.selectbox('Dependents', ['0', '1', '2', '3+'])
education = st.selectbox('Education', ['Graduate', 'Not Graduate'])
self_employed = st.selectbox('Self Employed', ['Yes', 'No'])
applicant_income = st.number_input('Applicant Income', min_value=0)
coapplicant_income = st.number_input('Coapplicant Income', min_value=0)
loan_amount = st.number_input('Loan Amount', min_value=0)
loan_amount_term = st.number_input('Loan Amount Term', min_value=0)
credit_history = st.selectbox('Credit History', [1.0, 0.0])
property_area = st.selectbox('Property Area', ['Urban', 'Semiurban', 'Rural'])

# Preprocess user input using the same encoders and scaler as during training
inputs = pd.DataFrame({
    'Gender': [gender],
    'Married': [married],
    'Dependents': [dependents],
    'Education': [education],
    'Self_Employed': [self_employed],
    'ApplicantIncome': [applicant_income],
    'CoapplicantIncome': [coapplicant_income],
    'LoanAmount': [loan_amount],
    'Loan_Amount_Term': [loan_amount_term],
    'Credit_History': [credit_history],
    'Property_Area': [property_area]
})

# Apply the encoders
for column in ['Gender', 'Married', 'Dependents', 'Education', 'Self_Employed', 'Property_Area']:
    inputs[column] = encoders[column].transform(inputs[column])

# Apply scaling
inputs = scaler.transform(inputs)

# Predict using the model and show probabilities
if st.button('Predict'):
    probability = model.predict_proba(inputs)[0][1]  # Probability of class 1 (Loan Approved)
    
    # Set a custom threshold for approval
    threshold = 0.5  # You can adjust this value based on your needs

    if probability > threshold:
        st.write(f'Approval Probability: {probability:.2f}')
        st.success('Loan Approved')
    else:
        st.write(f'Approval Probability: {probability:.2f}')
        st.error('Loan Denied')