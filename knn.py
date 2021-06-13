import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("whitegrid")

# import random
# li=[random.randint(0,100) for i in range(100)]

# classes=[0,1,2]
# classli=[random.choice(classes) for i in range(100)]

# from sklearn.datasets import make_classification
# x,y=make_classification(n_samples=200,n_classes=3,n_features=5,n_redundant=0,n_informative=3)

# from sklearn.model_selection import train_test_split
# x_train,x_test,y_train, y_test = train_test_split(x,y,test_size=0.25,random_state=0)

# from sklearn.neighbors import KNeighborsClassifier
# knn=KNeighborsClassifier(n_neighbors=3)
# knn.fit(x_train, y_train)

# y_pred=knn.predict(x_test)

# from sklearn.metrics import confusion_matrix
# cm=confusion_matrix(y_test,y_pred)

# print(knn.score(x_test,y_test))


from sklearn.datasets import load_iris
data=load_iris()
# print(data["feature_names"])
# print(data["target_names"])

df=pd.DataFrame(data["data"],columns=data["feature_names"])
df["class"]=data["target"]

sns.set(rc={"figure.figsize":(15,7)})
sns.scatterplot(x="sepal length (cm)",y="sepal width (cm)",data=df,hue="class")

sns.pairplot(df,hue="class")

x=df.iloc[:,:-1].values
y=df.iloc[:,-1].values

from sklearn.model_selection import train_test_split
x_train,x_test,y_train, y_test = train_test_split(x,y,test_size=0.25,random_state=0)

from sklearn.neighbors import KNeighborsClassifier
knn=KNeighborsClassifier(n_neighbors=1)
knn.fit(x_train,y_train)

y_pred=knn.predict(x_test)


from sklearn.metrics import confusion_matrix
cm=confusion_matrix(y_test,y_pred)




















