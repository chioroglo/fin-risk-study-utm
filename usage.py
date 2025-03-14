import joblib
import pandas as pd
import numpy as np

# Load the saved model and scaler
model = joblib.load('model.pkl')
scaler = joblib.load('scaler.pkl')

# Load the target mean encoding CSV files for Firm_Name and Industry_Affected
firm_name_means = pd.read_csv('Firm_Name_target_means.csv', index_col=0)
industry_means = pd.read_csv('Industry_Affected_target_means.csv', index_col=0)
print(firm_name_means)
print(industry_means)

# Define the new input data
new_data = pd.DataFrame({
    'Total_Audit_Engagements': [4784],
    'High_Risk_Cases': [382],
    'Compliance_Violations': [15],
    'Fraud_Cases_Detected': [73],
    'Industry_Affected': ['Healthcare'],
    'Total_Revenue_Impact': [268.67],
    'AI_Used_for_Auditing': [0],  # 'No' -> 0 (as per your original mapping)
    'Employee_Workload': [59],
    'Audit_Effectiveness_Score': [6.7]
})

# Target Mean Encoding for Firm_Name and Industry_Affected
# Apply Firm_Name encoding using the target mean from the CSV
new_data['Firm_Name_Encoded'] = new_data['Firm_Name'].map(firm_name_means['Client_Satisfaction_Score'])
# Apply Industry_Affected encoding using the target mean from the CSV
new_data['Industry_Affected_Encoded'] = new_data['Industry_Affected'].map(industry_means['Client_Satisfaction_Score'])

# Drop the original categorical columns after encoding
new_data = new_data.drop(['Firm_Name', 'Industry_Affected'], axis=1)

# Prepare features for prediction by selecting the columns that the model expects
X_new = new_data

# Normalize the new input data using the previously fitted scaler
X_new_scaled = scaler.transform(X_new)

# Make the prediction using the loaded model
predicted_client_satisfaction = model.predict(X_new_scaled)

# Output the predicted value
print(f"Predicted Client Satisfaction Score: {predicted_client_satisfaction[0]:.2f}")
