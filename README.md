💳 Financial Anomaly Detection (Fraud Detection)

📌 Overview

This project builds an end-to-end fraud detection system using unsupervised machine learning techniques to identify anomalous financial transactions.

---

🚀 Key Features

- Data preprocessing and feature scaling using RobustScaler
- Handling highly imbalanced dataset
- Anomaly detection using:
  - Isolation Forest
  - Local Outlier Factor (LOF)
- Model evaluation using precision, recall, and F1-score
- Model saving and loading using joblib

---

📁 Project Structure

- "data/" → raw and processed datasets
- "notebooks/" → step-by-step pipeline
- "models/" → saved trained models
- "src/" → production-ready scripts
- "reports/" → results and documentation

---

🛠 Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Jupyter Notebook

---

📊 Results

- Isolation Forest achieved better performance in detecting fraudulent transactions
- LOF was slower and less scalable on large datasets
- The project demonstrates practical anomaly detection on real-world financial data

---

🎯 Conclusion

Isolation Forest is a robust and efficient method for detecting anomalies in financial transactions.

---

✏️ How to Run

pip install -r requirements.txt

Run notebooks in order:

1. 01_eda_preprocessing.ipynb
2. 02_isolation_forest.ipynb
3. 03_lof_model.ipynb
4. 04_evaluation_threshold.ipynb

---

📂 Dataset

The dataset is not included in this repository due to size limitations.

You can download it from:
https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud

Place the file in:

data/raw/creditcard.csv