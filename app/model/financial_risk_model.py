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
    audit_Effectiveness_Score: float
    client_Satisfaction_Score: float