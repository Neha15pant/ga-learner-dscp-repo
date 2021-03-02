# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#Reading the file
data=pd.read_csv(path)

#Code starts here

# Step 1 
#Reading the file
#Creating a new variable to store the value counts
loan_status=data['Loan_Status'].value_counts()
print(loan_status)
#Plotting bar plot
plt.bar(loan_status.index ,loan_status.values )
print(data.iloc[25,1])
print(data.iloc[53,9])
print(loan_status[0])
print(loan_status[1])
# Step 2
#Plotting an unstacked bar plot

# Label X-axes and Y-axes=

property_and_loan=data.groupby(['Property_Area', 'Loan_Status'])
property_and_loan.size().unstack().plot(kind='bar', stacked=False, figsize=(15,10))
#data.groupby(['Property_Area', 'Loan_Status']).size().unstack().plot(kind='bar', stacked=False, figsize=(15,10))
# Label X-axes and Y-axes
plt.xlabel('Property_Area')
plt.ylabel('Loan_Status')
# Rotate X-axes labels
plt.xticks(rotation=45)
# Display plot
plt.show()
#print("Property and loan1 test:",property_and_loan['N'][1])
#print("Property and loan2 test:",property_and_loan['Y'][0])
# Step 3
#Plotting a stacked bar plot
education_and_loan= data.groupby(['Education', 'Loan_Status'])
education_and_loan.size().unstack().plot(kind='bar', stacked=True, figsize=(15,10))
#data.groupby(['Education', 'Loan_Status']).size().unstack().plot(kind='bar', stacked=True, figsize=(15,10))
# Label X-axes and Y-axes
plt.xlabel('Education Status')
plt.ylabel('Loan Status')
# Rotate X-axes labels
plt.xticks(rotation=45)
# Display plot
plt.show()
# Step 4 
#Subsetting the dataframe based on 'Education' column
graduate=data[data['Education']=="Graduate"]
not_graduate=data[data['Education']=="Not Graduate"]
#Subsetting the dataframe based on 'Education' column
graduate.LoanAmount.plot.density(color='green') 
plt.title('Density plot for Loan Amount-Graduate') 
plt.show()

#Plotting density plot for 'Graduate'
not_graduate.LoanAmount.plot.density(color='red') 
plt.title('Density plot for Loan Amount-Not Graduate') 
plt.show()

#For automatic legend display


# Step 5
#Setting up the subplots
fig, (ax_1, ax_2,ax_3) = plt.subplots(3, figsize=(20,10))

#Plotting scatter plot

ax_1.scatter(x=data['ApplicantIncome'],y=data['LoanAmount'])
ax_1.set_xlabel("Applicant Income")
ax_1.set_ylabel("Loan Amount")
ax_1.set_title("Applicant Income")


ax_2.scatter(x=data['CoapplicantIncome'],y=data['LoanAmount'])
ax_2.set_xlabel("Coapplicant Income")
ax_2.set_ylabel("Loan Amount")
ax_2.set_title("Coapplicant Income")

data['TotalIncome']=data['ApplicantIncome']+data['CoapplicantIncome']

ax_3.scatter(x=data['TotalIncome'],y=data['LoanAmount'])
ax_3.set_xlabel("Total Income")
ax_3.set_ylabel("Loan Amount")
ax_3.set_title("Total Income")

plt.show()

