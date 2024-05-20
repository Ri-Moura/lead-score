import joblib
import uvicorn
import pandas as pd

from scripts import models
from typing import List, Dict, Any
from fastapi import FastAPI, HTTPException
from sklearn.preprocessing import StandardScaler


model = joblib.load('./weights/xgb_model.pkl')
scaler = joblib.load('./weights/scaler.pkl')
expected_columns = joblib.load('./weights/expected_columns.pkl')

app = FastAPI()

def preprocess_input(data: pd.DataFrame, scaler: StandardScaler, expected_columns: List[str]) -> pd.DataFrame:
    """
    Preprocess the input data to ensure it matches the format expected by the model.

    Parameters:
    - data (pd.DataFrame): The input data as a pandas DataFrame.
    - scaler (StandardScaler): The scaler object used for scaling the features.
    - expected_columns (List[str]): List of columns expected by the model.

    Returns:
    - pd.DataFrame: The preprocessed and scaled data.
    """
    data_dropped = data.dropna()

    data_dropped['Visits_PageViews_Interaction'] = data_dropped['TotalVisits'] * data_dropped['Page_Views_Per_Visit']

    data_dropped['High_Time_Spent'] = data_dropped['Total_Time_Spent_on_Website'] > 1000

    country_visits_avg = data_dropped.groupby('Country')['TotalVisits'].transform('mean')
    data_dropped['Country_Visits_Avg'] = country_visits_avg

    data_dropped['Source_Activity'] = data_dropped['Lead_Source'] + '_' + data_dropped['Last_Activity']

    data_dropped['High_Time_Spent'] = data_dropped['High_Time_Spent'].astype(int)

    if 'Prospect_ID' in data_dropped.columns:
        data_for_encoding = data_dropped.drop(columns=['Prospect_ID'])
    else:
        data_for_encoding = data_dropped

    data_encoded = pd.get_dummies(data_for_encoding, drop_first=True)

    missing_cols = list(set(expected_columns) - set(data_encoded.columns))
    missing_df = pd.DataFrame(0, index=data_encoded.index, columns=missing_cols)
    data_encoded = pd.concat([data_encoded, missing_df], axis=1)

    data_encoded = data_encoded[expected_columns]

    data_scaled = scaler.transform(data_encoded)

    return data_scaled

@app.post("/predict")
def predict(lead_data: models.LeadData) -> Dict[str, Any]:
    """
    Predict the probability of lead conversion based on the input data.

    Parameters:
    - lead_data (LeadData): The input data as a LeadData model.

    Returns:
    - Dict[str, Any]: A dictionary containing the predictions.
    """
    data_dict = lead_data.dict()
    input_data = pd.DataFrame(data_dict)
    
    try:
        input_data_scaled = preprocess_input(input_data, scaler, expected_columns)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error in preprocessing input data: {e}")

    try:
        predictions = model.predict_proba(input_data_scaled)[:, 1]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error in making predictions: {e}")

    return {"predictions": predictions.tolist()}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)