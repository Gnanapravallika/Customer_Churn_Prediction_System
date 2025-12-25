from fastapi import FastAPI
from api.schemas import CustomerInput
from api.utils import make_prediction
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Customer Churn Prediction API",
    description="Predict customer churn using ML",
    version="1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],         
    allow_methods=["*"],         
    allow_headers=["*"],
)

@app.get("/")
def health_check():
    return {"status": "API is running"}


@app.post("/predict")
def predict_churn(customer: CustomerInput):
    result = make_prediction(customer.dict())
    return result
