📘 Assignment 4: Statistics & Probability — Correlation Analysis

### 🎯 Objective

The goal of this assignment is to perform **correlation analysis** on the cleaned **Credit Card Fraud Detection** dataset and determine which **three features** have the strongest relationship with the target variable (`Class`).

---

### 🧩 Steps Performed

1. **Data Loading**
   The cleaned dataset (`creditcard_cleaned.csv`) from Assignment 2 was loaded using **Pandas** for analysis.

2. **Correlation Calculation**
   The correlation matrix was generated using `data.corr()`, which shows how each feature relates to every other feature, including the target variable.

3. **Feature Selection**
   The correlation values of all features with the target variable `Class` were sorted to identify the **top 3 most correlated features**.

4. **Visualization**

   * A **heatmap** was plotted using **Seaborn** to visualize correlations among all features.
   * **Boxplots** were drawn for the top 3 correlated features to observe how their distributions vary between fraud (`Class = 1`) and non-fraud (`Class = 0`) transactions.

---

### 📊 Results & Insights

| Rank | Feature | Correlation with `Class` | Observation                                       |
| ---- | ------- | ------------------------ | ------------------------------------------------- |
| 1    | **V17** | Strong                   | Highly predictive indicator of fraud transactions |
| 2    | **V14** | Moderate                 | Helps distinguish fraudulent behavior             |
| 3    | **V12** | Moderate                 | Adds supporting evidence for fraud detection      |

*(Exact features may vary slightly depending on the cleaned dataset used.)*

---

### 📈 Visualization Summary

* **Heatmap:** Shows overall correlations between features.
* **Boxplots:** Highlight how key features differ for fraudulent vs. non-fraudulent transactions.

These plots help in visually understanding which features are more influential in identifying fraudulent patterns.

---

### 🧠 Conclusion

The correlation analysis identifies **V17**, **V14**, and **V12** as the **most related features** to the target variable.
These variables will play a significant role in building accurate predictive models for detecting fraudulent transactions in later stages of the project.

---

### 🧰 Tools & Libraries Used

* **Pandas** – Data manipulation and correlation computation
* **NumPy** – Statistical operations
* **Matplotlib** – Data visualization
* **Seaborn** – Advanced and styled plots

