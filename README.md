# 🩺 Liver Disease Prediction App

A machine learning web application that predicts whether a patient is likely to have liver disease based on clinical parameters.

---

## 🚀 Live App
👉 https://liver-disease-app-rdoq.onrender.com

---

## 📌 Project Overview

This project uses patient clinical features such as bilirubin levels, liver enzyme values, proteins, and demographic data to predict liver disease using a trained machine learning model.

The application provides a simple and interactive interface where users can input patient details and instantly get prediction results.

---

## 🎯 Objective

- Build an end-to-end machine learning project  
- Perform data preprocessing and feature engineering  
- Train and evaluate multiple models  
- Deploy the best model using Streamlit  
- Make the app accessible via web  

---

## 🧠 Best Model

- **Random Forest (Tuned)**

---

## 📊 Features Used

- Age  
- Gender  
- Total Bilirubin  
- Direct Bilirubin  
- Alkaline Phosphotase  
- Alamine Aminotransferase  
- Aspartate Aminotransferase  
- Total Proteins  
- Albumin  
- Albumin and Globulin Ratio  

---

## 🛠️ Tech Stack

- Python  
- Streamlit  
- Pandas  
- NumPy  
- Scikit-learn  
- XGBoost  
- Imbalanced-learn (SMOTE)  
- Matplotlib  
- Seaborn  
- Joblib  

---

## 📂 Project Structure

liver-disease-prediction/
│
├── app.py
├── requirements.txt
├── .python-version
├── model/
│ ├── liver_model.pkl
│ ├── scaler.pkl
│ ├── feature_names.json
│ └── model_metadata.json
│
├── Data/
│ └── dataset.csv
│
└── notebook/
└── liver_patient_prediction.ipynb


---

## ▶️ Run Locally

### 1. Clone the repository
```bash
git clone https://github.com/uwaiszmuhammed07-hash/liver-disease-prediction.git
cd liver-disease-prediction

### 2. Create virtual environment


