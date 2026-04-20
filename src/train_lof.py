from sklearn.neighbors import LocalOutlierFactor

def train_lof(X):
    model = LocalOutlierFactor(n_neighbors=20, contamination=0.001)
    y_pred = model.fit_predict(X)
    return y_pred