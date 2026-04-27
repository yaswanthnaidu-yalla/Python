import pandas as pd
import joblib
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Literal
app = FastAPI(title="Customer Churn Prediction API")
try:
    model = joblib.load('churn_model.pkl')
except Exception as e:
    print(f"Error loading model: {e}")

class CustomerData(BaseModel):
    gender: Literal['Male', 'Female']
    Partner: Literal['Yes', 'No']
    Dependents: Literal['Yes', 'No']
    tenure: int
    PhoneService: Literal['Yes', 'No']
    MultipleLines: Literal['Yes', 'No', 'No phone service']
    InternetService: Literal['DSL', 'Fiber optic', 'No']
    OnlineSecurity: Literal['Yes', 'No', 'No internet service']
    OnlineBackup: Literal['Yes', 'No', 'No internet service']
    DeviceProtection: Literal['Yes', 'No', 'No internet service']
    TechSupport: Literal['Yes', 'No', 'No internet service']
    StreamingTV: Literal['Yes', 'No', 'No internet service']
    StreamingMovies: Literal['Yes', 'No', 'No internet service']
    Contract: Literal['Month-to-month', 'One year', 'Two year']
    PaperlessBilling: Literal['Yes', 'No']
    PaymentMethod: Literal['Electronic check', 'Mailed check', 'Bank transfer (automatic)', 'Credit card (automatic)']
    MonthlyCharges: float
    TotalCharges: float

def preprocess_input(data: CustomerData):
    df = pd.DataFrame([data.dict()])
    df['gender'] = df['gender'].map({'Male': 1, 'Female': 0})
    df['Partner'] = df['Partner'].map({'Yes': 1, 'No': 0})
    df['Dependents'] = df['Dependents'].map({'Yes': 1, 'No': 0})
    df['PhoneService'] = df['PhoneService'].map({'Yes': 1, 'No': 0})
    df['PaperlessBilling'] = df['PaperlessBilling'].map({'Yes': 1, 'No': 0})
    df['MultipleLines'] = df['MultipleLines'].replace('No phone service', 'No')
    expected_columns = [
        'gender', 'Partner', 'Dependents', 'tenure', 'PhoneService', 
        'PaperlessBilling', 'MonthlyCharges', 'TotalCharges',
        'MultipleLines_Yes', 
        'InternetService_Fiber optic', 'InternetService_No',
        'OnlineSecurity_No internet service', 'OnlineSecurity_Yes',
        'OnlineBackup_No internet service', 'OnlineBackup_Yes',
        'DeviceProtection_No internet service', 'DeviceProtection_Yes',
        'TechSupport_No internet service', 'TechSupport_Yes',
        'StreamingMovies_No internet service', 'StreamingMovies_Yes',
        'StreamingTV_No internet service', 'StreamingTV_Yes',
        'Contract_One year', 'Contract_Two year',
        'PaymentMethod_Credit card (automatic)', 'PaymentMethod_Electronic check', 'PaymentMethod_Mailed check'
    ]
    cat_cols = [
        'MultipleLines', 'InternetService', 'OnlineSecurity', 'OnlineBackup', 
        'DeviceProtection', 'TechSupport', 'StreamingMovies', 'StreamingTV', 
        'Contract', 'PaymentMethod'
    ]
    df_encoded = pd.get_dummies(df, columns=cat_cols)
    for col in expected_columns:
        if col not in df_encoded.columns:
            df_encoded[col] = 0
    return df_encoded[expected_columns]
@app.post("/predict")
async def predict_churn(customer: CustomerData):
    try:
        processed_df = preprocess_input(customer)
        prediction = model.predict(processed_df)[0]
        probability = model.predict_proba(processed_df)[0][1]
        
        return {
            "churn_prediction": "Yes" if prediction == 1 else "No",
            "churn_probability": round(float(probability), 4)
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)