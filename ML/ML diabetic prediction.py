import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("diabetes.csv")

print(df.head())
print(df.shape)
print(df.info())
print(df.isnull().sum())

x=df.iloc[:,df.columns!="Outcome"]
y=df.iloc[:,df.columns=="Outcome"]

from sklearn.model_selection import train_test_split
xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.2)
print(xtrain.head())
print(ytrain.head())
print(xtrain.shape)
print(ytrain.shape)
print(ytrain.head())

from sklearn.ensemble import RandomForestClassifier

model=RandomForestClassifier()

model.fit(xtrain,ytrain.values.ravel())#to train the algorithm

predict_output=model.predict(xtest) #to test the algorithm

print(predict_output)

from sklearn.metrics import accuracy_score

acc=accuracy_score(predict_output,ytest)

print("The accuracy score of RF:",acc)
