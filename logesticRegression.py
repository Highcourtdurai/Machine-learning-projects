import  pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("whitegrid")

from sklearn.datasets import make_classification
x,y=make_classification(n_samples=200,n_features=2,n_classes=2,n_redundant=0)


sns.set(rc={"figure.figsize":(10,7)})
sns.scatterplot(x=x[:,0],y=x[:,1],hue=y)

from sklearn.model_selection import train_test_split
x_train, x_test,y_train, y_test = train_test_split(x,y,test_size=0.25,random_state=0)

from sklearn.linear_model import LogisticRegression
lr=LogisticRegression()
lr.fit(x_train, y_train)

y_pred=lr.predict(x_test)
# print(lr.predict_proba(x_test))

# y_pred=(lr.predict_proba(x_test)>=0.3)

from sklearn.metrics import confusion_matrix
cm=confusion_matrix(y_test,y_pred)



