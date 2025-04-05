import pandas as pd
import numpy as np

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

# What was the average (mean) BasePay of all employees per year? (2011-2014) ?