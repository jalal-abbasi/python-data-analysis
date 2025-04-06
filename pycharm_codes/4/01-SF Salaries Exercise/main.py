import pandas as pd
import numpy as np
from pandas.core.arrays.categorical import contains

salaries_dataframe = pd.read_csv('Salaries.csv', low_memory=False)

# head: shows the first n data. the default value is 5
# print(salaries_dataframe.head().to_string())

# info will give you the information about the dataframe
# print(salaries_dataframe.info())

# mean in a column
# print(salaries_dataframe['BasePay'].mean())

# What is the highest amount of OvertimePay in the dataset ?
# print(salaries_dataframe['OvertimePay'].max())

# 'JOSEPH DRISCOLL' Job title
# print(salaries_dataframe[salaries_dataframe['EmployeeName']=='JOSEPH DRISCOLL']['JobTitle'])

# How much does JOSEPH DRISCOLL make (including benefits)?
# print(salaries_dataframe[salaries_dataframe['EmployeeName']=='JOSEPH DRISCOLL'].to_string())
# print(salaries_dataframe[salaries_dataframe['EmployeeName']=='JOSEPH DRISCOLL']['TotalPayBenefits'])

# What is the name of highest paid person (including benefits)?
# print(salaries_dataframe[salaries_dataframe['TotalPayBenefits'] == salaries_dataframe['TotalPayBenefits'].max()]['EmployeeName'])

# What is the name of lowest paid person (including benefits)?
# print(salaries_dataframe[salaries_dataframe['TotalPayBenefits'] == salaries_dataframe['TotalPayBenefits'].min()].to_string())

# What was the average (mean) BasePay of all employees per year? (2011-2014)
# for year in range(2011,2015):
#     print(f"{year}    {salaries_dataframe[salaries_dataframe['Year']==year]['BasePay'].mean()}")

# I forgot to use the group-by method!
'''
print(salaries_dataframe.groupby('Year')['BasePay'].mean())
note that: you cannot see the grouped table, because the output is an object. therefore you have to use
Pandas’ aggregation functions like .sum() or .mean():
Ignore non-numeric columns (like strings) by default.
Work only on columns that support the operation.
'''

# How many unique job titles are there?
# print(salaries_dataframe['JobTitle'].nunique())

# What are the top 5 most common jobs?
# print(salaries_dataframe['JobTitle'].unique())
# print(salaries_dataframe['JobTitle'].value_counts().head())

# How many Job Titles were represented by only one person in 2013? (e.g. Job Titles with only one occurence in 2013?)
job_titles_value_counts = salaries_dataframe[salaries_dataframe['Year']==2013]['JobTitle'].value_counts()
print(job_titles_value_counts[job_titles_value_counts==1].sum())
'''
in my solution, sumn is a Series.sum().
however, in the instructor's solution sum  is Python’s built-in sum() working on a boolean iterable. because we have  boolean Series like
Clerk               False
Firefighter         False
Yoga Instructor      True
Dog Catcher          True
... (etc)
True is treated as 1, and False as 0. So this adds up how many Trues — i.e., how many unique job titles.

instructor's solution:
sum(salaries_dataframe[salaries_dataframe['Year']==2013]['JobTitle'].value_counts() == 1) # pretty tricky way to do this...
'''

# How many people have the word Chief in their job title? (This is pretty tricky)
count=0
def has_word_inside(cell):
    global count
    if 'Chief'.lower() in cell.lower():
            count+=1
    return count


salaries_dataframe['JobTitle'].apply(has_word_inside)
print(count)


'''
why code is not a good practice!!This is not considered good practice, because .apply() is meant to return a new Series — not modify global state.

instructor's code:
def chief_string(title):
    if 'chief' in title.lower():
        return True
    else:
        return False
        
sum(salaries_dataframe['JobTitle'].apply(lambda x: chief_string(x)))
lambda function here means:  For every x (i.e., job title) in the column, run chief_string(x)

keep in mind:
lambda arguments: expression
is equivalent to
def some_function(arguments):
    return expression

so in lamda (anonymous) function, we omit 'def', 'function_name' and 'return' keywords.

the instructor misused the usage of lambda! we would need it if chief_string() function, needed another argument other than the cell
contentent itself. for example:
sum(salaries_dataframe['JobTitle'].apply(lambda x: chief_string(x, 'chief')))
'''
# Bonus: Is there a correlation between length of the Job Title string and Salary?
# corr_dataframe = pd.concat([salaries_dataframe['JobTitle'].apply(len).rename('title_len'), salaries_dataframe['TotalPayBenefits']],axis=1)
# print(corr_dataframe.corr())