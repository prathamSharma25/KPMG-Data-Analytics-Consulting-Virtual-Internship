# -*- coding: utf-8 -*-
"""
Created on Thu May 21 18:15:34 2020

@author: Pratham
"""
"""
Data Quality Assessment for KPMG - Virtual Internship

The following datasets have been provided by the client:
    1) Customer Demographics
    2) Customer Addresses
    3) Transactions
    
This script performs the preliminary data exploration and quality assessment
to identify various data quality issue in the datasets provided.
"""

import pandas as pd

CustomerDemographic = pd.read_csv(r'C:\Users\Pratham\Virtual Experience Programs\KMPG-VI\Datasets\CustomerDemographic.csv')
print('Customer Demographics: \n')
print('Columns: \n', CustomerDemographic.columns, '\n')
print('Head: \n', CustomerDemographic.head(), '\n')
print('Shape: ', CustomerDemographic.shape, '\n')

CustomerAddresses = pd.read_csv(r'C:\Users\Pratham\Virtual Experience Programs\KMPG-VI\Datasets\CustomerAddresses.csv')
print('Customer Addresses: \n')
print('Columns: \n', CustomerAddresses.columns, '\n')
print('Head: \n', CustomerAddresses.head(), '\n')
print('Shape: ', CustomerAddresses.shape, '\n')

Transactions = pd.read_csv(r'C:\Users\Pratham\Virtual Experience Programs\KMPG-VI\Datasets\Transactions.csv')
print('Transactions: \n')
print('Columns: \n', Transactions.columns, '\n')
print('Head: \n', Transactions.head(), '\n')
print('Shape: ', Transactions.shape, '\n')