import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("whitegrid")

data=pd.read_csv("Real estate.csv")
x=data.iloc[:,1:-1].values
y=data.iloc[:,-1].values

from sklearn.model_selection import train_test_split
x_train,x_test,y_train, y_test = train_test_split(x,y,test_size=0.25,random_state=5)


from sklearn.preprocessing import StandardScaler
sd=StandardScaler()
x_train=sd.fit_transform(x_train)
x_test=sd.transform(x_test)

from sklearn.neighbors import KNeighborsRegressor
knn=KNeighborsRegressor(n_neighbors=15)
knn.fit(x_train, y_train)

y_pred=knn.predict(x_test)

from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
r2=r2_score(y_test,y_pred)
print("R2 score:",r2)

mse=mean_squared_error(y_test, y_pred)
print("MSE:",mse)