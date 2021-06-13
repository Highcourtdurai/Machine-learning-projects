import matplotlib.pyplot as plt

"""plt.plot([1,2,3,4],[2,5,6,8],c="r",linewidth=5,marker="o")
plt.title("Basic plot")
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.grid(True)
plt.show()"""


#Bar graph
"""x=["t","e","m","s","ss"]
y=[92,75,86,68,77]
plt.bar(x,y,color="g",label="std1",width=0.5)#width-changes width,default width=0.8
plt.bar(["c","p","a"],[60,67,66],color="r",label="std2")
plt.title("Basic plot")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.grid(True)
plt.legend()
plt.show()"""

#Histogram 
"""x=[25,35,123,45,67,87,98,54,65,35,54,32]
y=[3,6,43,76,85,91,100,110,120,130,140,150]
plt.hist(x,bins=y)
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.show()"""

#pie chart
"""x=["t","e","m","s","ss"]
y=[92,75,86,68,77]
plt.pie(y,labels=x,colors=["b","r","g","y","c"],autopct="%.1f%%",shadow=True,explode=(0,0,1,0,0),startangle=90)#explode=cut and show outside the pie chart
plt.legend()
plt.show()"""

#Scatter plot
x=[34,76,87,54,23,65,45]
y=[45,65,76,88,93,100,43]
plt.scatter(x, y,marker="o")
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.show()

plt.plot([1,2,3,5],[3,5,2,1],c="r",linewidth=3,marker="o",label="line1")
plt.plot([1,2,3,5],[4,6,8,10],c="g",linewidth=3,marker="o",label="line1")
plt.title("Basic plot")
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.grid(True)
plt.legend()
plt.show()

import random

li=[random.randint(0,100) for i in range(100)]
bins=[0,25,30,75,100]

plt.hist(li,bins=bins)
plt.show()