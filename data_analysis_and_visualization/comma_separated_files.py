'''
How to read data from CSV files using Pandas library of Python

CSV files are common in machine learning
'''

import pandas as pd

#Define the column name as a list
names = ['age', 'workclass', 'fnlwgt', 'education', 'educationnum', 'maritalstatus', 'occupation', 'relationship', 'race',
        'sex', 'capitalgain', 'capitalloss', 'hoursperweek', 'nativecountry', 'label']

#Read in the CSV file from the webpage using the defined column names
df = pd.read_csv("adult.data", header=None, names=names)

print(df.head()) # See first 5 rows of data

'''
A Pandas dataframe is very similar to a matrix of data
'''