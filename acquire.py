import pandas as pd
import os
from env import get_db_url

def gen_telco():
    if not os.path.isfile('telco_raw.csv'):
        url = get_db_url(db_name='telco_churn')
        telco_raw = pd.read_sql('SELECT * FROM customers', url)
        telco_raw.to_csv('telco_raw.csv')
    telco_raw = pd.read_csv('telco_raw.csv')

    if not os.path.isfile('contract_types.csv'):
        url = get_db_url(db_name='telco_churn')
        telco_raw = pd.read_sql('SELECT * FROM contract_types', url)
        telco_raw.to_csv('contract_types.csv')
    contract_types = pd.read_csv('contract_types.csv')

    if not os.path.isfile('internet_service_types.csv'):
        url = get_db_url(db_name='telco_churn')
        telco_raw = pd.read_sql('SELECT * FROM internet_service_types', url)
        telco_raw.to_csv('internet_service_types.csv')
    internet_service_types = pd.read_csv('internet_service_types.csv')

    if not os.path.isfile('payment_types.csv'):
        url = get_db_url(db_name='telco_churn')
        telco_raw = pd.read_sql('SELECT * FROM payment_types', url)
        telco_raw.to_csv('payment_types.csv')
    payment_types = pd.read_csv('payment_types.csv')

    return telco_raw, contract_types, internet_service_types, payment_types