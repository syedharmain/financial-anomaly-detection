import pandas as pd
from sklearn.preprocessing import RobustScaler

def load_data(path):
    return pd.read_csv(path)

def preprocess_data(df):
    scaler = RobustScaler()
    df['Amount'] = scaler.fit_transform(df[['Amount']])
    return df