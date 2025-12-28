🟢 **Assignment 9: Neural Network (ANN Baseline)** – Credit Card Fraud Detection

## 📚 Objective

* Build a **simple Artificial Neural Network (ANN)** to detect credit card fraud.
* Evaluate the ANN using **classification metrics** and **ROC-AUC**.
* Compare results with earlier models (Logistic Regression, Random Forest).

---

## 🛠️ Tools & Libraries

* **Python** 🐍
* `pandas` – for data handling 🗂️
* `scikit-learn` – for preprocessing, scaling, and ANN (`MLPClassifier`) 🔧
* `matplotlib` & `seaborn` – for visualization 📊
* `tkinter` – for file selection 🖱️

---

## 🔹 Steps Taken

1. **Load Dataset**

   * CSV file loaded using a file picker for flexibility.
   * Displayed dataset info and class distribution.

2. **Data Preprocessing**

   * Dropped unnecessary columns (`TransactionID`, `TransactionDate`).
   * Separated **features (X)** and **target (y)**.
   * Train-test split (80:20) with stratification to maintain class balance.

3. **Feature Scaling**

   * Standardized features using `StandardScaler` for ANN training.

4. **ANN Model – `MLPClassifier`**

   * 2 hidden layers `(32,16)` with **ReLU activation**.
   * Trained model for 100 iterations.
   * Avoided TensorFlow – fully compatible with Python 3.14.

5. **Evaluation**

   * Predicted on test set and calculated metrics:

     * Classification report
     * ROC-AUC score
     * Confusion matrix visualization
   * Compared results with previous models (Logistic Regression / Random Forest).

---

## 📊 Results

* ANN successfully learned non-linear patterns in data.
* ROC-AUC indicates strong ability to detect fraud.
* Confusion matrix shows correct and incorrect predictions across classes.
* ANN can be used as a **baseline neural network model** for further tuning.

---

## 🔍 Reflection

* `MLPClassifier` allows building an ANN **without TensorFlow**, solving compatibility issues with Python 3.14.
* Feature scaling is critical for neural network convergence.
* ROC-AUC is more meaningful than accuracy due to class imbalance.
* ANN provides another perspective on fraud detection compared to linear models.

---

## ⚡ Key Takeaways

* Neural networks can capture **complex, non-linear relationships** in data.
* Scaling and preprocessing are mandatory for good ANN performance.
* This ANN serves as a **baseline**; future improvements could include deeper layers, more neurons, or tuning hyperparameters.
* Ready for **comparison with previous supervised models** to complete your project milestone.

---
