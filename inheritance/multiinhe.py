#multi level inheratance



class A:
     def display(self):
          print("first")

class B(A):
     def show(self):
           print("second")
           
class C(B):
     def  demo(self):
           print("third")           

obj= C()
obj.display() 
obj.demo()
obj.show()       
    