# -*- coding: utf-8 -*-
"""Parkinson's Disease Detection - ML.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qXvsKLWzjQ74YTJZrNs2KpN3nuuR6tfW
"""

#Install Libraries with pip

!pip install numpy pandas sklearn xgboost

#Download necessary imports

import numpy as np
import pandas as pd
import os, sys
from sklearn.preprocessing import MinMaxScaler
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

#Read the file

df = pd.read_csv('/content/parkinsons-data.data')
df.head()

#Obtain all the features and labels from the dataset
#Features - all columns except the status
#Labels - Status column

features = df.loc[:, df.columns!='status'].values[:,1:]
labels=df.loc[:, 'status'].values

#Counting the values of the labels variables (0 and 1)

print(labels[labels==1].shape[0], labels[labels==0].shape[0])

