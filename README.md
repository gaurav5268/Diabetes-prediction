# Diabetes Prediction Machine Learning Project

A Machine Learning–based web application that predicts the probability of Diabetes
using patient health parameters such as Glucose level, BMI, Insulin, Age, etc.

The project includes:

✔ End-to-end ML pipeline  
✔ Feature Engineering  
✔ Model Training & Hyperparameter Tuning  
✔ Threshold Optimization (Recall-Focused)  
✔ MLflow Experiment Tracking  
✔ Flask API Deployment  
✔ Docker Support  
✔ Frontend UI with live inference  

---

## Live Demo

🔗 **App URL**  
[ https://diabetes-prediction-laim.onrender.com/ ]

---

## Problem Statement

Early prediction of diabetes can help:

- Reduce severe complications  
- Improve treatment planning  
- Support medical diagnosis

This project predicts whether a person is:

🟢 Non-Diabetic  
🔴 Diabetic (High Risk)

The model is optimized to **increase Recall**, ensuring fewer false negatives.

---

## Dataset

Dataset — PIMA Indians Diabetes Dataset

Features used:

| Feature | Description |
|--------|----------|
| Pregnancies | Number of pregnancies |
| Glucose | Plasma glucose concentration |
| BloodPressure | Diastolic blood pressure |
| SkinThickness | Triceps skin fold thickness |
| Insulin | Serum insulin |
| BMI | Body Mass Index |
| DiabetesPedigreeFunction | Genetic risk score |
| Age | Age in years |

Additional engineered features:

- Age Group Buckets  
- BMI Risk Category  
- Glucose Risk Category  
- BMI × Age Interaction  
- Glucose × Pregnancy Interaction  
- DPF Scaled Feature  

---

## Machine Learning Model Development & Selection
- Step 1 — Trained Multiple Base Models

The project started by training and evaluating multiple baseline machine learning models:

        Model	Description
        Logistic Regression	Simple & interpretable baseline
        KNN	Distance-based learner
        Decision Tree	Rule-based classifier
        Random Forest	Bagging ensemble
        Gradient Boosting	Sequential boosting
        XGBoost	Optimized gradient boosting
        LightGBM	Fast & memory-efficient boosting
        SVM	Margin-based classifier

All models were evaluated using:

        Accuracy

        Recall (priority metric)

        F1-Score

        Cross-Validation score

Step 2 — Shortlisted Top Performing Models

        After evaluation of all base models, the top 3 performers were shortlisted:

        Selected Model	Reason
        Random Forest	Strong baseline & robust
        Gradient Boosting	Good generalization
        LightGBM	Best recall & stability

        These were further improved using:

        Hyperparameter tuning

        Cross-validation

        Threshold tuning

## Step 3 — Business / Medical Objective

        Diabetes prediction is a health-risk classification problem.

        In real healthcare:

        ⚠ Missing a diabetic patient (False Negative)
        is more dangerous than giving an early alert (False Positive)

        Therefore, the project prioritizes:

            ✔ Higher Recall (catch risk cases)
            ✔ Lower False Negatives
            ✔ Early-risk detection

hreshold Optimization

Instead of using the default threshold 0.50,
multiple probability thresholds were tested:

0.20 → 0.25 → 0.30 → 0.35 → 0.40 → 0.50


The goal was to find a balance between:

    Recall (medical safety)

    Accuracy

F1 Score

Threshold = 0.20 gave the best medical value

It helps:

    ✔ Detect more potential diabetic cases early
    ✔ Reduce false-negative risk
    ✔ Improve recall while keeping accuracy acceptable''

Final Selected Model
- Final Model   : LightGBM Classifier
- Selection Base: Recall + Stability + Performance
- Threshold     : 0.20
- Decision Rule : Predict Diabetic if Probability ≥ 0.20

## Why LightGBM was chosen

- Best Recall performance

- Consistent results across runs

- Works well with engineered features

- Fast inference suitable for deployment

- Better handling of feature interactions

## Tech Stack

**Languages**
- Python

**Machine Learning**
- Scikit-Learn
- LightGBM
- Random Forest
- Gradient Boosting

**Experiment Tracking**
- MLflow

**Deployment**
- Flask API
- HTML + CSS + JS Frontend
- Docker Support

---

## Project Architecture

```
data/
models/
 └── ml_model.pkl
notebooks/
src/
app.py
static/
templates/
README.md
requirements.txt
Dockerfile
```

---

## Installation & Setup

### 🔹 1️ Create Virtual Environment

```bash
python -m venv ml_env
source ml_env/Scripts/activate   # Windows
```

---

### 🔹 2️ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 🔹 3️ Run Flask App

```bash
python app.py
```

App runs on:

```
http://127.0.0.1:5000
```

---

## Model Training Summary

Base models tested:

- Logistic Regression
- Random Forest
- Gradient Boosting
- LightGBM
- XGBoost
- SVM
- KNN

Threshold tuning performed to maximize Recall.

**Best Performing Model**

✔ LightGBM  
✔ Recall-optimized  
✔ Threshold = 0.2  

---

## 🧾 API Usage

### 🔹 Endpoint

```
POST /predict
```

### 🔹 Sample Request

```json
{
  "Pregnancies": 2,
  "Glucose": 155,
  "BloodPressure": 82,
  "SkinThickness": 32,
  "Insulin": 140,
  "BMI": 33.2,
  "DiabetesPedigreeFunction": 0.65,
  "Age": 45
}
```

### 🔹 Sample Response

```json
{
  "prediction": 1,
  "probability": 0.82,
  "threshold": 0.2,
  "result": "Diabetic"
}
```


---

**Gaurav Chauhan**  