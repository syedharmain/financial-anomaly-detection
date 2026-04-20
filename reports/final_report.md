# 📊 Financial Anomaly Detection Report

## 📌 Objective
The goal of this project is to detect fraudulent credit card transactions using unsupervised machine learning techniques.

---

## 📂 Dataset
- Source: Kaggle Credit Card Fraud Dataset  
- Highly imbalanced dataset  
- Fraud cases are very rare (~0.17%)

---

## ⚙️ Preprocessing
- Used **RobustScaler** for handling outliers
- Normalized transaction amounts
- Separated features and labels

---

## 🤖 Models Used

### 1. Isolation Forest
- Detects anomalies using random partitioning
- Works well with large datasets
- Fast and efficient

### 2. Local Outlier Factor (LOF)
- Measures local density deviation
- Slower compared to Isolation Forest

---

## 📈 Evaluation Metrics
- Precision
- Recall
- F1-score

---

## 📊 Results

- Isolation Forest performed better overall
- LOF was slower and less scalable

---

## 🧠 Conclusion

Isolation Forest is a robust and efficient method for detecting anomalies in financial transactions, especially for large and imbalanced datasets.

---

## 🚀 Future Improvements

- Add real-time detection system
- Deploy using Streamlit or Flask
- Improve threshold tuning
- Use deep learning models