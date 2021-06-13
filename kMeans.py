import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("whitegrid")

from sklearn import datasets

x,y=datasets.make_blobs(n_samples=1500,random_state=10)
#x,y=datasets.make_circles(n_samples=1500,noise=0.05,factor=0.5) -- In this datasets we cannot do clustering because of circle so we go for DBSCAN


plt.scatter(x[:,0],x[:,1],c=y)
plt.show()

from sklearn.cluster import KMeans
kmeans=KMeans(n_clusters=2)
kmeans.fit(x)

#print(kmeans.cluster_centers_)
#print(kmeans.inertia)

centroids=kmeans.cluster_centers_
y_pred=kmeans.predict(x)
plt.scatter(x[:,0],x[:,1],c=y_pred)
plt.scatter(centroids[:,0],centroids[:,1],marker="*",c="r")
plt.show()

#To find how many clusters are there so we need [ELBOW METHOD]

inertias=[]
for i in range(1,11):
    kmeans=KMeans(n_clusters=i)
    kmeans.fit(x)
    inertias.append(kmeans.inertia_)

plt.plot(inertias,marker="o")
plt.title("Elbow method")
plt.show()