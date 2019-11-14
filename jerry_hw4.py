#!/usr/bin/env python
# coding: utf-8

# In[13]:


# Hw2 Problem 2
from pandas import Series, DataFrame
import pandas as pd
import io
import requests
import numpy as np

WEBSITE_DATA = "https://data.seattle.gov/api/views/65db-xm6k/rows.csv?accessType=DOWNLOAD"
S = requests.get(WEBSITE_DATA).content
DATASET = pd.read_csv(io.StringIO(S.decode('utf-8')))
DF = pd.DataFrame(DATASET)
DF = DF.head(10)
DF_EAST = DF['Fremont Bridge East Sidewalk']
DF_WEST = DF['Fremont Bridge West Sidewalk']
DF1 = pd.DataFrame({'Fremont Bridge East Sidewalk': DF_EAST,
                    'Fremont Bridge West Sidewalk': DF_WEST})


TEST = DataFrame(np.arange(20.0).reshape(10, 2), index=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], columns=[
                 'Fremont Bridge East Sidewalk', 'Fremont Bridge West Sidewalk'])

# The DataFrame contains only the columns that you specified as the second argument.
if DF1.columns.all() == TEST.columns.all():
    print('true')

# The values in each column have the same python type
if DF1.columns.dtype == TEST.columns.dtype:
    print('true')

# There are at least 10 rows in the DataFrame.
if len(TEST.index) >= 10:
    print('true')

# Hw3 Problem 2
# Check that all columns have values of the corect type
if DF1.dtypes.all() == TEST.dtypes.all():
    print('true')

# Verify that the dataframe has at least one row
if len(TEST.index) >= 1:
    print('true')

# Check for nan values
DF1.isnull().values.any()
