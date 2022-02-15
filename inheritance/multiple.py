#multiple inheratance



class A:
     def display(self):
          print("first")

class B:
     def show(self):
           print("second")
           
class C(A,B):
     def  demo(self):
           print("third")           

obj= C()
obj.display()
obj.show()  
obj.demo()        
    