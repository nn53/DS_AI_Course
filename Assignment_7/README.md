📊 Assignment 7: Model Evaluation – Credit Card Fraud Detection

## 📚 Overview

This assignment focuses on **evaluating machine learning classification models** for detecting fraudulent credit card transactions.

Two models are trained:

1. 🤖 **Logistic Regression**
2. 🌲 **Random Forest**

We evaluate these models using **accuracy, precision, recall, F1-score, confusion matrix, and ROC-AUC curves**.

---

## 🗂 Dataset

* File: selected via a file picker (`askopenfilename`)
* Contains numerical and categorical features for credit card transactions
* The **target column** is assumed to be the **last column** in the dataset, representing:

  * `0` → Legitimate transaction ✅
  * `1` → Fraudulent transaction ⚠️

---

## ⚙️ Steps Performed

### 1️⃣ Data Preprocessing

* **Drop non-useful columns**:

  * `TransactionID`, `TransactionDate` (if present)
* **Handle missing values**:

  * Numeric columns → filled with median
  * Categorical columns → filled with mode
* **Encode categorical columns** using `LabelEncoder` 🔢
* **Feature-target split**:

  * `X` → all columns except target
  * `y` → target column
* **Train-test split**:

  * 80% training, 20% testing 🏋️‍♂️

---

### 2️⃣ Model Training

* **Logistic Regression**:

  * Trained with `max_iter=1000`
* **Random Forest**:

  * Trained with 100 estimators 🌳

---

### 3️⃣ Model Evaluation

* **Confusion Matrix** 🧮:

  * Visualizes predicted vs actual classes for both models
* **Classification Metrics** 📄:

  * Precision: fraction of correctly predicted frauds among all predicted frauds
  * Recall: fraction of actual frauds correctly detected
  * F1-score: harmonic mean of precision and recall
* **ROC Curve & AUC** 📈:

  * Measures model’s ability to distinguish between classes

---

## 📊 Key Functions

* `plot_confusion_matrix(y_true, y_pred, title)` → plots heatmap for predictions
* `print_metrics(y_true, y_pred, model_name)` → prints precision, recall, F1-score
* `plot_roc_curve(model, X_test, y_test, model_name)` → plots ROC curve and AUC

---

## 📈 Results

* Confusion matrices and classification metrics are generated for **both models**.
* ROC curves with **AUC scores** visualize model performance.
* ⚖️ Comparison helps determine which model best identifies fraudulent transactions.

---

## 🔑 Observations

* Random Forest tends to perform better in identifying fraud due to ensemble learning 🌲
* Logistic Regression is interpretable but may miss complex patterns 🤖
* **Recall** is particularly important in fraud detection to minimize missed fraudulent transactions
* F1-score balances Precision and Recall for overall model quality

---

## 🛠 Libraries Used

* `pandas` – data handling 🐼
* `scikit-learn` – preprocessing, model training, and evaluation 🤖🌲
* `seaborn` & `matplotlib` – visualization 📊
* `tkinter` – file selection GUI 🖱️

---

## ▶️ How to Run

1. Run the Python script or Jupyter Notebook
2. Select the CSV dataset using the file picker 🗂️
3. The script will preprocess data, train models, and display metrics and visualizations

---