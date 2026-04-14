#pandas handle tabular data, like data in databases or spreadsheets
#pandas help explore,clean,process data.
#data table in pandas is dataframe
#pandas supports the integration with many file formats or data sources out of the box (csv, excel, sql, json, parquet,…). The ability to import data from each of these data sources is provided by functions with the prefix, read_*. Similarly, the to_* methods are used to store data.
#questinos to answer 1-how many rows and colums. 2-names and datatypes. 3-any missing values. 4- how many yes no in churn column
import numpy as np
import pandas as pd
telco_churn  = pd.read_csv("data/telco_churn.csv")
#fo rfirst question-
print(telco_churn.info())
#answer-7043 rows and 21 columns
#2nd question-
print(telco_churn.columns)
#Index(['customerID', 'gender', 'SeniorCitizen', 'Partner', 'Dependents',
#      'tenure', 'PhoneService', 'MultipleLines', 'InternetService',
#      'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport',
#      'StreamingTV', 'StreamingMovies', 'Contract', 'PaperlessBilling',
#      'PaymentMethod', 'MonthlyCharges', 'TotalCharges', 'Churn'],
#     dtype='str') 
# 3rd question
telco_churn.replace("", np.nan, inplace=True)

telco_churn['TotalCharges']=pd.to_numeric(telco_churn["TotalCharges"], errors='coerce')
print(telco_churn.isna().sum().sum())
#11
#4th question
print(telco_churn["Churn"].value_counts())

#No     5174
#Yes    1869
#dropping useless rows 
telco_churn=telco_churn.dropna()
print(telco_churn.info())