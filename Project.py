import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("student_data.csv")
print(df.head())

df.describe()
df.info()
df.isnull().sum()

df=df.drop("Unnamed: 0", axis=1)
print(df.head())

df["WklyStudyHours"]=df["WklyStudyHours"].str.replace("05-Oct","5-10")
df.head()


plt.figure(figsize=(6,6))
ax=sns.countplot(data=df,x="Gender")
ax.bar_label(ax.containers[0])
plt.title("GENDER DISTRIBUTION")
plt.show()
gb=df.groupby("ParentEduc").agg({"MathScore":'mean',"ReadingScore":"mean","WritingScore":"mean"})
print(gb)


plt.figure(figsize=(4,5))
sns.heatmap(gb,annot=True)
plt.title("Relationship between parent's Education and Student Score")
plt.show()
gb1=df.groupby("ParentMaritalStatus").agg({"MathScore":'mean',"ReadingScore":"mean","WritingScore":"mean"})
print(gb1)


plt.figure(figsize=(3,3))
sns.heatmap(gb1,annot=True)
plt.title("Relationship between parent's Marital Status and Student Score")
plt.show()

sns.boxplot(data=df,x="MathScore")
plt.title("Outliers based on Math Score")
plt.show()

sns.boxplot(data=df,x="ReadingScore")
plt.title("Outliers based on Reading Score")
plt.show()

sns.boxplot(data=df,x="WritingScore")
plt.title("Outliers based on Writing Score")
plt.show()

print(df["EthnicGroup"].unique())
groupA=df.loc[(df['EthnicGroup']=="group A")].count()
groupB=df.loc[(df['EthnicGroup']=="group B")].count()
groupC=df.loc[(df['EthnicGroup']=="group C")].count()
groupD=df.loc[(df['EthnicGroup']=="group D")].count()
groupE=df.loc[(df['EthnicGroup']=="group E")].count()

l=["group A","group B","group C","group D","group E"]
mlist=[groupA["EthnicGroup"],groupB["EthnicGroup"],groupC["EthnicGroup"],groupD["EthnicGroup"],groupE["EthnicGroup"]]

plt.pie(mlist,labels=l,autopct="%1.2f%%")
plt.title("Distribution Of Ethnic Groups")
plt.show()

ax=sns.countplot(data=df,x='EthnicGroup')
ax.bar_label(ax.containers[0])

