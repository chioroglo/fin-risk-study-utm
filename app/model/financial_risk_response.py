from pydantic import BaseModel


class FinancialRiskResponse(BaseModel):
    audit_effectiveness_score: float