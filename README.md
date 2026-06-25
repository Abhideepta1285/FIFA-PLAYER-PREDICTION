# ⚽ FIFA Player Performance Classification

A Machine Learning project that predicts whether a FIFA World Cup player is a **High Performer** based on match statistics, physical attributes, and performance metrics.

---

## 📌 Project Overview

This project uses Machine Learning classification algorithms to analyze FIFA World Cup player data and predict player performance.

The dataset contains player statistics such as:

- Goals
- Assists
- Shots
- Pass Accuracy
- Tackles
- Interceptions
- Distance Covered
- Stamina Score
- Team Information
- Tournament Stage
- And many more features

---

## 🎯 Objective

To classify players into:

- **High Performer (1)**
- **Not High Performer (0)**

using Machine Learning techniques.

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-Learn
- Streamlit
- Joblib

---

## 📂 Project Workflow

### 1. Data Collection

Dataset downloaded from Kaggle.

### 2. Data Cleaning

- Removed ID columns
- Removed data leakage columns
- Removed future tournament statistics
- Handled categorical features using One-Hot Encoding

### 3. Exploratory Data Analysis (EDA)

- Missing Value Analysis
- Correlation Analysis
- Feature Engineering
- Multicollinearity Detection

### 4. Feature Scaling

Used:

```python
StandardScaler()
```

### 5. Model Training

The following models were trained and compared:

- Logistic Regression
- K-Nearest Neighbors (KNN)
- Decision Tree
- Random Forest
- Support Vector Machine (Linear SVM)

---

## 📊 Model Performance

| Model | Accuracy |
|---------|---------|
| SVM | 91.81% |
| Random Forest | 91.80% |
| Logistic Regression | 91.67% |
| Decision Tree | 86.18% |
| KNN | 75.82% |

### Best Model

**Linear SVM**

- Accuracy: 91.81%
- Precision: 85.91%
- Recall: 100%
- F1 Score: 92.42%

---

## 🚀 Streamlit Application

The project includes a Streamlit web application where users can:

- Enter player statistics
- Select team and opponent
- Provide match information
- Predict player performance

Run locally:

```bash
streamlit run app.py
```

---

## 📁 Project Structure

```text
FIFA-Player-Performance-Classification/
│
├── app.py
├── FIFA_Player_Performance.ipynb
├── fifa_cleaned.csv
├── model.pkl
├── scaler.pkl
├── features.pkl
├── feature_means.pkl
├── README.md
└── .gitignore
```

---

## 📷 Screenshots

Add screenshots of:

- EDA
- Model Comparison
- Streamlit App

---


## 👨‍💻 Author

**Abhideepta**

MCA Student | Machine Learning & Data Science Enthusiast

GitHub: https://github.com/Abhideepta1285
