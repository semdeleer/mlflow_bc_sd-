import pandas as pd

def load_data(filepath):
    df = pd.read_csv(filepath)
    return df

#df = load_data('../data/BankChurners.csv')

def clean_df(df):
    df = df[df.columns[:-2]]
    df = df.drop(['CLIENTNUM'], axis=1)
    return df

#df = clean_df(df)

