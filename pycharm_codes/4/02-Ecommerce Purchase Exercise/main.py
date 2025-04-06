from re import split

import pandas as pd
from pandas import value_counts

# importing the file
ecom = pd.read_csv('Ecommerce Purchases')

# checking the head of the file
print(ecom.head().to_string())
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

# How many people have the job title of "Lawyer" ?
# info() is very similar to count(), but it also gives more information on each data type
# print(ecom[ecom['Job']=='Lawyer'].info())


# How many people made the purchase during the AM and how many people made the purchase during PM ?
# print(ecom['AM or PM'].value_counts())

# What are the 5 most common Job Titles?
# print(ecom['Job'].value_counts().head(n=5))

# Someone made a purchase that came from Lot: "90 WT" , what was the Purchase Price for this transaction?
# print(ecom[ecom['Lot']=='90 WT']['Purchase Price'])

# What is the email of the person with the following Credit Card Number: 4926535242672853
# print(ecom[ecom['Credit Card']==4926535242672853]['Email'])

# How many people have American Express as their Credit Card Provider and made a purchase above $95 ?
# print(ecom[(ecom['CC Provider'] == 'American Express') & (ecom['Purchase Price'] > 95)].count())

# Hard: How many people have a credit card that expires in 2025?
# print(sum(ecom['CC Exp Date'].apply(lambda x: '/25' in x)))

# Hard: What are the top 5 most popular email providers/hosts (e.g. gmail.com, yahoo.com, etc...)
print(
    ecom['Email'].apply(lambda x: x.split('@')[1]).value_counts().head()
)






