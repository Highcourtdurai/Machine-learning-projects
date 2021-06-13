import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data=pd.read_csv("Real estate.csv")
print(data.columns)
sns.pairplot(data)

print(data.isna().sum())

x=data.iloc[:,:-1].values
y=data.iloc[:,-1].values

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=0)

from sklearn.preprocessing import StandardScaler
sd=StandardScaler()
x_train=sd.fit_transform(x_train)
x_test=sd.transform(x_test)

from sklearn.linear_model import LinearRegression
lr=LinearRegression()
lr.fit(x_train,y_train)

y_pred=lr.predict(x_test)

import math
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error
mse=mean_squared_error(y_test,y_pred)
print("MSE:",mse)
rmse=math.sqrt(mse)
print("RMSE:",rmse)
r2=r2_score(y_test,y_pred)
print("R2 score:",r2)
