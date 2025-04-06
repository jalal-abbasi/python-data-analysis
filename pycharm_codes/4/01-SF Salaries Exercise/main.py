import pandas as pd
import numpy as np
from pandas.core.arrays.categorical import contains

salaries_dataframe = pd.read_csv('Salaries.csv',low_memory=False)
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

# How many unique job titles are there?
# print(salaries_dataframe['JobTitle'].nunique())

# What are the top 5 most common jobs?
# print(salaries_dataframe['JobTitle'].unique())
# print(salaries_dataframe['JobTitle'].value_counts().head())

# How many Job Titles were represented by only one person in 2013? (e.g. Job Titles with only one occurence in 2013?)
# job_titles_value_counts = salaries_dataframe[salaries_dataframe['Year']==2013]['JobTitle'].value_counts()
# print(job_titles_value_counts[job_titles_value_counts==1].sum())

# How many people have the word Chief in their job title? (This is pretty tricky)
count=0
def has_word_inside(cell):
    global count
    if 'Chief'.lower() in cell.lower():
            count+=1
    return count


salaries_dataframe['JobTitle'].apply(has_word_inside)
print(count)