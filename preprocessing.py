
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score

def preprocess_data(input_path: str, output_path: str):
    """Loads data, cleans it, and saves the processed version."""
    df = pd.read_csv(input_path)
    
    # Drop Customer ID column if present
    if 'CustomerID' in df.columns:
        df.drop(columns=['CustomerID'], inplace=True)
    
    # Handling missing values
    df.fillna(df.median(numeric_only=True), inplace=True)
    
    # Handling categorical variables
    label_encoders = {}
    for col in df.select_dtypes(include=['object']).columns:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])
        label_encoders[col] = le
    
    # Save processed data
    df.to_csv(output_path, index=False)
    print(f'Processed data saved to {output_path}')

if __name__ == "__main__":
    preprocess_data("data/customer_churn.csv", "data/processed_data.csv")
