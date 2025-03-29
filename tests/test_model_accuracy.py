import joblib
import pandas as pd
from sklearn.metrics import accuracy_score
import pytest

# Load the trained model
model = joblib.load('models/my_model.pkl')

# Test data
test_data = pd.DataFrame({
    'CreditScore': [600, 700],
    'Geography': [2, 1],
    'Gender': [1, 0],
    'Age': [45, 30],
    'Tenure': [5, 1],
    'Balance': [15000, 3000],
    'NumOfProducts': [2, 1],
    'IsActiveMember': [1, 0],
    'EstimatedSalary': [50000, 30000]
})

# Actual labels
actual_labels = [0, 1]

# Predict
predictions = model.predict(test_data)

# Accuracy
accuracy = accuracy_score(actual_labels, predictions)

# Test case
def test_model_accuracy():
    assert accuracy > 0.8, f"Model accuracy is {accuracy}, which is less than 0.8"

if __name__ == "__main__":
    pytest.main()
