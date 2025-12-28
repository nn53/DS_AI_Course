🟢 **Assignment 10: Advanced Deep Learning (Enhanced ANN)** – Credit Card Fraud Detection

## 📚 Objective

* Build a **more advanced Artificial Neural Network (ANN)** to detect credit card fraud.
* Evaluate the ANN using **classification metrics** and **ROC-AUC**.
* Apply a **specialized AI model** suitable for tabular data.

> ⚠️ *Note:* CNN/RNN are not applied because the dataset is **tabular**, not images or sequences. Instead, a deeper ANN is used.

---

## 🛠️ Tools & Libraries

* **Python** 🐍
* `pandas` – data handling 🗂️
* `scikit-learn` – preprocessing, scaling, and ANN (`MLPClassifier`) 🔧
* `matplotlib` & `seaborn` – visualization 📊
* `tkinter` – file selection 🖱️

---

## 🔹 Steps Taken

1. **Load Dataset**

   * CSV file loaded using a **file picker**.
   * Verified dataset shape and class distribution.

2. **Data Preprocessing**

   * Dropped unnecessary columns (`TransactionID`, `TransactionDate`).
   * Separated **features (X)** and **target (y)**.
   * Train-test split (80:20) with stratification for class balance.

3. **Feature Scaling**

   * Standardized features using `StandardScaler` – critical for ANN performance.

4. **Advanced ANN – `MLPClassifier`**

   * 3 hidden layers `(64,32,16)` with **ReLU activation**.
   * Trained for **300 iterations** to improve learning.
   * This serves as a **specialized AI model for tabular data**.

5. **Evaluation**

   * Predictions on test set.
   * Calculated **classification report**, **ROC-AUC**, and **confusion matrix**.
   * Compared metrics with baseline ANN and earlier models (Logistic Regression / Random Forest).

---

## 📊 Results

* Advanced ANN captures **non-linear patterns** better than baseline models.
* ROC-AUC improved, showing better fraud detection capability.
* Confusion matrix visualizes correct and incorrect predictions.
* Serves as a **baseline for deep learning on tabular fraud data**.

---

## 🔍 Reflection

* MLPClassifier works well for **tabular datasets** where CNN/RNN are not applicable.
* Feature scaling is essential for neural networks.
* ROC-AUC is a better metric than accuracy due to class imbalance.
* Advanced ANN provides **stronger insights and model performance** than baseline ANN.

---

## ⚡ Key Takeaways

* Advanced ANN = **deeper network, more neurons, higher iterations**.
* Specialized AI model is applied even though CNN/RNN are not suitable.
* Ready to compare with previous ML models for final project milestone.
* Can be **further improved** with hyperparameter tuning (layers, neurons, iterations).

