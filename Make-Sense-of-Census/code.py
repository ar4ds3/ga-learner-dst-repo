# --------------
# Importing header files
import numpy as np
import warnings

warnings.filterwarnings('ignore')

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Reading file
data = np.genfromtxt(path, delimiter=",", skip_header=1)

#Code starts here

#Concatenating a new record and storing the array in a new variable

print("="*100)
print("Loading of information from the .CSV named ""Data"" to ""Census""")
print(" ")
print("\nData: \n\n", data)
print(" ")
print("\nType of data: \n\n", type(data))
print(" ")
print("\nShape of Data:", data.shape)
census = np.concatenate((data, new_record))
print(" ")
print("\nShape of Census:", census.shape)
print(" ")
print("\n Census: \n\n",census)
print(" ")
print("="*100)

#Extracting the Age from the Census array

for i in census:
    age = census[:,0]
print(" ")
print("\nExtracted ""Age"" from the Census array:\n", age)

max_age = np.max(age)
print(" ")
print("\nMaximum Age:\n",max_age)

min_age = np.min(age)
print(" ")
print("\nMinimum Age:\n",min_age)

age_mean = np.mean(age).round(2)
print(" ")
print("\nMean Age:\n",age_mean)

age_std = np.std(age).round(2)
print(" ")
print("\nAge Std Deviation:\n",age_std)
print("="*100)

#Determining the minority race so that the government can assist them

print("\nTotal unique values in race:\n",np.unique(census[:,2]))

race_0 = census[census[:,2]==0]
race_1 = census[census[:,2]==1]
race_2 = census[census[:,2]==2]
race_3 = census[census[:,2]==3]
race_4 = census[census[:,2]==4]
print("Race 0 :",race_0)
len_0 = len(race_0)
len_1 = len(race_1)
len_2 = len(race_2)
len_3 = len(race_3)
len_4 = len(race_4)
print(f'Total count in Race 0: {len_0}\nTotal count in Race 1: {len_1}\nTotal count in Race 2: {len_2}\nTotal count in Race 3: {len_3}\nTotal count in Race 4: {len_4}')

minority_race = len_0
if minority_race < len_1:
    minority_race = 0
if minority_race < len_2:
    minority_race = 1
if minority_race < len_3:
    minority_race = 2
if minority_race < len_4:
    minority_race = 3
else:
    minority_race = 4

print("\n\nMinority Race:", minority_race)

#To determine the working hours of people above 60 years of age

print("="*100)
print("\nTo check if the policy of 25 hours per week is followed for age greater than 60 years\n")

#Array of Senior Citizens
senior_citizens = census[census[:,0]>60]
# print("\nSenior Citizens:\n",senior_citizens)
# print(" ")

#Total Working Hours of all Senior Citizens in the array
working_hours_sum=senior_citizens.sum(axis=0)[6]
print("\nWorking Hours of Senior Citizens: \n",working_hours_sum)
print(" ")

#Total number of Senior Citizens
senior_citizens_len = len(senior_citizens)
print("\nTotal Number of Senior Citizens: \n", senior_citizens_len)
print(" ")

#Average Working Hours of Senior Citizens
avg_working_hours = working_hours_sum/senior_citizens_len
print("\nAverage Working Hours of Senior Citizens:\n",avg_working_hours)
print(" ")
print("="*100)


#To check the average High and Low pay

print("\nTo check the average High and Low pay\n")
print(" ")

#Arrays to sort census with high and low exposure in education
high = census[census[:,1]>10]
low = census[census[:,1]<=10]

#To calculate average pay of people who pursued higher education
avg_pay_high = round(high.mean(axis=0)[7],2)
print("\nThe average pay of people who pursued higher education: \n", avg_pay_high)
print(" ")

#To calculate average pay of people who did not pursue higher education
avg_pay_low = round(low.mean(axis=0)[7],2)
print("\nThe average pay of people who did not pursue higher education: \n", avg_pay_low)
print(" ")



