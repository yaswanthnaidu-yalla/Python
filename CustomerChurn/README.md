Telco Customer Churn Prediction

This project implements a machine learning pipeline to predict customer churn using the Telco dataset. It includes data preprocessing, model comparison, and a REST API for real-time predictions.
Problem Statement

    What is Churn?: Churn refers to the phenomenon where customers stop doing business with a company.

    Why it Matters: Predicting churn allows businesses to identify at-risk customers and implement retention strategies, which is often more cost-effective than acquiring new customers.

Dataset

    Source: Kaggle Telco Churn dataset.

    Size: 7,032 rows (after removing rows with missing TotalCharges).

    Class Imbalance: A significant imbalance was noted, with "No Churn" (5,163) significantly outnumbering "Yes Churn" (1,869).

Approach

    EDA: Analyzed distributions and correlations; found that newer customers and those with expensive monthly plans churn more frequently.

    Feature Engineering:

        Dropped customerID and SeniorCitizen (weak correlation).

        Encoded categorical variables using manual mapping and get_dummies.

        Scaled numerical features (tenure, MonthlyCharges, TotalCharges) using StandardScaler.

    Modeling: Compared Logistic Regression (LR), XGBoost (XGB) and Random Forest (RF) classifiers.

    API: Wrapped the final model in a FastAPI application for deployment.

Model Performance
Logistic Regression (LR)
Plaintext

              precision    recall  f1-score   support

           0       0.84      0.89      0.86      1033
           1       0.62      0.52      0.57       374

    accuracy                           0.79      1407

Random Forest (RF)
Plaintext

              precision    recall  f1-score   support

           0       0.82      0.91      0.86      1033
           1       0.64      0.45      0.53       374

    accuracy                           0.79      1407

XGBoost (XGB)
precision    recall  f1-score   support

           0       0.83      0.90      0.86      1033
           1       0.64      0.51      0.57       374

    accuracy                           0.79      1407

Chose Logistic regression as it has less false negatives meaning it will catch most of the customers who are about to churn.

How to Run

    Install Dependencies:
    Bash

    pip install fastapi uvicorn pandas scikit-learn joblib pydantic

    Start the Server:
    Bash

    uvicorn main:app --reload

    Test the API:
    Navigate to http://localhost:8000/docs to use the interactive Swagger UI and send test payloads to the /predict endpoint.

Tech Stack

    Language: Python

    Data Manipulation: pandas, NumPy

    Machine Learning: scikit-learn

    API Framework: FastAPI, uvicorn

    Model Serialization: joblib