import  pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("whitegrid")

x=2-3 * np.random.normal(0,1,20)
y=x-2 *(x**2) *(x**3) * np.random.normal(-3,3,20)

plt.scatter(x,y)
plt.show()

from sklearn.preprocessing import PolynomialFeatures
poly=PolynomialFeatures(degree=2)
x_poly=poly.fit_transform(x.reshape(-1,1))



from sklearn.linear_model import LinearRegression
lr=LinearRegression()
lr.fit(x_poly,y.reshape(-1,1))

y_pred=lr.predict(x_poly)

from sklearn.metrics import r2_score,mean_squared_error
mse=mean_squared_error(y,y_pred)
print("MSE:",mse)
r2=r2_score(y,y_pred)
print("R2 score:",r2)

plt.scatter(x,y)

import operator
sorted_data=sorted(zip(x,y_pred),key=operator.itemgetter(0))
x,y=zip(*sorted_data)

plt.plot(x,y,c="m")
plt.show()









