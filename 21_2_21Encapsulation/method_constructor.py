class method_constructor:
    

    def __init__(self):
        print("welcome")

    def show(self,a):
        print(self,a)
   
    def meths(self,a,b):
        print(a+b)    

obj=method_constructor() #contsrtuctor are call to when you create obj
obj.show(10)
obj.meths(10,20)        