import pandas as pd

from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from typing import Dict

from api.schemas import ClaimInput

from models.train import train_pipeline
from models.predict import predict_claims

import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)
logger = logging.getLogger(__name__)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health():
    return {"status": "ok"}


trained_pipeline = None

@app.on_event("startup")
def startup_event():
    global trained_pipeline

    logger.info("Starting application and training pipeline")

    df = pd.read_csv("C:/Users/Sam/Documents/GitHub/insurance-risk-scoring/data/raw/labeled_insurance.csv")
    X = df.drop(columns=["claims_count"])
    y = df["claims_count"]

    trained_pipeline = train_pipeline(X, y)

    logger.info("Pipeline trained and ready")


@app.post("/predict")
def predict(input_data: ClaimInput):
    try:
        logger.info(f"Received prediction request: {input_data.dict()}")

        prediction = predict_claims(trained_pipeline, input_data.dict())

        logger.info(f"Prediction result: {prediction}")

        return {"claims_count": prediction}

    except Exception as e:
        logger.exception("Prediction failed")
        raise HTTPException(
            status_code=500,
            detail="Internal server error during prediction",
        )
