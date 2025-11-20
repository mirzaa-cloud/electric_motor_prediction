import streamlit as st
import requests

st.title("Electric Motor Speed Predictor")

api_url = "http://localhost:8000/predict"  # Change if your backend runs elsewhere

feature_names = [
    "ambient", "coolant", "u_d", "u_q", "i_d", "i_q",
    "pm", "stator_yoke", "stator_tooth", "stator_winding", "torque"
]

inputs = {}
for feat in feature_names:
    inputs[feat] = st.number_input(f"{feat.replace('_', ' ').title()}:", value=0.0)

if st.button("Predict Motor Speed"):
    response = requests.post(api_url, json=inputs)
    if response.status_code == 200:
        st.success("Predicted Motor Speed: {:.2f}".format(response.json()["predicted_motor_speed"]))
    else:
        st.error("Prediction failed: {}".format(response.text))
