class human:
    hands=2
    legs=2
    
    def __init__(self,name):#init variable #non static method
        self.__name=name
        
    def walk(self):#non static method
        print(self.__name)
        print("Human can walk with {} legs".format(human.legs))
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self,value):
        self.__name=value
        
    @name.deleter
    def name(self,value):
        del self.__name
    
    @classmethod
    def write(cls):#non static method
        print("Human can walk with {} hands".format(human.hands))
        
    @staticmethod
    def greed():
        print("Good morning")
    
    def __del__(self):#non static method
        print("Deleted")

#constructor-->()

#variable types:
#class variables
#init variables

durai=human("durai")

durai.name="High court durai"

print(durai.name)#init variables

human.greed()


human.hands=3
print(durai.hands)
print(durai.legs)

del durai.name

print(human.write())

durai.walk()#or human.walk(self)#self -current working object

#del durai #used when durai variable is deleted

#getter,setter,deletter

#Method types:
#Non-static method
#static method
#

#Access modifiers:
#private(__name)
#public(name)
#protected