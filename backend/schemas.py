from pydantic import BaseModel

class MotorSpeedFeatures(BaseModel):
    ambient: float
    coolant: float
    u_d: float
    u_q: float
    i_d: float
    i_q: float
    pm: float
    stator_yoke: float
    stator_tooth: float
    stator_winding: float
    torque: float
