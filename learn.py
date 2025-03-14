import joblib
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Load the CSV file
df = pd.read_csv('big4_financial_risk_compliance.csv')

# We have no control over a year, so drop it as an unnecesary fact
df = df.drop(columns=['Year'])

# We should drop firm_name column, because keeping it won't cover cases
# Of newly incoming firms since new company name isn't represented
# in training group
df = df.drop(columns=['Firm_Name'])

# Convert AI_Used_for_Auditing to binary flag
df['AI_Used_for_Auditing'] = df['AI_Used_for_Auditing'].map({'Yes': 1, 'No': 0})

# Target Mean Encoding Function
def target_mean_encoding(data, col, target):
    """
    Encodes a categorical column using target mean encoding.
    """
    mean_encoded = data.groupby(col)[target].mean()
    return data[col].map(mean_encoded)

# Apply Target Mean Encoding to categorical columns
for col in ['Industry_Affected']:
    # Calculate target mean for each category
    mean_encoded = df.groupby(col)['Client_Satisfaction_Score'].mean()
    
    # Save the means to a CSV file
    mean_encoded.to_csv(f'{col}_target_means.csv', header=True)
    
    # Apply target mean encoding to the dataset
    df[f'{col}_Encoded'] = target_mean_encoding(df, col, 'Client_Satisfaction_Score')

# Drop original categorical columns after encoding
df = df.drop(['Industry_Affected'], axis=1)

# Separate features and target variable
X = df.drop('Client_Satisfaction_Score', axis=1)
y = df['Client_Satisfaction_Score']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Normalize numerical features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Create and train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict and evaluate
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f'Mean Squared Error: {mse}')
print(f'R-squared: {r2}')

# Save model and scaler
joblib.dump(model, "model.pkl")
joblib.dump(scaler, "scaler.pkl")

