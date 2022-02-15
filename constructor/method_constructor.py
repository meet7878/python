class method_constructor:
    a=10

    def __init__(self):
        print("welcome")

    def show(self):
        print(self.a)
   
    def meths(self,a,b):
        print(a+b)    

obj=method_constructor()
obj.show()
obj.meths(10,20)        