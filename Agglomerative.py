import matplotlib.pyplot as plt

from sklearn import datasets
x,y=datasets.make_blobs(n_samples=1500,random_state=10)

plt.scatter(x[:,0],x[:,1],c=y)
plt.show()

from scipy.cluster.hierarchy import dendrogram,linkage
from sklearn.cluster import AgglomerativeClustering

# linkage=linkage(x,"average")
# labels=range(1,16)
# dendrogram(linkage,orientation='top',labels=labels,distance_sort="descending",show_leaf_counts=True)

# plt.show()

cluster=AgglomerativeClustering(n_clusters=6,affinity="euclidean",linkage="ward")
cluster.fit_predict(x)

labels=cluster.labels_

plt.scatter(x[:,0],x[:,1],c=labels)
plt.show()