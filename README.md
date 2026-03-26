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

```
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
```


---
## 🚀 How to Run Locally

### Step 1 — Clone the Repository
```bash
git clone https://github.com/uwaiszmuhammed07-hash/liver-disease-prediction.git
cd liver-disease-prediction
```

### Step 2 — Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate        
```

### Step 3 — Install Requirements
```bash
pip install -r requirements.txt
```

### Step 4 — Run the App
```bash
streamlit run app.py
```

### Step 5 — Open in Browser
```
http://localhost:8501
```






📈 Output

The application predicts:

✅ No Liver Disease
⚠️ Liver Disease Detected

It also shows:

Prediction probability
Input summary

📈 Key Insights
-SMOTE improved class balance significantly
-Random Forest handled feature interactions better
-Feature importance showed bilirubin & enzymes as key indicators
-Scaling improved performance for certain models

⚠️ Disclaimer

This project is for educational purposes only.
It is not a substitute for professional medical advice.

##👨‍💻 Author

Uwais Muhammed KP
GitHub**
[![GitHub](https://img.shields.io/badge/GitHub-uwaiszmuhammed07--hash-black?logo=github)](https://github.com/uwaiszmuhammed07-hash)
---




