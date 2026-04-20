from sklearn.ensemble import IsolationForest
import joblib

def train_isolation_forest(X):
    model = IsolationForest(
        n_estimators=100,
        contamination=0.001,
        random_state=42
    )

    model.fit(X)
    joblib.dump(model, 'models/isolation_forest.pkl')
    return model