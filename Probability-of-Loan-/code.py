# --------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataframe
df = pd.read_csv(path)

#Code starts here

num=len(df)
print("total number of events:",num)
fico_more_700= df[df['fico']>700]
len_fico=len(fico_more_700)
p_a=len_fico/num
print("probability of fico>700 is:",round(p_a,2))

purp=df[df['purpose']=='debt_consolidation']
len_purp=len(purp)
p_b=len_purp/num
print("probability of purpose debt consolations is:",round(p_b,2))

df1=purp
anb=df[(df['purpose']=='debt_consolidation') & (df['fico']>700)]
len_anb=len(anb)
p_a_b=len_anb/num
print("probability of a and b is:",round(p_a_b,2))
result= (p_a_b == p_a)
print (result)
print("*"*70)

#TASK 2

paid_back_loan= df[df['paid.back.loan']=='Yes']
len_paid_back_loan= len(paid_back_loan)
prob_lp=len_paid_back_loan/num
print("Probability of paid back loan yes is:",round(prob_lp,2))

credit_policy=df[df['credit.policy']=='Yes']
len_creditpolicy=len(credit_policy)
prob_cs=len_creditpolicy/num
print("Probability of credit policy  yes is:",round(prob_cs,2))


new_df= paid_back_loan

prob_pd_cs=new_df[new_df['credit.policy']=='Yes'].shape[0]/new_df.shape[0]
print("Probability of paid back loan and credit policy yes is:",round(prob_pd_cs,2))
bayes=(prob_pd_cs * prob_lp)/prob_cs
print("Conditional probability  Bayes is:",round(bayes,4))

print("*"*70)

#TASK 3

df1=df[df['paid.back.loan']=='No']
df1.purpose.value_counts(normalize=True).plot(kind='bar')
print("Shape of df1 is:", df1.shape)
print("*"*70)

# Task 4

inst_median= df['installment'].median()
print("Median of installment is:",inst_median)
inst_mean=df['installment'].mean()
print("Mean of installment is:",inst_mean)
df['installment'].hist(normed=True, bins=50)
#df['log.annual.inc'].plot.hist(bins=50)





