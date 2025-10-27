# Assignment 3 - Data Visualization

## 📘 Course: Data Analytics
**Week 3**: Data Visualization

---

## 📊 Objective
The goal of this assignment is to perform **data visualization** using Python libraries such as **Matplotlib** and **Seaborn**.  
You will create multiple types of plots to understand and present insights from the dataset.

---

## 📂 Dataset
**File Name:** `creditcard_cleaned.csv`  
**Description:**  
This dataset contains transaction data with several features like `Time`, `Amount`, and various `V` features.  
The target variable `Class` indicates whether a transaction is **fraudulent (1)** or **non-fraudulent (0)**.

---

## 🧰 Libraries Used
- `pandas` – for data manipulation  
- `matplotlib.pyplot` – for basic plotting  
- `seaborn` – for advanced and aesthetic visualizations  

---

## 🧪 Tasks Performed
### 1️⃣ Bar Chart  
Visualizes the count of fraudulent vs non-fraudulent transactions.  
**Insight:** Helps to understand class imbalance in the dataset.

### 2️⃣ Histogram  
Shows the distribution of transaction amounts.  
**Insight:** Most transactions are of smaller amounts, while few are large.

### 3️⃣ Scatter Plot  
Plots `Time` vs `Amount` to observe transaction behavior over time.  
**Insight:** Certain time intervals have high-value transactions.

### 4️⃣ Box Plot  
Shows the spread and outliers of transaction amounts.  
**Insight:** Outliers indicate rare high-value transactions.

### 5️⃣ Correlation Heatmap  
Displays relationships between numerical features.  
**Insight:** Helps to identify which features are strongly correlated.

---

## 📈 Project Milestone
✅ **First Exploratory Data Analysis (EDA)** completed.  
This includes understanding data patterns, distributions, and relationships using visual techniques.

---

## 🧑‍💻 How to Run
1. Make sure `creditcard_cleaned.csv` is placed in the `Assignment_3` folder.  
2. Open the Jupyter Notebook:  
   ```bash
   jupyter notebook Assignment_3.ipynb