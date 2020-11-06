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
print("shape of new record", np.shape(new_record))
print("shape of data", np.shape(data))
print("\n")
census=np.concatenate((new_record,data))
print("census is", "\n", census)
print("\n")
print(" shape of census is", np.shape(census))
age= census[:,0]
print (age)
max_age= np.max(age)
print("max age is:", max_age)
min_age=np.min(age)
print("min age is:", min_age)
age_mean=np.mean(age)
print("mean age is:", age_mean)
age_dev=np.std(age)
print("standard deviation is:", age_dev)


cond=(census[:,2]==0)
race_0= census[cond]
#print("Race zero:", race_0)
print("*"*50)
len_0= len(race_0)


cond1=(census[:,2]==1)
race_1= (census[cond1].astype(int))
#print("Race one:", race_1)
print("*"*50)
len_1= len(race_1)


cond2=(census[:,2]==2)
race_2= (census[cond2].astype(int))
#print("Race two:", race_2)
print("*"*50)
len_2= len(race_2)



cond3=(census[:,2]==3)
race_3= (census[cond3].astype(int))
#print("Race three:", race_3)
print("*"*50)
len_3= len(race_3)



cond4=(census[:,2]==4)
race_4= (census[cond4].astype(int))
#print("Race four:", race_4)
print("*"*50)
len_4=len(race_4)

print("length of cond 0 array is", len_0 )
print("length of cond 1 array is", len_1)
print("length of cond 2 array is", len_2)
print("length of cond 3 array is", len_3)
print("length of cond 4 array is", len_4)

minority_race= min(len_0,len_1,len_2,len_3,len_4)
print("minority race is", minority_race, )

cond_age=(census[:,0]>60)
senior_citizens= census[cond_age]
working_hours_sum= np.sum(senior_citizens[:,6])
print("working hours for senior citizens", working_hours_sum)
senior_citizens_len= len(senior_citizens)
avg_working= working_hours_sum/senior_citizens_len
print("average working hours:",avg_working)

condhigh= (census[:,1]>10)
condlow= (census[:,1]<=10)
high= census[condhigh]
low=census[condlow]

avg_pay_high= np.mean(high[:,7])
avg_pay_low=np.mean(low[:,7])

print("average high pay is:", avg_pay_high)
print("average low pay is:", avg_pay_low)





