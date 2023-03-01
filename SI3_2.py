import numpy as np
import pandas as pd

# create 15 random revenue values between 1000 and 5000
revenue = np.random.randint(1000, 5000, size=15)

# create a list of worker names
workers = ['Worker {}'.format(i) for i in range(1, 16)]

# create a dictionary with the data
data = {'Worker': workers, 'Revenue ($)': revenue}

# create a dataframe from the dictionary
df = pd.DataFrame(data)

print(df)
# display lines 2, 6, and 13
print(df.iloc[[1, 5, 12]])
# display the worker value for line 7
print(df.loc[6, 'Worker'])

# display the revenue value for line 14
print(df.loc[13, 'Revenue ($)'])
# load data from csv file
df = pd.read_csv('data.csv')

# set option to display all columns without abbreviations
pd.set_option('display.max_colwidth', None)

# display all records
print(df)
# display first 100 records
print(df.head(100))

# display last 100 records
print(df.tail(100))

def removeRows(df):
    return df.dropna()