from package.feature.data_processing import load_data, clean_df
from package.ml_training.retrieval import get_train_test_set
from package.ml_training.preprocessing_pipiline import get_pipline
from package.ml_training.train import train_model
from package.utils.utils import set_or_create_experiment, get_performance_plots, get_classification_metrics
import mlflow

def experiments(experiment_name:str, run_name:str, filepath:str, modelname:str):
    experiment_name = experiment_name
    run_name = run_name
    df = load_data(filepath)
    df = clean_df(df)

    X_train, X_test, y_train, y_test = get_train_test_set(df)

    pipeline = get_pipline(df, X_train, modelname)

    experiment_id = set_or_create_experiment(experiment_name=experiment_name)

    run_id, model = train_model(pipeline=pipeline, run_name=run_name, x=X_train, y=y_train)

    y_pred = model.predict(X_test)
    y_prob = model.predict_proba(X_test)[:, 1]  # Get probabilities for the positive class

    classification_metrics = get_classification_metrics(
        y_true=y_test, y_pred=y_pred, y_prob=y_prob, prefix="test", pos_label='Attrited Customer'
    )

    with mlflow.start_run(run_id=run_id):
        # log metrics
        mlflow.log_metrics(classification_metrics)

        # log params
        mlflow.log_params(model[-1].get_params())

        # log tags
        mlflow.set_tags({"type": "classifier"})

        # log description
        mlflow.set_tag(
            "mlflow.note.content", "this is the churn data"
        )

if __name__ == '__main__':
    
    experiments("bankChirners", "decisionTree", "./package/data/BankChurners.csv", "Tree")
    experiments("bankChirners", "KNN", "./package/data/BankChurners.csv", "KNN")
