# --------------
#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#Reading of the file
data=pd.read_csv(path)
data['Gender']= data['Gender'].replace(to_replace ="-", value ="Agender")
#print(data['Gender'])
gen=data['Gender'].value_counts()
plt.figure(figsize=[8,6])
plt.bar(gen.index ,gen.values )
plt.xlabel("Gender")
plt.ylabel("Number")

align=data['Alignment'].value_counts()
plt.figure(figsize=[8,6])
plt.bar(align.index, align.values)
plt.xlabel("Alignment")
plt.ylabel("Number")


covariance1=data[['Combat', 'Intelligence']].cov().iloc[0,1]
print ("Covariance between Combat and intelligence is:", covariance1)
covariance2=data[['Combat', 'Strength']].cov().iloc[0,1]
print ("Covariance between Combat and strength is:", covariance2)
intelligence= data.Intelligence.std()
print("Standard deviation intelligence:",intelligence)
strength=data.Strength.std()
print("Standard deviation strength:",strength)
combat=data.Combat.std()
print("Standard deviation combat:",combat)
pearson_intelligence=covariance1/(combat*intelligence)
print("Pearson Corelation between Combat and Intelligence is:",pearson_intelligence)
pearson_strength=covariance2/(combat*strength)
print("Pearson Corelation between Combat and Strength is:",pearson_strength)


quart=data['Total'].quantile(q=0.99)
print (quart)


newdf= data[data['Total']>quart]
super_best_names=[]
super_best_names=newdf['Name'].tolist()

print("super_best_names:\n", super_best_names)





