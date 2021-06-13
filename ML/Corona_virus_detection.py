#Aim - To predict a conformed cases

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import warnings
warnings.filterwarnings('ignore')

covid=pd.read_csv("covid_19_india.csv")

print(covid.head())

covid['State/UnionTerritory'].unique()

df=covid.loc[(covid['State/UnionTerritory']=="Tamil Nadu")]

import plotly.offline as py
import plotly.graph_objs as go

cured_rate=go.Scatter(x=df['Date'],y=df['Cured'],name='Cured Rate')
death_rate=go.Scatter(x=df['Date'],y=df['Deaths'],name='Death Rate')
py.iplot([cured_rate,death_rate])

df1=df["Confirmed"]

df1=df1.values
print(type(df1))

train_size=int(len(df1) * 0.80) #80%
test_size=len(df1) - train_size #20%

train,test=df1[0:train_size,:],df1[train_size:len(df1),:]
print(test)

def create_dataset(dataset,look_back=1):
    datax.datay=[],[]
    for i in range(len(dataset)-look_back-1):
        a=dataset[i:(i+look_back),0]
        datax.append(a)
        datay.append(dataset[i+look_back,0])
    return np.array(datax),np.array(datay)

look_back=2
trainx,trainy=create_dataset(train,look_back=look_back)
testx,testy=create_dataset(test,look_back=look_back)

from sklearn.linear_model import LinearRegression
model=LinearRegression()

model.fit(trainx,trainy) #train

predict1=model.predict(testx)

df=pf.DataFrame({'Actual':testy.flatten(),'Predicted':predict1.flatten()})

print(df)

df.plot(kind='bar',figsize=(16,10))



