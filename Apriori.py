import pandas as pd
import numpy as np

data=pd.read_csv("Market_Basket_Optimisation.csv",header=None)#In this dataset there is no column names present so that we use "header=None",If we not added "header=None" it will take first row values as columns


transactions=[]
for i in range(0,7501):
    transactions.append([str(data.values[i,j]) for j in range(0,20)])

from apyori import apriori
rules=apriori(transactions=transactions,min_support=0.003,min_confidence=0.2,min_lift=3,min_length=2,max_length=2)
results=list(rules)
print(results)
# print(results[0])
#print(results[0].ordered_statistics)
#print(results[0].ordered_statistics[0][0])


base=[results.ordered_statistics[0][0] for results in results]
#print(base)

add=[results.ordered_statistics[0][1] for results in results]
#print(add)

supports=[results.support for results in results]
#print(supports)

confidences=[results.ordered_statistics[0][2] for results in results]
# print(confidences)

lift=[results.ordered_statistics[0][3] for results in results]
# print(lift)


li=list(zip(base,add,supports,confidences,lift))
df=pd.DataFrame(li,columns=["LHS","RHS","support","confidence","lift"])






