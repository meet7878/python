#single level inheratance



class A:
     def display(self):
          print("first")

class B(A):
     def show(self):
           print("second")

obj= B()
obj.display()
obj.show()          
    