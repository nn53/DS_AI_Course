🧮 Assignment 5 – Supervised Learning: Regression

## 🎯 Objective

The aim of this assignment is to **understand and implement Linear Regression**, one of the most basic yet powerful supervised learning algorithms.
You’ll split your dataset into training and testing sets, train a regression model, and evaluate it using **Mean Absolute Error (MAE)** and **Root Mean Squared Error (RMSE)**.

---

## 📊 Dataset

The dataset used is the **Credit Card Transactions Dataset**, which includes:

* 💳 `TransactionID`
* ⏰ `TransactionDate`
* 💰 `Amount`
* 🏪 `MerchantID`
* 🔁 `TransactionType`
* 📍 `Location`
* ⚠️ `IsFraud` (Target variable for fraud detection)

For regression analysis, numerical columns were used — such as predicting the **Amount** or analyzing relationships between features and fraud probability.

---

## 🧠 Tasks Performed

### 1️⃣ Data Loading & Cleaning

* Loaded the dataset using `pandas`.
* Removed duplicates and handled missing values.
* Encoded categorical variables if needed.

### 2️⃣ Feature Selection

* Defined `X` (independent variables) and `y` (target variable).

### 3️⃣ Train/Test Split

* Split dataset using `train_test_split` → 80% training / 20% testing.

### 4️⃣ Model Implementation

* Used **`LinearRegression()`** from `scikit-learn` to train the model.

### 5️⃣ Evaluation Metrics

* Calculated performance metrics:

  * 📉 **Mean Absolute Error (MAE)**
  * 📈 **Root Mean Squared Error (RMSE)**
* Compared results to check model accuracy and error spread.

---

## 📋 Results

✅ The Linear Regression model successfully fitted the dataset.
✅ Calculated **MAE** and **RMSE** to measure accuracy.
✅ Results serve as a **baseline regression model** for further improvement.

---

## 🧰 Tools & Libraries Used

* 🐍 **Python 3.x**
* 🧾 **pandas** – Data manipulation
* 🔢 **numpy** – Numerical operations
* 📊 **matplotlib** & **seaborn** – Visualization
* 🤖 **scikit-learn** – Machine learning algorithms

---

## ⚙️ How to Run

1. Install the required libraries:

   ```bash
   pip install pandas numpy matplotlib seaborn scikit-learn
   ```

2. Run the script or notebook:

   ```bash
   python Assignment5_Regression.py
   ```

   or open in Jupyter Notebook:

   ```bash
   jupyter notebook Assignment5_Regression.ipynb
   ```

---

## 🧾 Conclusion

Through this assignment, I learned how to:

* Build and train a **Linear Regression** model 👩‍💻
* Split data for model evaluation 🔍
* Use **MAE** and **RMSE** for regression performance comparison 📈

✨ This marks the completion of **Milestone 5: Building the first baseline regression model**!

---