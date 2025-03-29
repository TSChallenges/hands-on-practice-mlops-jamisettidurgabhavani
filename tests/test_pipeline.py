import os
import pandas as pd
import joblib
import pytest
from sklearn.metrics import accuracy_score

#from customer_churn_model import preprocess_data, train_model  # Assuming your main script is named customer_churn_model.py

def test_preprocessed_data():
    output_path = "data/processed_data.csv"
    
    # Check if the processed file exists
    assert os.path.exists(output_path), "Processed data file does not exist!"
    
    # Load processed data
    processed_df = pd.read_csv(output_path)
    
    # Check if there are no missing values
    assert processed_df.isnull().sum().sum() == 0, "Processed data contains null values!"

def test_model_accuracy():
    model_path = "models/model.pkl"
    
    # Check if the model file exists
    assert os.path.exists(model_path), "Model file does not exist!"
    
    # Load trained model
    model_dict = joblib.load(model_path)
    model = model_dict['model']
    
    # Load processed data
    data = pd.read_csv("data/processed_data.csv")
    X_test = data.drop(columns=['Exited'])
    y_test = data['Exited']
    
    # Apply the saved scaler before predicting
    scaler = model_dict['scaler']
    X_test = scaler.transform(X_test)

    # Evaluate model on the dataset
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)

    
    # Check if accuracy is above 60%
    assert accuracy >= 0.6, f"Model accuracy is too low: {accuracy:.2f}"
