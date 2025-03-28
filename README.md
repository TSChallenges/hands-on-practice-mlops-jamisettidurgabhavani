# Assignment-6
## CI/CD Pipeline for Customer Churn data using GitHub Actions / gitlab

##  Project Overview  
This Hands-on implements a **CI/CD pipeline using GitHub Actions** to process **Customer Churn data** and train a machine learning model 

The pipeline includes:  
- **Data Preprocessing**: Cleaning & transforming raw data.  
- **Model Training**: Training a classification model.  
- **Automated Testing**: Using `pytest` for test cases.  
- **CI/CD Integration**: Automating workflow using GitHub Actions.  


#### Column Description:
The dataset you'll be working with is a customer dataset from a **Credit Card company**, which includes the following features:


- **RowNumber:** corresponds to the record (row) number and has no effect on the output.
- **CustomerId:** contains random values and has no effect on customer leaving the bank.
- **Surname:** the surname of a customer has no impact on their decision to leave the bank.
- **CreditScore:** can have an effect on customer churn, since a customer with a higher credit score is less likely to leave the bank.
- **Geography:** a customer’s location can affect their decision to leave the bank.
- **Gender:** it’s interesting to explore whether gender plays a role in a customer leaving the bank.
- **Age:** this is certainly relevant, since older customers are less likely to leave their bank than younger ones.
- **Tenure:** refers to the number of years that the customer has been a client of the bank. Normally, older clients are more loyal and less likely to leave a bank.
- **Balance:** also a very good indicator of customer churn, as people with a higher balance in their accounts are less likely to leave the bank compared to those with lower balances.
- **NumOfProducts:** refers to the number of products that a customer has purchased through the bank.
- **HasCrCard:** denotes whether or not a customer has a credit card. This column is also relevant, since people with a credit card are less likely to leave the bank.
- **IsActiveMember:** active customers are less likely to leave the bank.
- **EstimatedSalary:** as with balance, people with lower salaries are more likely to leave the bank compared to those with higher salaries.
- **Exited:** whether or not the customer left the bank. (0=No,1=Yes)

---
 
## Assignment Tasks

**1. Understanding the given files**

You are provided with the following:
* **Dataset (`data/customer_churn.csv`)**: Required for preprocessing and model training.
* **Preprocessing script (`preprocessing.py`)**: Cleans and prepares the data.
* **Model training script (`train_model.py`)**: Trains and saves a machine learning model.
* **Test scripts (`tests/test_pipeline.py`)**: Validates the preprocessing and model performance.

**2. Setting Up the CI/CD Pipeline**

You need to create a GitHub Actions workflow to automate the ML pipeline when code is pushed to the main branch or a pull request is made.

**Steps to Include in ml_pipeline.yml**
* Trigger the Workflow: Run the pipeline on push and pull requests to the main branch.
* Set Up the Environment: Use Ubuntu-latest as the runner.
* Setup Python 3.8 and install required dependencies (pandas, numpy, scikit-learn, pytest).
* **Run Preprocessing**: Execute `preprocessing.py` to clean and transform the dataset.
* **Train the Model**: Run `train_model.py` to train and save the model.
* **Run Test Cases**: Use `pytest` to verify correctness.

**3. Implementing the Workflow**

You need to define the `ml_pipeline.yml` file in the `.github/workflows/` directory, ensuring it includes:

* Checking out the repository
* Setting up python
* Installing dependencies
* Running preprocessing and model training
* Executing tests

---

## Submission Guidelines
After completing the assignment and developing the solution code in your system, commit and push the changes to this repository. 
  - Stage your changes and commit the files:
    ```
    git add .
    git commit -m "challenge Completed "
    ```
  - Push your changes to the GitHub repository:
    ```
    git push
    ```

Good luck, and happy coding!
