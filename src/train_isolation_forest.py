from sklearn.ensemble import IsolationForest
import joblib

def train_model(X):
    model = IsolationForest(contamination=0.001, random_state=42)
    model.fit(X)
    return model

def save_model(model, path):
    joblib.dump(model, path)