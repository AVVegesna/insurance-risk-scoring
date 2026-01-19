from models.pipeline_def import get_pipeline

def train_pipeline(X, y):
    pipeline = get_pipeline()
    pipeline.fit(X, y)
    return pipeline
