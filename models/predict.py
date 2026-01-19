import pandas as pd

def predict_claims(pipeline, input_data: dict) -> int:
    """
    Predict claims count using a trained pipeline.
    """
    df = pd.DataFrame([input_data])
    prediction = pipeline.predict(df)
    return int(prediction[0])
