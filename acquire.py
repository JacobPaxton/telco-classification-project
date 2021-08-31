import pandas as pd
import os
from env import get_db_url

def gen_telco():
    """
        Checks for local copies of telco_churn tables,
        If tables aren't stored locally, 
            Reads the telco_churn database from Codeup, and
            Saves each table to the current directory as separate .csv files, then
        Returns each table separately.
    """

    # customers table
    if not os.path.isfile('telco_raw.csv'):
        url = get_db_url(db_name='telco_churn')
        telco_raw = pd.read_sql('SELECT * FROM customers', url)
        telco_raw.to_csv('telco_raw.csv')
    telco_raw = pd.read_csv('telco_raw.csv')

    # contract_types table
    if not os.path.isfile('contract_types.csv'):
        url = get_db_url(db_name='telco_churn')
        telco_raw = pd.read_sql('SELECT * FROM contract_types', url)
        telco_raw.to_csv('contract_types.csv')
    contract_types = pd.read_csv('contract_types.csv')

    # internet_service_types table
    if not os.path.isfile('internet_service_types.csv'):
        url = get_db_url(db_name='telco_churn')
        telco_raw = pd.read_sql('SELECT * FROM internet_service_types', url)
        telco_raw.to_csv('internet_service_types.csv')
    internet_service_types = pd.read_csv('internet_service_types.csv')

    # payment_types table
    if not os.path.isfile('payment_types.csv'):
        url = get_db_url(db_name='telco_churn')
        telco_raw = pd.read_sql('SELECT * FROM payment_types', url)
        telco_raw.to_csv('payment_types.csv')
    payment_types = pd.read_csv('payment_types.csv')

    return telco_raw, contract_types, internet_service_types, payment_types