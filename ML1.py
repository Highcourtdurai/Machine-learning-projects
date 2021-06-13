import numpy as np
import pandas as pd
import matplotlib.pyplot

df=pd.read_csv("Data.csv")
print(df.corr())

#print(df["Age"].isna().value_counts())#To find how many null values by column vise
#print(df.info())#To find total information

#values={"Age":df["Age"].mean(),"Salary":df["Salary"].mean()}#To fill the Nan values
#df.fillna(value=values,inplace=True)

# pd.get_dummies(df,columns=["country"]).head()#like encoding
# values={"Purchased":{"No":0,"Yes":1}}
# df=df.replace(values)
 

# df=pd.get_dummies(df,columns=["country"])#anathor method like encoding

x=df.iloc[:,0:3].values
y=df.iloc[:,-1].values
print(x)
print(y)

from sklearn.impute import SimpleImputer
# sm=SimpleImputer(missing_values=pd.NA,strategy="mean")
# x[:,1:]=sm.fit_transform(x[:,1:])

imputer=SimpleImputer()
x[:,1:3]=imputer.fit_transform(x[:,1:3])

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder

ct=ColumnTransformer(transformers=[("encode",OneHotEncoder(),[0])],remainder="passthrough")
x=ct.fit_transform(x)

lb=LabelEncoder()
y=lb.fit_transform(y)

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=30)

from sklearn.preprocessing import StandardScaler
sd=StandardScaler()
x_train=sd.fit_transform(x_train)
x_test=sd.transform(x_test)



