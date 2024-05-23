from sklearn.model_selection import train_test_split
import pandas as pd

def get_train_test_set(df: pd.DataFrame):
    x_train, x_test, y_train, y_test= train_test_split(
        df.drop('Attrition_Flag', axis=1), df['Attrition_Flag'], test_size=0.3, random_state=42
    )

    return x_train, x_test, y_train, y_test
