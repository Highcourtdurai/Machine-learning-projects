import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("whitegrid")

data=pd.read_csv("iris.csv")

x=data.iloc[:,:-1].values
y=data.iloc[:,-1].values

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.25,random_state=0)

from sklearn.tree import DecisionTreeClassifier
classifier=DecisionTreeClassifier()
classifier.fit(x_train,y_train)


#To view Tree diagram
from sklearn.tree import export_graphviz
export_graphviz(classifier,out_file='tree.dot',feature_names=['sepal_lengthCm','sepal_widthCm','petal_lengthCm','petal_widthCm'],class_names=['setosa','versicolor','virginica'],rounded=True,proportion=False,precision=2,filled=True)



y_pred=classifier.predict(x_test)

from sklearn.metrics import confusion_matrix
cm=confusion_matrix(y_test,y_pred)

print(classifier.score(x_test,y_test))

