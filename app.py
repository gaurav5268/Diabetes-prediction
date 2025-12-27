from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np

app = Flask(__name__)

model = joblib.load("ml_model.pkl")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    data = request.json

    preg = float(data["Pregnancies"])
    glucose = float(data["Glucose"])
    bp = float(data["BloodPressure"])
    skin = float(data["SkinThickness"])
    insulin = float(data["Insulin"])
    bmi = float(data["BMI"])
    dpf = float(data["DiabetesPedigreeFunction"])
    age = float(data["Age"])

    # ---- Feature engineering ----

    if age < 25: age_group = "<25"
    elif age < 35: age_group = "25-35"
    elif age < 45: age_group = "35-45"
    elif age < 60: age_group = "45-60"
    else: age_group = "60+"

    if bmi < 18.5: bmi_cat = "Under"
    elif bmi < 25: bmi_cat = "Normal"
    elif bmi < 30: bmi_cat = "Over"
    else: bmi_cat = "Obese"

    if glucose < 99: glu_risk = "Normal"
    elif glucose < 125: glu_risk = "Prediabetes"
    else: glu_risk = "Diabetes"

    bmi_age = bmi * age
    glu_preg = glucose * preg
    dpf_scaled = dpf * 100

    feature_dict = {

        "Pregnancies": preg,
        "Glucose": glucose,
        "BloodPressure": bp,
        "SkinThickness": skin,
        "Insulin": insulin,
        "BMI": bmi,
        "DiabetesPedigreeFunction": dpf,
        "Age": age,

        "BMI*Age": bmi_age,
        "Glucose*Preg": glu_preg,
        "DPF_Scaled": dpf_scaled,

        "Age_Group_25-35": 1 if age_group=="25-35" else 0,
        "Age_Group_35-45": 1 if age_group=="35-45" else 0,
        "Age_Group_45-60": 1 if age_group=="45-60" else 0,
        "Age_Group_60+":   1 if age_group=="60+"   else 0,

        "BMI_Category_Normal": 1 if bmi_cat=="Normal" else 0,
        "BMI_Category_Over":   1 if bmi_cat=="Over"   else 0,
        "BMI_Category_Obese":  1 if bmi_cat=="Obese"  else 0,

        "Glucose_Risk_Prediabetes": 1 if glu_risk=="Prediabetes" else 0,
        "Glucose_Risk_Diabetes":    1 if glu_risk=="Diabetes"    else 0,
    }

    features = np.array([list(feature_dict.values())])

    prob = model.predict_proba(features)[0][1]

    THRESHOLD = 0.2
    pred = int(prob >= THRESHOLD)

    return jsonify({
        "prediction": pred,
        "probability": round(prob,3),
        "threshold": THRESHOLD
    })


if __name__ == "__main__":
    app.run(debug=True)
