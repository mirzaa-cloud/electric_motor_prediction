from fastapi import FastAPI
from .schemas import MotorSpeedFeatures
from .predictor import predict_speed

app = FastAPI(title="Electric Motor Speed Predictor API")

@app.post("/predict")
def predict(features: MotorSpeedFeatures):
    input_data = features.dict()
    pred = predict_speed(input_data)
    return {"predicted_motor_speed": pred}
