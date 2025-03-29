import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score

def train_model(data_path: str, model_path: str):
    """Loads processed data, trains a model, and saves it."""
    # Load the data
    data = pd.read_csv(data_path)
    
    # Split data into features and target
    X = data.drop(columns=['Exited'])  # Assuming 'Churn' is the target variable
    y = data['Exited']
    
    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Standardize features
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)
    
    # Train a logistic regression model
    model = LogisticRegression()
    model.fit(X_train, y_train)
    
    # Evaluate model
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    print(f'Model Accuracy: {accuracy:.4f}')
    print(f'Model F1 Score: {f1:.4f}')
    
    # Save model
    joblib.dump({'model': model, 'scaler': scaler}, model_path)
    print(f'Model saved to {model_path}')

if __name__ == "__main__":
    train_model("data/processed_data.csv", "models/model.pkl")
