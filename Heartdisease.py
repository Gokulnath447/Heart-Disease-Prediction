import streamlit as st
import pickle
import numpy as np
with open('Heart', 'rb') as file:
    model = pickle.load(file)

st.title('❤️ Heart Disease Prediction')
st.write('Enter the required data to predict heart disease (Yes / No)')

age = st.number_input('Age', min_value=1, max_value=120)
sex = st.selectbox('Sex (0 = Female, 1 = Male)', [0, 1])
cp = st.selectbox('Chest Pain Type (0–3)', [0, 1, 2, 3])
trestbps = st.number_input('Resting Blood Pressure')
chol = st.number_input('Cholesterol')
fbs = st.selectbox('Fasting Blood Sugar > 120 mg/dl (1 = Yes, 0 = No)', [0, 1])
restecg = st.selectbox('Resting ECG (0–2)', [0, 1, 2])
thalach = st.number_input('Maximum Heart Rate Achieved')
oldpeak = st.number_input('Oldpeak (ST depression)')
slope = st.selectbox('Slope (0–2)', [0, 1, 2])
ca = st.selectbox('Number of Major Vessels (0–3)', [0, 1, 2, 3])
thal = st.selectbox('Thal (1 = Normal, 2 = Fixed Defect, 3 = Reversible Defect)', [1, 2, 3])

# Prediction
if st.button("Predict Heart Disease"):
    input_data = np.array([[age, sex, cp, trestbps, chol, fbs,
                             restecg, thalach, oldpeak, slope, ca, thal]])
    prediction = model.predict(input_data)
    if prediction[0] == 1:
        st.error("⚠️ Heart Disease Detected")
    else:
        st.success("✅ No Heart Disease Detected")