from sklearn.neighbors import LocalOutlierFactor
import joblib

def train_lof(X):
    model = LocalOutlierFactor(
        n_neighbors=20,
        contamination=0.001,
        novelty=True
    )

    model.fit(X)
    joblib.dump(model, 'models/lof_model.pkl')
    return model