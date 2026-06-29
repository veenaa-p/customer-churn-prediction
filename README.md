# 🔄 Customer Churn Prediction

An end-to-end **Data Analytics and Machine Learning** project that predicts customer churn using the **Telco Customer Churn Dataset**. This project demonstrates the complete analytics workflow—from SQL-based business analysis and exploratory data analysis (EDA) to Machine Learning, Power BI dashboard development, and deployment with Streamlit.

---

# 📌 Project Overview

Customer churn is one of the biggest challenges faced by subscription-based businesses. Understanding why customers leave helps organizations improve customer retention and reduce revenue loss.

This project analyzes customer behavior, identifies churn patterns, and predicts whether a customer is likely to churn using a **Random Forest Classifier**.

---

# 🎯 Project Objectives

- Analyze customer churn trends using SQL.
- Perform Exploratory Data Analysis (EDA) using Python.
- Build and evaluate a Machine Learning classification model.
- Develop an interactive Power BI dashboard.
- Deploy a Streamlit web application for real-time customer churn prediction.

---

# 🛠️ Tech Stack

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- SQL (MySQL)
- Power BI
- Streamlit
- Joblib
---

# 📂 Project Structure

```text
customer-churn-prediction/
│
├── app/
│   ├── app.py
│   └── churn_model.pkl
│
├── data/
│   ├── raw/
│   ├── cleaned/
│   └── visuals/
│
├── notebooks/
│   ├── eda.ipynb
│   └── model.ipynb
│
├── powerbi/
│   └── churn_dashboard.pbix
│
├── sql/
│   └── queries.sql
│
├── requirements.txt
├── .gitignore
└── README.md
```
---

# 📊 SQL Analysis

SQL was used to analyze customer behavior and identify key business insights before building the machine learning model.

### SQL Queries Performed

- Overall Customer Churn Rate
- Churn by Contract Type
- Average Monthly Charges by Churn Status
- Churn by Tenure Group
- Top Payment Methods among Churned Customers

### Key Business Insights

- Overall churn rate: **26.58%**
- Customers with **Month-to-Month contracts** showed the highest churn.
- Customers with **higher monthly charges** were more likely to churn.
- Customers with **shorter tenure** exhibited significantly higher churn rates.
- **Electronic Check** was the most common payment method among churned customers.
---

# 📈 Exploratory Data Analysis (EDA)

Exploratory Data Analysis was performed to understand customer behavior and identify factors associated with churn.

### Visualizations Created

- Customer Churn Distribution
- Churn by Contract Type
- Monthly Charges vs Churn
- Tenure vs Churn
- Correlation Heatmap

### Key Findings

- Approximately **26.6%** of customers had churned.
- Customers with Month-to-Month contracts had the highest churn.
- Customers with higher monthly charges tended to churn more frequently.
- Customers with lower tenure were significantly more likely to leave.
- Correlation analysis highlighted relationships between customer demographics, subscribed services, and churn behavior.
