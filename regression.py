import pandas as pd

data=pd.read_csv("50_Startups.csv")

data=pd.get_dummies(data,columns=["State"])

y=data.loc[:,"Profit"].values
x=data.drop("Profit",axis=1).values

from sklearn.preprocessing import StandardScaler
sd=StandardScaler()
x=sd.fit_transform(x)

from sklearn.linear_model import LinearRegression
linear=LinearRegression()

from sklearn.tree import DecisionTreeRegressor
tree=DecisionTreeRegressor(anacon)

from sklearn.neighbors import KNeighborsRegressor
knn=KNeighborsRegressor(n_neighbors=8)

from sklearn.ensemble import RandomForestRegressor
forest=RandomForestRegressor(n_estimators=15)

from sklearn.svm import SVR
support=SVR(kernel="rbf",gamma=0.001,C=15)


from sklearn.model_selection import KFold,cross_val_score

models=[linear,tree,knn,forest,support]
kfold=KFold(n_splits=10)

for model in models:
    accuracy=cross_val_score(model,x,y,cv=kfold)
    print(model,accuracy.mean())