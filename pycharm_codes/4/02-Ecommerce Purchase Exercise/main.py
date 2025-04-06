import pandas as pd
from pandas import value_counts

# importing the file
ecom = pd.read_csv('Ecommerce Purchases')

# checking the head of the file
# print(ecom.head().to_string())
print("\n ===================================================================== \n")

# how many rows and columns
# print(ecom.info())

# average purchase price
# print(ecom['Purchase Price'].mean())

# highest and lowest purchase price
# print(ecom['Purchase Price'].max())
# print(ecom['Purchase Price'].min())

# how many people have en as their language?
# important: there is a difference between count() and value_counts()
# count: gives you the number of rows for each column
# value_count: append a new column to the original dataframe and puts the number of time the same row has been repeated
# print(ecom[ecom['Language']=='en'].count())








