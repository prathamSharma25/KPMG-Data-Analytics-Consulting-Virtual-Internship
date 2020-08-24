# -*- coding: utf-8 -*-
"""
Created on Fri May 29 17:54:11 2020

@author: Pratham
"""
"""
A simple regression model was applied to predict the profits that may be earned by atrgetting the new customers.
Model is trained based on historical data provided.
"""

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder

train = pd.read_csv(r'C:\Users\Pratham\Virtual Experience Programs\KMPG-VI\Datasets\TrainingSet.csv')
test = pd.read_csv(r'C:\Users\Pratham\Virtual Experience Programs\KMPG-VI\Datasets\TestingSet.csv')

encoder = LabelEncoder()
train['Customer Segment'] = encoder.fit_transform(train['Customer Segment'])
test['Customer Segment'] = encoder.fit_transform(test['Customer Segment'])

train_X = train.iloc[:, 1:].values
train_y = train.iloc[:,0].values
test_X = test.iloc[:,:].values

regressor = LinearRegression()
regressor.fit(train_X, train_y)
pred_profits = regressor.predict(test_X)

predicted_profits = pd.DataFrame(test_X)
predicted_profits['Profit'] = pd.Series(pred_profits)
predicted_profits.to_csv("predicted_profits.csv", index = False)
