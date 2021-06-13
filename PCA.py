import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("whitegrid")

#Linear data
# rng=np.random.RandomState(1)
# x=np.dot(rng.rand(2,2),rng.randn(2,200)).T

# plt.scatter(x[:,0],x[:,1])
# plt.show()

# from sklearn.decomposition import PCA
# pca=PCA(n_components=1)
# pca.fit(x)

# x_pca=pca.transform(x)
# # reduced=np.dot(data.pca.components_)
# # original=np.dot(reduced,data)

# x_new=pca.inverse_transform(x_pca)

# plt.scatter(x[:,0],x[:,1],alpha=0.4)
# plt.scatter(x_new[:,0],x_new[:,1],alpha=0.8)
# plt.show()


from sklearn.datasets import load_digits
data=load_digits()

def plot_digits(data):
    fig,axes=plt.subplots(4,10,figsize=(10,4),subplot_kw={'xticks':[],'yticks':[]},gridspec_kw=dict(hspace=0.1,wspace=0.1))
    
    for i,ax in enumerate(axes.flat):
        ax.imshow(data[i].reshape(8,8),cmap='binary',interpolation='nearest',clim=(0,16))
        
plot_digits(data.data)

#Adding noise

np.random.seed(42)
noisy=np.random.normal(data.data,4)

plot_digits(noisy)


from sklearn.decomposition import PCA
pca=PCA(0.6)
pca.fit(noisy)

reduced=pca.transform(noisy)
original=pca.inverse_transform(reduced)
plot_digits(original)

















