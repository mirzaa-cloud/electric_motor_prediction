# Electric Motor Speed Predictor

Modular machine learning pipeline for electric motor speed prediction with a FastAPI backend and Streamlit frontend.

## Folder structure

      motor_speed_predictor/
      ├── backend/
      │   ├── main.py
      │   ├── model/
      │   │   └── motor_speed_model.pkl
      │   ├── preprocessing/
      │   │   └── pipeline.py
      │   ├── predictor.py
      │   ├── schemas.py
      │   └── requirements.txt
      ├── frontend/
      │   ├── app.py
      │   └── requirements.txt

## Usage

1. Place your trained model pickle in `backend/model/motor_speed_model.pkl`

py 3.10 -m venv mynv

2. Start FastAPI backend:  
   `uvicorn backend.main:app --reload`

3. Start Streamlit frontend:  
   `streamlit run frontend/app.py`

The frontend UI lets users enter sensor features and receive predicted motor speed from the backend.


cd path\to\motor_speed_predictor
py 3.10 -m venv mynv
.\mynv\Scripts\Activate
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
# [in new PowerShell window]
cd path\to\motor_speed_predictor
.\mynv\Scripts\Activate
cd frontend
pip install -r requirements.txt
streamlit run app.py
