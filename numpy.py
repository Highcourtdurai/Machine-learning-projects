import numpy as np

import sys
a=np.array([1,2,3,4,5,6,7,8,9,10])
print(a)

# arr=np.array([1,2,3,4,5])
# print(len(arr)*arr.size)


"""li=[1,2,3,5,6,723,45]
print(sys.getsizeof(li)*len(li))

print(a.size*a.itemsize)"""

# import time
# a=np.arange(1000)
# b=np.arange(1000)

# start=time.time()
# print(a+b)
# end=time.time()
# print((end-start)*1000)#To multiply with 1000 to convert milli seconds into seconds

# import time
# a=list(range(10000))
# b=list(range(10000))

# start=time.time()
# print([i+j for i,j in zip(a,b)])
# end=time.time()
# print((end-start)*1000)

# a=np.arange(1,100)
# b=np.arange(1,100)
# print(a,b)
# linspace=np.linspace(1,20)
# print(linspace)


"""import time
size=1000000
li=range(size)
li2=range(size)
start=time.time()

result=[a+b for a,b in zip(li,li2)]
print((time.time()-start)*1000)

a=np.arange(size)
b=np.arange(size)
start=time.time()

result=a+b"""

# random=np.random.random(100)
# print(random)


normal=np.random.normal(size=100)
print(normal)#Mean=0,S.D=1

#calculate dimension
"""a=np.array([(1,2,3,4,5),(6,7,8,9,10)])
print(a.ndim)
print(a.size)
print(a.itemsize)
print(a.shape)#shape shows how many rows and columns
print(a.reshape(5,2))#we can change the rows and columns 

print(a[0,1])
print(a[:,1:4])#slicing"""

a=np.array([(1,2,3,4,5),(6,7,8,9,10)])
b=np.array([(1,2,3,4,5),(6,7,8,9,10)])
print(a+b)
print(a-b)
print(a*b)
print(a/b)

#concadination
# print(np.vstack((a,b)))#vstack-vertical stack
# print(np.hstack((a,b)))#hstack-horizontal stack

# print(a.ravel())#converts high to low dimension

# print(np.sqrt(a))

# print(np.std(b))

# print(np.sin(a))

# print(np.cos(b))

# print(np.exp(b))

# print(np.log(a))

# print(a.min())#minimum value

# print(b.max())#maximum value

# print(a.sum())#sum value

print(a.mean())
print(a.std())