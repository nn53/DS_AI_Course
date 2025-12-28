import joblib
from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

# Load model and scaler
model = joblib.load('model.pkl')
scaler = joblib.load('scaler.pkl')

@app.route('/')
def home():
    return "Credit Card Fraud Detection API is running!"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        df = pd.DataFrame([data])
        X_scaled = scaler.transform(df)
        prediction = model.predict(X_scaled)[0]
        probability = model.predict_proba(X_scaled)[0,1]
        return jsonify({'prediction': int(prediction), 'fraud_probability': float(probability)})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == "__main__":
    app.run(debug=True)