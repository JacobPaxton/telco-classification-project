import pandas as pd
from acquire import gen_telco


def gen_prep_telco():
    """
        Acquires all tables from Codeup's telco_churn database,
        Prepares the 'customers' table for modeling, then
        Returns all tables including the prepared 'customers' table.
    """

    # Acquire data using gen_telco()
    telco_raw, contract_types, internet_service_types, payment_types = gen_telco()

    # Create maps and map lists
    first_map = {'No':0, 'Yes':1}
    first_map_cols = ['partner', 'dependents', 'phone_service', 'multiple_lines', 
                    'online_backup', 'device_protection', 'tech_support',
                    'streaming_tv', 'streaming_movies', 'paperless_billing', 'churn']

    second_map = {'No':0, 'Yes':1, 'No phone service':2}
    second_map_cols = ['multiple_lines']

    third_map = {'No':0, 'Yes':1, 'No internet service':2}
    third_map_cols = ['online_security', 'online_backup', 'device_protection', 'tech_support', 
                  'streaming_tv', 'streaming_movies']
    fourth_map = {'Male':0, 'Female':1}
    fourth_map_cols = ['gender']

    # Retain columns that don't need to be mapped
    ordinal_cols = ['senior_citizen', 'internet_service_type_id', 'contract_type_id',
                    'payment_type_id']
    numeric_cols = ['tenure', 'monthly_charges', 'total_charges']

    # Encode
    telco_encoded = pd.DataFrame()
    for col in first_map_cols:
        telco_encoded[col] = telco_raw[col].map(first_map)
    for col in second_map_cols:
        telco_encoded[col] = telco_raw[col].map(second_map)
    for col in third_map_cols:
        telco_encoded[col] = telco_raw[col].map(third_map)
    for col in fourth_map_cols:
        telco_encoded[col] = telco_raw[col].map(fourth_map)

    # Stitch dataframe back together
    telco = pd.concat([telco_encoded, 
                       telco_raw[ordinal_cols], 
                       telco_raw[numeric_cols]], axis=1)

    return telco, contract_types, internet_service_types, payment_types