# Hands-on Practice MLOps (Ungraded)-ok

## Attempt below exerices with the provided Customer Churn Data

### Exercise-1: Train the model for Customer Churn prediction

- Install required packages using `requirements.txt`
- Run the training script `train_model.py'
- Check the trained model saved in `models` directory

### Exercise-2: Develop test cases

- Install required testing package - `pytest`
- Write your test case in `tests/test_prediction.py` file to check model accuracy > 0.8
- Return a custom error response when the test case fails

### Exercise-3: Create API endpoint

- Install required packages - `fastapi`, `uvicorn`, etc
- Write your code in `app.py` file to create a `predict/` endpoint using FastAPI that will take data from user and returns the model prediction
- You can use Swagger UI to test the endpoint which is avaialble to `/docs` endpoint once you start the FastAPI application

### Exercise-4: Dockerize the application

- Create a `Dockerfile` to containerize your FastAPI application
- Build a docker image using the Dockerfile
- Start a container and test if the application is working fine
- Push the docker image on your DockerHub account

---

## Dataset Description:

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

## Submission Guidelines

After completing the exercises and developing the solution, commit and push the changes to this repository. 
  - Stage your changes and commit the files:
    ```
    git add .
    git commit -m "Exercies Completed"
    ```
  - Push your changes to the GitHub repository:
    ```
    git push
    ```

Good luck, and happy learning!
