"""import random
import numpy as np
weights=[random.random()*10 for i in range(100)]
sample=[random.choice(weights) for i in range(20)]
mean=np.mean(weights)

from scipy import stats

ttest,p_value=stats.ttest_1samp(sample,mean)
if p_value>=0.05:
    print("Accept the null hypothesis")
else:
    print("Reject the null hypothesis")"""

"""import random
import numpy as np
age=[random.randint(1, 100) for i in range(100)]
weights=[random.randint(1, 100) for i in range(100)]
sample=[random.choice(weights) for i in range(20)]
mean=np.mean(weights)

from scipy import stats

ttest,p_value=stats.ttest_ind(age, weights)
if p_value>=0.05:
    print("Accept the null hypothesis")
else:
    print("Reject the null hypothesis")"""

#Correlation    
"""import seaborn as sns
data=sns.load_dataset("iris")
print(data.corr())   """ 
    
#Chi-square
import seaborn as sns
import pandas as pd
data=sns.load_dataset("tips")
table=pd.crosstab(data["sex"],data["smoker"]).values

from scipy.stats import chi2_contingency
expected=chi2_contingency(table)
expected=expected[3]

chi_square=[(0-e)**2/e for o,e in zip(table,expected)]
chi_square=sum(chi_square)

dof=(2-1)*(2-1)

from scipy.stats import chi2

p_value=chi2.cdf(chi_square,df=dof)


