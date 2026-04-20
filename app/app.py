import pandas as pd
import joblib

from src.preprocessing import load_data, preprocess_data
from src.utils import convert_labels
from src.evaluate import evaluate_model

# Load data
df = load_data('data/raw/creditcard.csv')

# Preprocess
df = preprocess_data(df)

# Split features & labels
X = df.drop('Class', axis=1)
y = df['Class']

# Load models
iso_model = joblib.load('models/isolation_forest.pkl')
lof_model = joblib.load('models/lof_model.pkl')

# Predictions
iso_pred = iso_model.predict(X)
lof_pred = lof_model.predict(X)

# Convert predictions
iso_pred = convert_labels(iso_pred)
lof_pred = convert_labels(lof_pred)

# Evaluate
print("Isolation Forest Results:")
evaluate_model(y, iso_pred)

print("\nLOF Results:")
evaluate_model(y, lof_pred)