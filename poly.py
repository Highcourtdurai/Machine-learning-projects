#Method overriding
#Method overloading
#Operator overloading

#Method ovrriding
class A:
    def __init__(self):
        print("Constructor of A")
    def name(self):
        print("In A")
        
class B:
    def name(self):
        print("Good morning")

class C(B,A):
    def do_something(self):
        print("hi")
        
obj=C()
obj.name()
obj.do_something()

#In python there is no over loading

# def greed():
#     pring("Good morning")

# def greed(person):
#     print("Hi",person)

def add(*args):
    print(sum(args))

add(1,2)
add(1,2,3)
add(1,2,3,4)



a=5 
b=10

print(a)

#Magical methods
class Integer:
    def __init__(self,value):
        self.i=value
    
    def __add__(self,other):
        return self.i+other.i
    
    def __sub__(self,other):
        return self.i-other.i
    
    def __gt__(self,other):
        return self.i>other.i


c=Integer(5)
d=Integer(10)
print(c+d)
print(c-d)
print(c>d)


class EvenList:
    def __init__(self,*args):
        self.values=list(self.even(args))
        
        
    def append(self,value):
        if value%2==0:
            self.values.append(value)
            
    
    def even(self,li):
        return filter(lambda x:x%2==0,li)
    
    def __str__(self):
        return " ".join(map(str,self.values))
    
    def __repr__(self):
         return " ".join(map(str,self.values))
    
    def extend(self,li):
        for i in li:
            if i%2==0:
                self.values.append(i)
    
    def __add__(self,other):
        li=[]
        if isinstance(self,EvenList) and isinstance(other,EvenList):
            li.extend(self.values)
            li.extend(other.values)
            return li
        else:
            print("Different objects")
            
        
    
li=EvenList(10,34,57,86,103,108,231)
li.append(10)
li.extend([30,33,45,84,98])

li2=[3,5,7,6,34,21]

print(li+li2)
print(li)
    



# str1="Hello world"
# for ch in str1:
#     print(ch)
    
# it=iter(str1)
# while True:#infinity loop
#     try:
#         ch=next(it)
#         print(ch)
#     except StopIteration:
#         break
    
# it=iter(str1) #- __iter__
# print(next(it)) #- __next__
# print(next(it)) #- __next__
