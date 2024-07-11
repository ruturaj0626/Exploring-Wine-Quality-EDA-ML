#data_proessing.py
import pandas as pd
from sklearn.preprocessing import StandardScaler
import numpy as np

def preprocess_data(df):
    
    # Scale numerical features
    scaler = StandardScaler()
    numerical_features = ['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar',
       'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density',
       'pH', 'sulphates', 'alcohol']
    df[numerical_features] = scaler.fit_transform(df[numerical_features])
    
    return df