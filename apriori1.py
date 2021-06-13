import pandas as pd
import numpy as np

import csv
with open("groceries.csv","r") as file:
    data=csv.reader(file)
    data=pd.DataFrame(data)


transactions=[]
for i in range(0,9835):
    transactions.append([str(data.values[i,j]) for j in range(0,32)])

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






