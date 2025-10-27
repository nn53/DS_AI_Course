🟢 Assignment 8: Unsupervised Learning – K-Means & PCA

## 📚 Objective

* Apply **K-Means clustering** on the dataset.
* Visualize clusters in 2D using **PCA**.
* Add unsupervised analysis to support your project insights.

---

## 🛠️ Tools & Libraries

* **Python** 🐍
* `pandas` – for data handling 🗂️
* `scikit-learn` – for preprocessing, K-Means, PCA 🔧
* `matplotlib` & `seaborn` – for visualization 📊
* `tkinter` – for file selection 🖱️

---

## 🔹 Steps Taken

1. **Load Dataset**

   * CSV file is loaded using a file picker.
   * Columns names cleaned to remove extra spaces.

2. **Data Preprocessing**

   * Dropped unnecessary columns (`TransactionID`, `TransactionDate`).
   * Encoded categorical columns with `LabelEncoder`.
   * Filled missing numeric values with median.

3. **Feature Scaling**

   * Standardized all numeric features using `StandardScaler`.

4. **K-Means Clustering**

   * Determined optimal **k** using the **Elbow method**.
   * Fitted K-Means and assigned cluster labels to data.

5. **PCA Visualization**

   * Reduced features to **2 principal components**.
   * Visualized clusters in 2D using a scatter plot.

6. **Cluster Analysis**

   * Counted samples in each cluster.
   * Displayed cluster centers for insights.

---

## 📊 Results

* **Elbow Method** helped identify the optimal number of clusters.
* **Scatter plot with PCA** shows clear separation of clusters.
* Each cluster can be analyzed for patterns, anomalies, or group behavior.

---

## 🔍 Reflection

* Unsupervised clustering helps understand the structure of the data without relying on labels.
* PCA visualization makes it easier to **see patterns in high-dimensional data**.
* Clusters can be used for **anomaly detection** (e.g., possible fraud) or segmenting customers.

---

## ⚡ Key Takeaways

* K-Means is sensitive to feature scaling – always scale numeric data.
* PCA is very useful to **visualize high-dimensional data** in 2D or 3D.
* This analysis adds **unsupervised insights** to the project.

---

