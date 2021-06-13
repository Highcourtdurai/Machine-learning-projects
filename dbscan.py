import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("whitegrid")

from sklearn import datasets

x,y=datasets.make_blobs(n_samples=1500,random_state=10)
plt.scatter(x[:,0],x[:,1])
plt.show()


from sklearn.cluster import DBSCAN

db=DBSCAN(eps=1,min_samples=3).fit(x)

labels=db.labels_

plt.scatter(x[:,0],x[:,1],c=labels)
plt.show()