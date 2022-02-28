class A:
    def meth1(self):
        print("Test 1")
        
class B(A):
    def meth1(self):
        
        print("Test2")
        super().meth1()    
obj=B()
obj.meth1() 


      
            