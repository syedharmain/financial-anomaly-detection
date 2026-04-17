💳 Financial Anomaly Detection (Fraud Detection)

📌 Overview

This project detects fraudulent credit card transactions using unsupervised machine learning techniques.

🚀 Key Features

- Data preprocessing and feature scaling using RobustScaler
- Handling highly imbalanced dataset
- Anomaly detection using:
  - Isolation Forest
  - Local Outlier Factor (LOF)
- Model evaluation using precision, recall, and F1-score
- Model saving and loading using joblib

📂 Project Structure

- data/ → raw and processed datasets
- notebooks/ → step-by-step pipeline
- models/ → saved trained models
- src/ → production-ready scripts
- reports/ → results and documentation

⚙️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Jupyter Notebook

📊 Results

- Isolation Forest performed better for fraud detection
- LOF was slower and less scalable

🎯 Conclusion

Isolation Forest is a robust and efficient method for detecting anomalies in financial transactions.

🧪 How to Run

pip install -r requirements.txt

Run notebooks in order:

1. 01_eda_preprocessing.ipynb
2. 02_isolation_forest.ipynb
3. 03_lof_model.ipynb
4. 04_evaluation_threshold.ipynb

---