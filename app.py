import streamlit as st
import pickle
import pandas as pd

# Load the trained RandomForest model
with open('rfmodel_pickle', 'rb') as f:
    rfc = pickle.load(f)

# Define the Streamlit app
st.title("Employee Retention Predictor")

st.write("This application predicts if an employee is likely to stay or leave based on various features.")

# Collect user input for each feature
sn = st.number_input("Satisfaction Level (e.g., 0.5)", min_value=0.0, max_value=1.0, step=0.01)
number_project = st.slider("Number of Projects", 1, 10, 3)
average_monthly_hours = st.number_input("Average Monthly Hours", min_value=0, max_value=400, step=1)
time_spend_company = st.slider("Years at Company", 1, 20, 3)
work_accident = st.selectbox("Work Accident", [0, 1])
high = st.selectbox("High Salary Level", [0, 1])
low = st.selectbox("Low Salary Level", [0, 1])

# Create a dataframe with the selected features
input_data = pd.DataFrame({
    'sn': [sn],
    'number_project': [number_project],
    'average_montly_hours': [average_monthly_hours],
    'time_spend_company': [time_spend_company],
    'Work_accident': [work_accident],
    'high': [high],
    'low': [low]
})

# Predict button
if st.button("Predict Retention"):
    # Make prediction
    prediction = rfc.predict(input_data)
    result = "Likely to Stay" if prediction[0] == 0 else "Likely to Leave"

    # Display the result
    st.subheader("Prediction Result")
    st.write(result)
