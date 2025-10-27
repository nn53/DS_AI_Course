🟡 Assignment 1: Orientation & Setup

## 📚 Objective

* Set up the data science environment.
* Load and explore a sample dataset.
* Upload your work to **GitHub** for version control.

---

## 🛠️ Tools & Libraries

* **Python** 🐍
* **Pandas** – for data manipulation 🗂️
* **Jupyter Notebook / Google Colab** – for executing code 💻
* **GitHub** – for repository and version control 🌐

---

## 🔹 Steps Taken

1. **Setup Environment**

   * Installed Python via Anaconda / used Google Colab.
   * Created a **GitHub account** and repository for assignments.

2. **Download Dataset**

   * Downloaded the Titanic dataset from **Kaggle**:
     [Titanic: Machine Learning from Disaster](https://www.kaggle.com/c/titanic/data)
   * Saved the `train.csv` file to the local machine.

3. **Load Dataset**

   * Loaded the CSV file using `pandas`:

```python
import pandas as pd

# Load the dataset
df = pd.read_csv("train.csv") 

# Show first 10 rows
df.head(10)
```

4. **Exploration**

   * Displayed the **first 10 rows** to understand the dataset structure.
   * Observed columns like `PassengerId`, `Survived`, `Pclass`, `Name`, `Sex`, `Age`, etc.

5. **GitHub Upload**

   * Uploaded the Jupyter Notebook with the code and outputs to the repository.

---

## 📊 Results

* Successfully loaded the Titanic dataset.
* The first 10 rows were displayed, showing initial structure and values.

---

## ⚡ Key Takeaways

* Setting up the environment is the first step in any data science project.
* **Pandas** makes it easy to load and explore datasets.
* Using **GitHub** ensures version control and safe storage of assignments.
* Datasets from **Kaggle** can be easily downloaded and used for practice and assignments.

---

