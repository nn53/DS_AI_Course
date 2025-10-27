📚 Overview

This assignment implements **supervised machine learning models** to detect **fraudulent credit card transactions**. Two classification algorithms are applied:

1. 🤖 **Logistic Regression**
2. 🌲 **Random Forest**

The models are evaluated for **accuracy** and **classification performance**.

---

## 🗂 Dataset

* File: `creditcard_cleaned.csv`
* Features: numerical & categorical transaction data
* Target column: `Class`

  * `0` → Legitimate transaction ✅
  * `1` → Fraudulent transaction ⚠️

---

## ⚙️ Steps Performed

### 1️⃣ Data Preprocessing

* **Missing values**:

  * Numeric columns → filled with **median**
  * Categorical columns → filled with **mode**
* **Encoding**:

  * Categorical columns converted to numeric using `LabelEncoder` 🔢
* **Feature-target split**:

  * `X` → all features except `Class`
  * `y` → target column `Class`
* **Train-test split**:

  * 80% training, 20% testing 🏋️‍♂️
  * `random_state=42` for reproducibility

### 2️⃣ Model Training

* **Logistic Regression**:

  * Trained using `LogisticRegression(max_iter=1000)`
* **Random Forest**:

  * Trained using `RandomForestClassifier(n_estimators=100)` 🌳

### 3️⃣ Model Evaluation

* **Accuracy** ✅
* **Classification Report** 📄: Precision, Recall, F1-score
* **Confusion Matrix** 🧮 for Random Forest

---

## 📊 Results

| Model                  | Accuracy |
| ---------------------- | -------- |
| 🤖 Logistic Regression | 0.XXXX   |
| 🌲 Random Forest       | 0.XXXX   |

> Replace `0.XXXX` with your actual results

* 🌲 Random Forest generally performs better for detecting fraud due to its ensemble learning.

---

## 🔑 Key Observations

* Logistic Regression: simple & interpretable, may miss complex patterns
* Random Forest: handles non-linear relationships well, higher accuracy
* Confusion matrix & classification report provide deeper insights than accuracy alone

---

## 🛠 Libraries Used

* `pandas` – data handling 🐼
* `numpy` – numerical operations 🔢
* `scikit-learn` – preprocessing & model training 🤖🌲
* `seaborn` & `matplotlib` – visualization 📊

---

## ▶️ How to Run

1. Place `creditcard_cleaned.csv` in your project folder 📂
2. Open the notebook or Python script 📝
3. Run all cells sequentially ▶️
4. Visualizations (confusion matrix, classification report) will display 📈

---