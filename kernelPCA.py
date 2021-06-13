import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("whitegrid")

# from sklearn.datasets import make_moons,make_circles
# x,y=make_moons(n_samples=500)

# plt.scatter(x[y==0,0],x[y==0,1])
# plt.scatter(x[y==1,0],x[y==1,1])
# plt.show()

# #PCA

# from sklearn.decomposition import PCA
# pca=PCA(n_components=2)
# x_pca=pca.fit_transform(x)

# plt.scatter(x_pca[y==0,0],x_pca[y==0,1])
# plt.scatter(x_pca[y==1,0],x_pca[y==1,1])
# plt.show()

# #kernelPCA

# from sklearn.decomposition import KernelPCA
# kpca=KernelPCA(n_components=2,kernel="rbf",gamma=15)
# x_kpca=kpca.fit_transform(x)

# plt.scatter(x_kpca[y==0,0],x_kpca[y==0,1])
# plt.scatter(x_kpca[y==1,0],x_kpca[y==1,1])
# plt.show()

from sklearn.datasets import make_moons,make_circles
x,y=make_circles(n_samples=500,factor=0.5,noise=0.05)

plt.scatter(x[y==0,0],x[y==0,1])
plt.scatter(x[y==1,0],x[y==1,1])
plt.show()

#PCA

from sklearn.decomposition import PCA
pca=PCA(n_components=2)
x_pca=pca.fit_transform(x)

plt.scatter(x_pca[y==0,0],x_pca[y==0,1])
plt.scatter(x_pca[y==1,0],x_pca[y==1,1])
plt.show()

#kernelPCA

from sklearn.decomposition import KernelPCA
kpca=KernelPCA(n_components=2,kernel="rbf",gamma=15)
x_kpca=kpca.fit_transform(x)

plt.scatter(x_kpca[y==0,0],x_kpca[y==0,1])
plt.scatter(x_kpca[y==1,0],x_kpca[y==1,1])
plt.show()