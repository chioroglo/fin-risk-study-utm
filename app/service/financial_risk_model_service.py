import os
import joblib
import pandas as pd

from model.financial_risk_model import FinancialRiskModel


class FinancialRiskModelService:
    def __init__(self) -> None:
        self.model = joblib.load(os.getenv('JOBLIB_MODEL_PATH'))
        self.scaler = joblib.load(os.getenv('JOBLIB_SCALER_PATH'))
    
    def predict_audit_effectiveness_score(self,request_model: FinancialRiskModel) -> str: 
        dataframe_model_request = request_model.to_ready_input_dataframe()
        feature_values_from_model = dataframe_model_request.iloc[0].values
        scaled_values_from_dto = self.scaler.transform([feature_values_from_model])
        result = self.model.predict(scaled_values_from_dto)
        print(result)
        return result