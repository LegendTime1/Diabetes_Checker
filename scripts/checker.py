#CONTAINS FUNCTION WHICH PREDICTS WHETHER PERSON IS DIABETIC OR NOT

import pandas as pd
import numpy as np
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split


def predict_diabetes(age, serum_insulin):
    df = pd.read_csv('Diabetes_Pima.csv')
    df = df.drop('Patient ID', axis=1)
    Diabetes = df['Diabetes']
    df = df.drop('Diabetes', axis=1)
    mean_values = df.mean(skipna=True).to_dict()
    df = df.fillna(mean_values)
    df = df[['Serum Ins', 'Age']]
    df['Diabetes'] = Diabetes

    X_diabetes = df[['Age', 'Serum Ins']]
    y_diabetes = df['Diabetes']

    model = GaussianNB()
    model.fit(X_diabetes, y_diabetes)  # Use the full dataset for training

    y_model = model.predict([[age, serum_insulin]])

    return y_model[0]

# Example usage:
#age_input = 40
#serum_insulin_input = 180
#prediction = predict_diabetes(age_input, serum_insulin_input)

#print(prediction)
