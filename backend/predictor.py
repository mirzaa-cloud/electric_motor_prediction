import pickle
import os
from .preprocessing.pipeline import preprocess_input


MODEL_PATH = os.path.join(os.path.dirname(__file__), "model", "motor_speed_model.pkl")

with open(MODEL_PATH, "rb") as f:
    bundle = pickle.load(f)
model = bundle["model"]
scaler = bundle["scaler"]
feature_names = bundle["features"]

def predict_speed(features_dict):
    X_processed = preprocess_input(features_dict, feature_names, scaler)
    pred = model.predict(X_processed)
    return float(pred[0])
