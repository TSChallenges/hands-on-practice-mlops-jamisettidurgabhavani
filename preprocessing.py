import pandas as pd
import numpy as np

# hello
def preprocess_data(input_path: str, output_path: str):
    """Loads data, cleans it, and saves the processed version."""
    df = pd.read_csv(input_path)

    # Handling missing values
    # ToDo

    # Handling categorical variables
    # ToDo

    # Save processed data
    # ToDo
if __name__ == "__main__":
    preprocess_data()
