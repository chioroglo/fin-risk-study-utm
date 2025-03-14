import joblib
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt


def analyse_model(model: LinearRegression, feature_names: list[str]):
    coefficients = model.coef_
    print(feature_names)
    print(coefficients)

    coef_df = pd.DataFrame({
        'Feature': feature_names,
        'Coefficient': coefficients,
        'Absolute Value': np.abs(coefficients)
    })

        # Sort the coefficients by value in descending order
    coef_df = coef_df.sort_values(by='Absolute Value', ascending=True)
    colors = ['green' if coef > 0 else 'red' for coef in coef_df['Coefficient']]

    # Plot the coefficients as a bar graph
    plt.figure(figsize=(12, 8))
    plt.barh(coef_df['Feature'], coef_df['Absolute Value'], color=colors)
    plt.xlabel('Coefficient Value')
    plt.ylabel('Feature')
    plt.title('Feature Coefficient Impact (Ordered Descending)')
    plt.show()
