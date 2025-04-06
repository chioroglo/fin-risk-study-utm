import pandas as pd
from pydantic import BaseModel, Field
from typing import Literal

class FinancialRiskModel(BaseModel):
    year: int
    firm_Name: Literal['PwC', 'Deloitte', 'Ernst & Young', 'KPMG']
    total_Audit_Engagements: int
    high_Risk_Cases: int
    compliance_Violations: int
    fraud_Cases_Detected: int
    industry_Affected: Literal['Healthcare', 'Finance', 'Retail', 'Tech']
    total_Revenue_Impact: float
    AI_Used_for_Auditing: Literal["Yes", "No"]
    employee_Workload: float
    client_Satisfaction_Score: float

    def to_ready_input_dataframe(self) -> pd.DataFrame:
        industry_means = pd.read_csv('../resources/Industry_Affected_target_means.csv', index_col=0)
        # Prepare the data dictionary
        data = {
            'Total_Audit_Engagements': [self.total_Audit_Engagements],
            'High_Risk_Cases': [self.high_Risk_Cases],
            'Compliance_Violations': [self.compliance_Violations],
            'Fraud_Cases_Detected': [self.fraud_Cases_Detected],
            'Industry_Affected': [self.industry_Affected],
            'Total_Revenue_Impact': [self.total_Revenue_Impact],
            'AI_Used_for_Auditing': [1 if self.AI_Used_for_Auditing == "Yes" else 0],
            'Employee_Workload': [self.employee_Workload],
            'Client_Satisfaction_Score': [self.client_Satisfaction_Score]
        }
        print(data["Industry_Affected"])
        print(industry_means)
        data['Industry_Affected'] = industry_means.loc[self.industry_Affected, 'Audit_Effectiveness_Score']
        
        # Convert dictionary to DataFrame
        return pd.DataFrame(data)