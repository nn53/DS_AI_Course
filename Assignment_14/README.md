# 📝 Assignment 14: Ethics & Explainability – Credit Card Fraud Detection

## 🎯 Objective

* Explain predictions of your ML model using **SHAP**.
* Understand **why a transaction is flagged as fraud or not**.
* Add an **“Explainability”** section to your project report.

---

## 🛠️ Tools & Libraries

* **Python** 🐍
* `pandas` – data handling 🗂️
* `joblib` – load saved model & scaler 🔧
* `shap` – interpret ML predictions 👁️
* `matplotlib` – visualization 📊

---

## 🔹 Steps Taken

1️⃣ Load Model & Scaler

2️⃣ Load Dataset

3️⃣ Create SHAP Explainer

4️⃣ Explain a Transaction

5️⃣ Optional: Summary Plot for Multiple Transactions


## 📊 Results

* Each bar shows how much a feature contributes to **fraud probability**.
* Positive bars → increase likelihood of fraud.
* Negative bars → decrease likelihood of fraud.
* Summary plot highlights **most important features across multiple transactions**.

---

## 🔍 Reflection

* SHAP helps **interpret black-box models** (MLP, Random Forest, etc.).
* Adds **ethics and transparency** to AI by showing why a model made a decision.
* Useful for **fraud investigation, audits, or compliance**.

---

## ⚡ Key Takeaways

* Always scale numeric data before explainability.
* Use **Kernel SHAP** for any model, **Tree SHAP** for tree-based models (faster).
* Explainability is essential for **trustworthy AI**.
