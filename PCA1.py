#Random forest reggressor data

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("whitegrid")

from sklearn.datasets import load_boston
data=load_boston()

df=pd.DataFrame(data["data"],columns=data["feature_names"])
df["MDEV"]=data["target"]

x=df.iloc[:,:-1].values
y=df.iloc[:,-1].values


from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.25,random_state=1)


from sklearn.preprocessing import StandardScaler
sd=StandardScaler()
x_train=sd.fit_transform(x_train)
x_test=sd.transform(x_test)

from sklearn.decomposition import PCA
pca=PCA(n_components=5)
x_train=pca.fit_transform(x_train)
x_test=pca.transform(x_test)


pca=PCA().fit(x)
plt.plot(np.cumsum(pca.explained_variance_ratio_))

from sklearn.ensemble import RandomForestRegressor
regressor=RandomForestRegressor(n_estimators=10)
regressor.fit(x_train,y_train)

y_pred=regressor.predict(x_test)

from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score

r2=r2_score(y_test,y_pred)
mse=mean_squared_error(y_test,y_pred)

print('R2 score: ',r2)
print("MSE: ",mse)