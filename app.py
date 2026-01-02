from flask import Flask, request, jsonify,render_template
from flask_cors import CORS
import numpy as np
import pickle

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return render_template("index.html")

# ================= LOAD TRAINED ARTIFACTS =================
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

# ================= DECISION RULE =================
def decision_action(prob):
    if prob >= 0.6:
        return "Auto-Approve"
    elif prob >= 0.3:
        return "Manual Review"
    else:
        return "Reject"

# ================= INFERENCE ENDPOINT =================
@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json(force=True)

    X = np.array([[
        float(data["no_of_dependents"]),
        float(data["income_annum"]),
        float(data["loan_amount"]),
        float(data["loan_term"]),
        float(data["cibil_score"]),
        float(data["residential_assets_value"]),
        float(data["luxury_assets_value"])
    ]])

    X_scaled = scaler.transform(X)

    proba = model.predict_proba(X_scaled)[0]
    class_index = list(model.classes_).index(1)  # Approved = 1
    prob = float(proba[class_index])

    return jsonify({
        "approval_probability": prob,
        "decision": decision_action(prob)
    })

if __name__ == "__main__":
    app.run(debug=True)