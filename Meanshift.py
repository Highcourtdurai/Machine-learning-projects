import matplotlib.pyplot as plt

from sklearn import datasets
x,y=datasets.make_blobs(n_samples=1500,random_state=10)

plt.scatter(x[:,0],x[:,1],c=y)
plt.show()

from sklearn.cluster import MeanShift,estimate_bandwidth
bandwidth=estimate_bandwidth(x,quantile=0.2,n_samples=1000)
cluster=MeanShift(bandwidth=bandwidth)
cluster.fit(x)

labels=cluster.predict(x)

plt.scatter(x[:,0],x[:,1],c=labels)
plt.show()