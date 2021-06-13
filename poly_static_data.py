import  pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("whitegrid")

from sklearn.datasets import load_boston
data=load_boston()


# x=data["data"]
# y=data["target"]

df=pd.DataFrame(data["data"],columns=data["feature_names"])
df["MDEV"]=data["target"]

sns.set(rc={"figure.figsize":(20,15)})
sns.heatmap(df.corr(),annot=True,vmin=-1,vmax=1,center=0)


x=df.loc[:,["RM","LSTAT"]].values
y=df.iloc[:,-1].values

plt.subplot(2,1,1)
plt.scatter(x[:,0],y)
plt.xlabel("RM")
plt.ylabel("MDEV")


plt.subplot(2,1,2)
plt.scatter(x[:,1],y)
plt.xlabel("LSTAT")
plt.ylabel("MDEV")

plt.show()


from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=10)

from sklearn.preprocessing import PolynomialFeatures
poly=PolynomialFeatures(degree=3)

x_train_poly=poly.fit_transform(x_train)
x_test_poly=poly.transform(x_test)

from sklearn.linear_model import LinearRegression
lr=LinearRegression()
lr.fit(x_train_poly,y_train)

y_pred=lr.predict(x_test_poly)



import math
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error
mse=mean_squared_error(y_test,y_pred)
print("MSE:",mse)
rmse=math.sqrt(mse)
print("RMSE:",rmse)
r2=r2_score(y_test,y_pred)
print("R2 score:",r2)




















