import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("whitegrid")

from sklearn import datasets

x,y=datasets.make_circles(n_samples=1500,noise=0.06,factor=0.5,random_state=20)
plt.scatter(x[:,0],x[:,1])
plt.show()

from sklearn.preprocessing import StandardScaler
sd=StandardScaler()
x=sd.fit_transform(x)


from sklearn.cluster import DBSCAN
db=DBSCAN(eps=.3).fit(x)

labels=db.labels_

plt.scatter(x[:,0],x[:,1],c=labels)
plt.show()