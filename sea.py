import seaborn as sns
import pandas as pd

titanic=pd.read_csv("train.csv")
sns.set_style("whitegrid")
sns.distplot(x="Pclass",data=titanic)
