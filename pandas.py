# series-1 dimension
# dataframe-2 dimension
# panel-3 dimension
import numpy as np
import pandas as pd

s=pd.Series([1,2,3,4,5])
print(s)

s=pd.Series([81,92,73,64,95],index=["sub1","sub2","sub3","sub4","sub5"],dtype=np.float64)
print(s)

li=[["A",43],["B",45],["C",54],["D",42]]
df=pd.DataFrame(li,columns=("Sub","Marks"))
print(df)

dfd=pd.DataFrame({"Sub":["A","B","C","D","E"],"Marks":[98,67,54,65,78]})
dfd2=dfd.set_index("Sub")
print(dfd2)

dfd=pd.DataFrame({"Sub":["A","B","C","D","E"],"Marks":[98,67,54,65,78]})
dfd.set_index("Sub",inplace=True)#inplace used for change the existing values
print(dfd)

dfd=pd.DataFrame({"Marks":[98,67,54,65,78]},index=["A","B","C","D","E"])
print(dfd)


"""df=pd.DataFrame({"subjects":["t","e","m","s","ss"],"marks":[87,77,86,97,54]})
print(df.head(3))
print(df.tail(2))

print(df.loc[df["marks"]>=90])

print(df.loc[[1,3],"marks"])

df.set_index('subjects',inplace=True)
print(df.loc["t":"s","marks"])

print(df.iloc[1:3,1])#we can use only integers but not characters"""


"""df=pd.DataFrame({"marks":[87,77,86,97,54]},index=["t","e","m","s","ss"])
df2=pd.DataFrame({"names":["ff","gg","fr","de","ll"]},index=["t","e","m","s","ss"])
#result=pd.merge(df,df2,on="subjects")
joining=df.join(df2)"""

import matplotlib.pyplot as plt
df=pd.read_csv("Data.csv")
df.to_html("data.html")
df.plot(kind="scatter",x="Age",y="Salary")
df.plot()
plt.show()


titanic=pd.read_csv("train.csv")
print(titanic.head(10))
print(titanic.tail(10))
print(titanic.info())
print(titanic.describe())

grouped=titanic.groupby("Sex")
print(grouped.head())

print(grouped.mean())

print(titanic.loc[0:10,"PassengerId":"Pclass"])

print(titanic.loc[0:10,["PassengerId","Name"]])

print(titanic.iloc[0:20,0:3])#we can use only index values in iloc

print(titanic[titanic.Pclass==3])#shows pclass 3 values only

print(titanic[(titanic.Pclass==3)&(titanic.Survived==1)])


titanic.to_excel("out.xlsx")
titanic.to_html("out.html")
