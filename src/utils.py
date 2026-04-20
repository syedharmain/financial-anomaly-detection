def split_features_labels(df):
    X = df.drop('Class', axis=1)
    y = df['Class']
    return X, y