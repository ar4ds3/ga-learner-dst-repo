# --------------
# Importing header files
import numpy as np
import pandas as pd
from scipy.stats import mode 
 
import warnings
warnings.filterwarnings('ignore')


#Reading file
#Original var = bank_data
bank = pd.read_csv(path)

#Code starts here

#Step 1 - Seggregating the Categorical and Numerical columns
print("=" * 100)
print("\nSeggregating the Categorical and Numerical columns...\n")
print(" ")

#To determine the categorical and numnerical features
categorical_var = bank.select_dtypes(include = 'object')
print("\nCategorical Features:\n",categorical_var.columns)

numerical_var = bank.select_dtypes( include = 'number')
print("\nNumerial Features:\n",numerical_var.columns)
print("=" * 100)

#Step 2 - Cleaning the data set
print("\n Cleansing the dataset...\n")
print(" ")
#Creating a new data frame 'banks'

#Dropping a column from the dataset
banks= bank.drop(columns='Loan_ID')

#Determining the null values across the dataset
print("\nColumns having null values:\n", banks.isnull().sum())
print(" ")
#Determing the mode of the dataset 'banks'
bank_mode = banks.mode().iloc[0]
print("\nMode for all the features in the dataset:\n", bank_mode)
print(" ")

#To fill the missing values in the features accross the dataset
banks.fillna(bank_mode, inplace = True)
#banks.shape
banks.isnull().sum().values.sum()
print("\nFeatures after replacing the null values with mode: \n", banks.isnull().sum())
print(" ")
print("=" * 100)

#Step 3 -  To check the loan amount status
print("\nTo check the loan amount status...\n")
print(" ")

#To determine the loan amount of an average person
avg_loan_amount = banks.pivot_table(index=['Gender', 'Married', 'Self_Employed'], values= ['LoanAmount'], aggfunc='mean')
print("\nPivot Table to check the loan amount of an average person:\n", avg_loan_amount)
print(" ")
print("\nSelf Employed Unmarried Female:\n",avg_loan_amount['LoanAmount'][1],2)
print(" ")
print("=" * 100)


#Step 4 - To determine the percentage of loan approaved based on person's employment type
print("\nTo determine the percentage of loan approaved based on person's employment type...\n")


loan_approved_se = banks[(banks['Self_Employed'] == 'Yes') & (banks['Loan_Status'] == 'Y')]
#print("\nLoan approved for Self Employed:\n",loan_approved_se)
print(" ")
loan_approved_nse = banks[(banks['Self_Employed'] == 'No') & (banks['Loan_Status'] == 'Y')]
#print("\nLoan approved for other than Self Employed:\n",loan_approved_nse)
print(" ")

Loan_Status = banks['Loan_Status'].count()
print("\nCount of Loan Status:\n",Loan_Status)
print(" ")

percentage_se = round((len(loan_approved_se)/Loan_Status)*100, 2)
print("\nPercentage of loan approved for self-employed:\n", percentage_se)
print(" ")

percentage_nse = round((len(loan_approved_nse)/Loan_Status)*100, 2)
print("\nPercentage of loan approved for self-employed:\n", percentage_nse)
print(" ")

print("=" * 100)

#Step 5 - Applicants with long loan terms
print("\nApplicants with long loan terms...\n")
print(" ")

loan_term = banks['Loan_Amount_Term'].apply(lambda x: int(x)/12)
print("\nConverting loan term:\n", loan_term)
print(" ")
big_loan_term = len(loan_term[loan_term>=25])
print("\nTotal number of applicant's loan greater than equal to 25 years:\n",big_loan_term)


#Step 6 - Average income of applicant and average loan given based on their income

print("\nAverage income of applicant and average loan given based on their income...\n")
print(" ")

loan_groupby = banks.groupby(['Loan_Status'])
loan_groupby = loan_groupby['ApplicantIncome', 'Credit_History']

mean_values = loan_groupby.mean()
print(mean_values)


