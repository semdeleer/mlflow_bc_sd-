import pandas as pd
from sklearn.pipeline import Pipeline
import mlflow


from typing import Tuple

def train_model(pipeline:Pipeline, run_name:str, x:pd.DataFrame, y:pd.DataFrame)->Tuple[str, Pipeline]:
    with mlflow.start_run(run_name=run_name) as run:
        pipeline = pipeline.fit(x,y)
        mlflow.sklearn.log_model(pipeline, "model")
    return run.info.run_id, pipeline