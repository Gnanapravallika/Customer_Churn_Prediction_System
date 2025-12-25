import joblib
import pandas as pd
from config import MODEL_PATH

model=joblib.load(MODEL_PATH)


def predict_churn(input_dict:dict):
    df = pd. DataFrame([input_dict])
    prediction = model.predict(df)[0]
    probability = model.predict_proba(df)[0][1]

    return {
        "churn_prediction": int(prediction),
        "churn_probability": float(probability)
    }