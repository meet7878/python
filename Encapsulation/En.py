#getter and setter
from unicodedata import name


class student:
    # def __init__(self):
    #     self.__name="" 
    def set(self,name): 
        self.__name=name 
   
   
    def get(self):
        return self.__name
        
        
  
        
         
obj=student()
obj.set("test")
name=obj.get()
print(name)        