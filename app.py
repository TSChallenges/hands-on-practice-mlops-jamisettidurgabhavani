
# ADD YOUR CODE HERE to create API endpoint using FastAPI to do prediction with the model


from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import pandas as pd

# Load the trained model
model = joblib.load('models/my_model.pkl')

app = FastAPI()

# Define the request body
class CustomerData(BaseModel):
    CreditScore: int
    Geography: int
    Gender: int
    Age: int
    Tenure: int
    Balance: float
    NumOfProducts: int
    IsActiveMember: int
    EstimatedSalary: float

# API endpoint for prediction
@app.post("/predict/")
def predict(data: CustomerData):
    try:
        # Convert data to DataFrame
        input_data = pd.DataFrame([data.dict()])
        
        # Predict
        prediction = model.predict(input_data)[0]
        
        # Return the prediction
        return {"Exited": prediction}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Run using: uvicorn app:app --reload
