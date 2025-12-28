🟢 Assignment 13: Model Deployment – Credit Card Fraud Detection

## 📚 Objective
* Deploy trained ANN as a **Flask API** for real-time fraud prediction.
* Complete the **end-to-end pipeline** from data → model → deployment.

## 🔹 Steps Taken
1. Trained advanced ANN from Assignment 10.
2. Saved **model and scaler** in `deployment/` folder.
3. Created **Flask API** with:
   - `/` → health check
         The scaler file (scaler.pkl) is a binary file created using joblib.
         It stores the fitted scaling parameters and cannot be opened in a text editor.
         It is loaded programmatically in Python to ensure consistent preprocessing during prediction and explainability.

   - `/predict` → fraud prediction with probability
4. Tested API locally using sample transaction data.

## 📊 Project Milestone
* End-to-end pipeline working: Data → Preprocessing → ANN → Prediction API.

## 🔍 Reflection
* API deployment allows integration with real-world apps (e.g., banking systems).
* Can be extended to cloud deployment (Heroku, AWS) for production use.