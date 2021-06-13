import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data=pd.read_csv("voice.csv")

from sklearn.preprocessing import LabelEncoder
lb=LabelEncoder()
data["label"]=lb.fit_transform(data["label"])

sns.pairplot(data)

sns.set(rc={"figure.figsize":(15,10)})
sns.heatmap(data.corr(),annot=True)

x=data.loc[:,["sd","Q25","IQR","sp.ent","meanfun"]].values#We put values for converting to array
y=data.iloc[:,-1].values


plt.scatter(x[:,0],x[:,1],c=y)
plt.xlabel("sd")
plt.ylabel("Q25")
plt.show()



from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.25,random_state=0)

from sklearn.svm import SVC
classifier=SVC(kernel="linear",C=100,gamma=0.1)#we can select gamma value as 0.1 to 0.001
# classifier=SVC(kernel="rbf",C=2,gamma=0.01)
# classifier=SVC(kernel="poly",degree=2,gamma=0.01)
classifier.fit(x_train,y_train)

y_pred=classifier.predict(x_test)

from sklearn.metrics import confusion_matrix
cm=confusion_matrix(y_test,y_pred)

print(classifier.score(x_test,y_test))


#GridSearchCV---->It automatillay detect the C value and its accuracy in that we can find percentage 

# from sklearn.model_selection import GridSearchCV
# params={"C":[1,2,3,10,100],"gamma":[0.1,0.01,0.001,0.0001]}
# cv=GridSearchCV(SVC(kernel="rbf"),param_grid=params,verbose=10,scoring="accuracy")
# cv.fit(x_train,y_train)

