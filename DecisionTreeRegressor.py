import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("whitegrid")

from sklearn.datasets import load_boston
data=load_boston()

df=pd.DataFrame(data["data"],columns=data["feature_names"])
df["MDEV"]=data["target"]

x=df.loc[:,['RM','LSTAT']].values
y=df.iloc[:,-1].values


from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=1)

from sklearn.tree import DecisionTreeRegressor
regressor=DecisionTreeRegressor()
regressor.fit(x_train,y_train)

y_pred=regressor.predict(x_test)

from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score

r2=r2_score(y_test,y_pred)
mse=mean_squared_error(y_test,y_pred)

print('R2 score: ',r2)
print("MSE: ",mse)