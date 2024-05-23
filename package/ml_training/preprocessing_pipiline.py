from sklearn.pipeline import Pipeline
from sklearn.tree import DecisionTreeClassifier
from imblearn.over_sampling import SMOTE
from imblearn.pipeline import Pipeline as ImbPipeline
from sklearn.pipeline import make_pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.neighbors import KNeighborsClassifier




def get_pipline(df, X_train, modelN) -> Pipeline:
    
    
    # Identifying categoricals and numericals
    categorical_cols = X_train.select_dtypes(include=['object', 'category']).columns
    numerical_cols = X_train.select_dtypes(exclude=['object', 'category']).columns

    # Numerical preprocessing
    numerical_pipeline = make_pipeline(
        SimpleImputer(strategy='mean'),
        StandardScaler()
    )

    # Categorical preprocessing
    categorical_pipeline = make_pipeline(
        OneHotEncoder(handle_unknown='ignore')
    )

    # ColumnTransformer 
    preprocessor = ColumnTransformer(
        transformers=[
            ('cat', categorical_pipeline, categorical_cols),
            ('num', numerical_pipeline, numerical_cols) 
        ],
        remainder='passthrough'
    )

    if modelN == "Tree":
        model = DecisionTreeClassifier()

        # A pipeline that includes the above
        pipe = ImbPipeline([
            ('preprocessor', preprocessor),
            ('smote', SMOTE(random_state=42)),
            ('DecisionTreeClassifier', model)
        ])

        return pipe
    else:
        model = KNeighborsClassifier()

        # A pipeline that includes the above
        pipe = ImbPipeline([
            ('preprocessor', preprocessor),
            ('smote', SMOTE(random_state=42)),
            ('KNN', model)
        ])

        return pipe

   