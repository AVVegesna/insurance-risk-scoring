import pandas as pd

from fastapi import FastAPI
from models.train import train_pipeline
import pandas as pd

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
