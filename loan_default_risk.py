import pandas as pd
import numpy as np
import streamlit as st
import joblib

# Load the saved model
model = joblib.load("loan_default_risk_predictor.pkl")

# Add the streamlit title
st.title("Loan Default Risk Predictor App")
st.markdown("### Predict the likelihood of loan default risk")

# Create a sidebar for user input
st.sidebar.header("User Input")
loan_amount = st.sidebar.slider("Loan Amount", 1000, 50000, 10000)
total_due = st.sidebar.number_input("Total Due", min_value=10000, max_value=100000)
term_days = st.sidebar.slider("Term Days", 15, 90)
bank_account_type = st.sidebar.selectbox("Bank Account Type", ['savings', 'current', 'others'])
longitude_gps = st.sidebar.slider("Longitude GPS", -200.0, 200.0)
latitude_gps = st.sidebar.slider("Latitude GPS", -200.0, 200.0)
bank_name_clients = st.sidebar.selectbox("Bank Name Clients", ['access', 'fidelity','first bank', 'uba', 'others'])
employment_status_clients = st.sidebar.selectbox("Employment Status Clients", ['students', 'unemployed', 'self-employed', 'contract', 'permanent', 'retired'])
age = st.sidebar.slider("Age", 18, 90)

# Compute Age Category
if age <= 18:
    age_category = 'Teens'
elif age <= 38:
    age_category = 'Youth'
elif age <= 48:
    age_category = 'Young Adult'
elif age <= 58:
    age_category = 'Adult'
elif age <= 68:
    age_category = 'Mid_Age'
else:
    age_category = 'Aged'

# Compute Employment Risk
employment_risk_map = {
    'students': 'High Risk',
    'unemployed': 'High Risk',
    'contract': 'Medium Risk',
    'self-employed': 'Medium Risk',
    'permanent': 'Low Risk',
    'retired': 'Low Risk - Retired'
}
employment_risk = employment_risk_map[employment_status_clients]

# Compute interest
interest = total_due - loan_amount

# Predict button
if st.sidebar.button("Predict Loan Default Risk"):
    data = {
        "loan_amount": [loan_amount],
        "total_due": [total_due],
        "term_days": [term_days],
        "bank_account_type": [bank_account_type],
        "longitude_gps": [longitude_gps],
        "latitude_gps": [latitude_gps],
        "bank_name_clients": [bank_name_clients],
        "employment_status_clients": [employment_status_clients],
        "age_category": [age_category],
        "employment_risk": [employment_risk],
        "interest": [interest]
    }
    
    # Create a DataFrame
    df = pd.DataFrame(data)
    
    # Create logarithmic transformations of the features
    df['total_due_log'] = np.log(df['total_due'])
    df['latitude_gps_log'] = np.log(np.abs(df['latitude_gps']) + 1)
    df['interest_log'] = np.log(df['interest'] + 1)
    df['longitude_gps_log'] = np.log(np.abs(df['longitude_gps']) + 1)
    df['term_days_log'] = np.log(df['term_days'])
    df['loan_amount_log'] = np.log(df['loan_amount'])

    # Drop original columns
    df = df.drop(['loan_amount', 'total_due', 'term_days', 'longitude_gps', 'latitude_gps', 'interest'], axis=1)

    # Predict the model
    loan_default_risk = model.predict(df)
    prediction = loan_default_risk[0]

    if prediction == 0:
        st.success(f'### Loan Default Risk: Low')
        st.markdown("The loan default risk is low. The customer is likely to repay the loan.")
    else:
        st.error(f'### Loan Default Risk: High')
        st.markdown("The loan default risk is high. The customer may default on the loan.")

