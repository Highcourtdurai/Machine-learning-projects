import  pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("whitegrid")

data=pd.read_csv("Prostate_Cancer.csv")

from sklearn.preprocessing import LabelEncoder
lb=LabelEncoder()
data["diagnosis_result"]=lb.fit_transform(data["diagnosis_result"])


sns.set(rc={"figure.figsize":(10,7)})
sns.heatmap(data.corr(),annot=True,vmin=-1,vmax=1,center=0)

x=data.loc[:,["perimeter","area","compactness"]].values
y=data.iloc[:,1].values

from sklearn.model_selection import train_test_split
x_train, x_test,y_train, y_test = train_test_split(x,y,test_size=0.25,random_state=0)

from sklearn.preprocessing import StandardScaler
sd=StandardScaler()
x_train=sd.fit_transform(x_train)
x_test=sd.transform(x_test)

from sklearn.linear_model import LogisticRegression
lr=LogisticRegression()
lr.fit(x_train, y_train)

y_pred=lr.predict(x_test)

print(lr.score(x_test,y_test))#To find accuracy

from sklearn.metrics import confusion_matrix
cm=confusion_matrix(y_test,y_pred)
print(cm)




