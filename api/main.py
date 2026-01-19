import pandas as pd

from fastapi import FastAPI
from fastapi import Request

from typing import Dict

from models.train import train_pipeline
from models.predict import predict_claims

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}


trained_pipeline = None

@app.on_event("startup")
def startup_event():
    global trained_pipeline

    df = pd.read_csv("C:/Users/Sam/Documents/GitHub/insurance-risk-scoring/data/raw/labeled_insurance.csv")
    X = df.drop(columns=["claims_count"])
    y = df["claims_count"]

    trained_pipeline = train_pipeline(X, y)


@app.post("/predict")
async def predict(input_data: Dict):
    """
    Accepts JSON input with keys: age, tenure, vehicle_type, claims_history
    Returns predicted claims_count
    """

    prediction = predict_claims(trained_pipeline, input_data)
    return {"claims_count": prediction}