import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("whitegrid")

from sklearn.datasets import load_iris
data=load_iris()
x=data["data"]
y=data["target"]

plt.scatter(x[y==0,0],x[y==0,1])
plt.scatter(x[y==1,0],x[y==1,1])
plt.scatter(x[y==2,0],x[y==2,1])
plt.xlabel("sepal length")
plt.ylabel("sepal width")
plt.show()

#PCA

from sklearn.decomposition import PCA
pca=PCA(n_components=2)
x_pca=pca.fit_transform(x)
plt.scatter(x_pca[y==0,0],x_pca[y==0,1])
plt.scatter(x_pca[y==1,0],x_pca[y==1,1])
plt.scatter(x_pca[y==2,0],x_pca[y==2,1])
plt.xlabel("sepal length")
plt.ylabel("sepal width")
plt.show()

#LDA

from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
lda=LDA(n_components=2)
x_lda=lda.fit_transform(x,y)
plt.scatter(x_lda[y==0,0],x_lda[y==0,1])
plt.scatter(x_lda[y==1,0],x_lda[y==1,1])
plt.scatter(x_lda[y==2,0],x_lda[y==2,1])
plt.xlabel("sepal length")
plt.ylabel("sepal width")
plt.show()
















