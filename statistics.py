import random

weights=[random.randint(2, 100) for i in range(100)]

print(weights)

import numpy
weights=numpy.array(weights)

mean=numpy.mean(weights)
print(mean)

median =numpy.median(weights)
print(median)


from scipy import stats
mode=stats.mode(weights)
print(mode)

#standard deviation
stdev=weights.std()
print(stdev)

import matplotlib.pyplot as plt
plt.plot([2,4,6,8,10])
plt.show()

#Bar chart
#plt.bar([2,4,6,8,10],[1,2,3,4,5])
plt.bar(["t","e","m","s","ss"],[1,2,3,4,5])
plt.show()

#histogram
#plt.hist([2,4,6,8,10],[1,2,3,4,5])
plt.hist([2,4,6,8,10],[3,6,9,12,15])
plt.show()

#pie chart
plt.pie([71,92,73,84,65],labels=["t","e","m","s","ss"],autopct="%.1f%%")
plt.show()

#Boxplot
plt.boxplot([2,4,6,8,11,13,54,32,66,43])
plt.show()

