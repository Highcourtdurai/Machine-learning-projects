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

from sklearn.ensemble import RandomForestClassifier
classifiers=RandomForestClassifier(n_estimators=5,criterion='gini',)
classifiers.fit(x_train,y_train)

#print(classifiers.estimators_) Use the comment in run window

y_pred=classifiers.predict(x_test)

from sklearn.metrics import confusion_matrix
cm=confusion_matrix(y_test,y_pred)

print(classifiers.score(x_test,y_test))

import pydotplus # (We can see the image of the tree in this IDE itself)


from sklearn.tree import export_graphviz

for i in range(0,len(classifiers.estimators_)):
    tree=export_graphviz(classifiers.estimators_[i],out_file=None,feature_names=['sepal_lengthCm','sepal_widthCm','petal_lengthCm','petal_widthCm'],class_names=['setosa','versicolor','virginica'],rounded=True,proportion=False,precision=2,filled=True)
    graph=pydotplus.graph_from_dot_data(tree)
    graph.write_png("tree%d.png"%(i))
    
    
    
    
    
    
    
    
    
    
    
    