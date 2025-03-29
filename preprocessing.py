
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
    preprocess_data("Raw data path", "path to store processed data")
