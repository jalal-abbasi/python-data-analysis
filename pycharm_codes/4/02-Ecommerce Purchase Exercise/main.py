import pandas as pd

# importing the file
ecom = pd.read_csv('Ecommerce Purchases')

# checking the head of the file
print(ecom.head().to_string())

# how many rows and columns
# print(ecom.info())

# average purchase price
# print(ecom['Purchase Price'].mean())

# highest and lowest purchase price
# print(ecom['Purchase Price'].max())
# print(ecom['Purchase Price'].min())

# how many people have en as their language?

