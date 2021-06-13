#single level inheritance
class A:
    
    def __init__(self):
        self.i=10
        
    def tell(self):
        print("In A")
    
class B(A):
    def __init__(self):
        super(B,self).__init__()
        self.name="somethink"
        
    def greed(self):
        print("In B")
        print("Good Morning")
        
obj=B()
print(obj.i)
obj.tell()
obj.greed()

#Multiple inheritance
class A:
    def name(self):
        print("In A")
        
class B:
    def greed(self):
        print("Good morning")

class C(A,B):
    def do_something(self):
        print("hi")
        
obj=C()
obj.name()
obj.greed()
obj.do_something()

#Multi level inheritance
class A:
    def name(self):
        print("In A")
        
class B(A):
    def greed(self):
        print("Good morning")

class C(B):
    def do_something(self):
        print("hi")
        
obj=C()
obj.name()
obj.greed()
obj.do_something()

#Hierarchical inheritance(combination of two inheritance)
class A:
    
    def __init__(self):
        self.i=10
        
    def tell(self):
        print("In A")
    
class B(A):
    def __init__(self):
        super(B,self).__init__()
        self.name="somethink"
        
    def greed(self):
        print("In B")
        print("Good Morning")

class C(A,B):
    def do_something(self):
        print("hi")
        
obj1=C()
obj2=B()
print(obj.i)
obj.tell()
obj.greed()