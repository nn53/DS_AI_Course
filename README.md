# Data Science & AI Course

This repository contains my complete work for the **Data Science & AI** course, covering all stages of the data science workflow — from data collection to model deployment. Each task contributed to building my final machine learning project based on my assigned topic.

---

## Project Title

**Credit Card Fraud Detection** *(example — replace with your actual project based on your roll number)*

---

## Project Workflow

### 1. Data Loading & Exploration

* Imported the dataset using **Pandas** and displayed the first few rows to understand its structure.
* Checked data types, column names, and overall dataset shape.
* Performed initial data exploration using `.info()` and `.describe()` to understand the statistical summary of features.

### 2. Data Cleaning

* Removed **duplicate entries** and handled **missing values** appropriately using mode or mean imputation.
* Treated **outliers** by applying statistical methods (e.g., IQR or z-score).
* Verified the dataset’s consistency after cleaning by comparing “before vs after” summaries.

### 3. Exploratory Data Analysis (EDA) & Visualization

* Visualized the data using **Matplotlib** and **Seaborn** to identify patterns and trends.
* Created **bar plots**, **scatter plots**, **histograms**, and **correlation heatmaps**.
* Analyzed feature relationships and detected which attributes were most correlated with the target variable.

### 4. Statistical Analysis

* Calculated **mean, median, mode, variance, and correlation** for numerical features.
* Conducted correlation analysis to determine which top three variables strongly influence the target outcome.

### 5. Model Building – Regression

* Implemented **Linear Regression** as a baseline model for numeric prediction tasks.
* Split the dataset into training and testing sets using **train_test_split**.
* Evaluated results using **Mean Absolute Error (MAE)** and **Root Mean Squared Error (RMSE)** to measure accuracy.

### 6. Model Building – Classification

* Applied **Logistic Regression** and **Random Forest Classifier** to perform classification.
* Compared both models’ performance using **accuracy** and selected the better-performing one.
* Generated a **confusion matrix** to visualize true/false positives and negatives.

### 7. Model Evaluation

* Evaluated model performance using **Precision, Recall, and F1 Score** to gain deeper insight into model accuracy.
* Plotted the **ROC Curve** and calculated the **AUC score** to assess classification quality.
* Identified which metric was most relevant for my project (e.g., Recall for fraud detection since missing a fraud case is costlier than a false alarm).

### 8. Unsupervised Learning

* Applied **K-Means Clustering** to explore natural groupings within the dataset.
* Used **Principal Component Analysis (PCA)** for dimensionality reduction and plotted the data in 2D space.
* Compared clusters with existing labels to analyze similarities and hidden patterns.

---

## Tools & Libraries Used

* **Python**
* **Pandas**, **NumPy**
* **Matplotlib**, **Seaborn**
* **Scikit-Learn**
* **Jupyter Notebook / Google Colab**
* **GitHub** for version control

---

## Summary

Throughout this course, I learned to:

* Handle real-world datasets and perform complete preprocessing.
* Apply both **supervised and unsupervised machine learning** techniques.
* Evaluate models using professional metrics like **Precision, Recall, F1 Score, and ROC-AUC**.
* Interpret results and decide which evaluation metric best suits the project goal.

This repository reflects my step-by-step journey from data preparation to model evaluation in a full **Data Science + AI pipeline**.

---