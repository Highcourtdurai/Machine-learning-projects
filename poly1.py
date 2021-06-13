a=10


def greed():
    print("Hi")

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
            
        
