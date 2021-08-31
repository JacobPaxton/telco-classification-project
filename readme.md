# <center>Churn at Telco</center>
<!-- ## Overview
**Project Goals:**
- Goal 1: **Demonstrate the process** for data acquisition, data processing, and model creation.
- Goal 2: **Create modules** that make the process repeatable.
- Goal 3: **Identify potential drivers of churn.**
- Goal 4: **Construct a model to predict churn using classification techniques.**
- Goal 5: **Deliver a presentation** to the Codeup Data Science Team using the Jupyter Notebook for the above steps.
- Goal 6: Answer potential questions about the code, process, findings and key takeaways, and model. -->

<!-- **Deliverables:**
- JupyterNB presentation
- README.md project description containing:
    * Goals
    * Initial hypotheses
    * Data dictionary
    * Plan (data science pipeline)
    * Instructions on how to recreate your work
    * Answers to hypotheses
    * Key findings
    * Recommendations
    * Takeaways
- CSV of X_test predictions with customer_id, probability of churn, and prediction of churn. (1=churn, 0=not_churn).
- Scripts, specifically acquire.py and prepare.py
- The presentation -->
## Description:
The Codeup Data Science Team is tasked with analyzing churn at Telco. This repository serves as the vehicle for this analysis.

## Goals: 
1. Identify potential drivers of churn
2. Construct a model to predict churn

## Initial Hypotheses:
1. Customers without support options churn more than those with support
2. Customers without a spouse or dependents churn more than those with a spouse or dependents

## Key findings
1. Customers without support options churn much more than those with support
2. Customers without a spouse or dependents do churn more than those with spouse or dependents

## Recommmendations
1. Team should focus on analyzing the support options further
2. Team should make churn projections involving increased support options

## Takeaways
Increased support outreach to customers and retuning marketing approach to families should decrease churn.

## Data Dictionary:
|Target|Datatype|Definition|
|:-------|:--------|:----------|
| churn | 150 non-null: object | has churned - 0 for no, 1 for yes |

|Feature|Datatype|Definition|
|:-------|:--------|:----------|
| customer_id              | 7043 non-null: object | customer id - unique string for each customer |
| gender                   | 7043 non-null: object | gender - male or female |
| senior_citizen           | 7043 non-null: int64  | is senior citizen - 0 for no, 1 for yes |
| partner                  | 7043 non-null: object | has spouse - yes or no |
| dependents               | 7043 non-null: object | has dependents - yes or no |
| tenure                   | 7043 non-null: int64  | # of months of tenure with telco |
| phone_service            | 7043 non-null: object | has phone service - yes or no |
| multiple_lines           | 7043 non-null: object | has multiple lines - yes, no, or no phone service |
| online_security          | 7043 non-null: object | has the online security service - yes, no, or no internet service |
| online_backup            | 7043 non-null: object | has the online backup service - yes, no, or no internet service |
| device_protection        | 7043 non-null: object | has the device protection service - yes, no, or no internet service |
| tech_support             | 7043 non-null: object | has the tech support service - yes, no, or no internet service |
| streaming_tv             | 7043 non-null: object | has the tv streaming service - yes, no, or no internet service |
| streaming_movies         | 7043 non-null: object | has the movie streaming service - yes, no, or no internet service |
| paperless_billing        | 7043 non-null: object | has paperless billing - 0 for no, 1 for yes |
| monthly_charges          | 7043 non-null: float64 | customer burden each month |
| total_charges            | 7043 non-null: object  | total customer burden paid |
| churn                    | 7043 non-null: object  | has churned - 0 for no, 1 for yes |

|Keyed Feature|Datatype|Definition|
|:-------|:--------|:----------|
| internet_service_type_id | 7043 non-null: int64  | internet service - DSL (1), Fiber optic (2), or No internet service (3) |
| contract_type_id         | 7043 non-null: int64  | subscription plan - Month-to-month (1), One year (2), or Two year (3) |
| payment_type_id          | 7043 non-null: int64  | payment methods - Electronic check (1), Mailed check (2), Bank transfer (automatic) (3), or Credit card (automatic) (4) |

## Plan
1. Write script to acquire and store each table from Codeup's telco_churn database
    * Deliverable for **acquire.py**
2. Write script to split/tidy the customers table for model fit and evaluation
    * Deliverable for **prepare.py**
3. Run preliminary exploration functions to understand basic dataset structure and contents
4. Narrow potential features down to those with *a value* having the following characteristics:
    * Much higher churn rate than the feature's other values,
    * Roughly between 30% and 60% share of total customer population, and
    * Less than 60% commonality with another potential feature's churning value.
5. Build models using these features in different combinations as necessary
6. Evaluate models, and with extra time, further optimize models by tuning hyperparameters
7. Create CSV of X_test predictions with customer_id, probability of churn, and prediction of churn. (1=churn, 0=not_churn)
    * Deliverable for **predictions.csv**
8. Split all work into this README and final_telco_presentation.ipynb
9. Clean work, and with extra time, make work more pretty
10. Present!

## Instructions for re-creating my work
0. For exact syntax, please see my project artifacts or contact me
1. Pull acquire.py and prepare.py
2. Use your own env.py with a get_db_url function that acquire.py can call to access the database
    * Example call for acquire.py (for reference):
    * url = get_db_url(db_name='telco_churn')
3. Run the acquire.py function to acquire the data from the database and store it locally
4. Run the prepare.py function to encode the data, assign output to four dataframes
5. Run Maggie's explore.py functions for train_validate_test_split with seed=123
6. Separate features and target out for Maggie's univariate and bivariate functions
7. Build RandomForest, KNearestClassifier, and LogisticRegression models using combinations of these features:
    * 'partner', 'internet_service_type_id', 'online_backup', 'contract_type_id', 'device_protection'
8. Feel free to reference my notebook's un-optimized hyperparameters or use your own