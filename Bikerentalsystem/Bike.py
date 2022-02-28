from re import T


class Bike:
    
    def __init__(self,stock):
        self.stock=stock 
    def displayBike(self):
         print("Total Bikes",self.stock) 
    def rentforBike(self,q):
        if q<=0:
            print("Enter the positive value or grater the zero") 
        elif q>self.stock:
            print("Enter the value(less then stock)")
        else:
            self.stock=self.stock-q
            print("total price",q*100)
            print("total bikes Avalible",self.stock) 
obj=Bike(100)               
while True:
    uc=int(input('''
 1 Display stocks
 2 rent Bike
 3 Exit
              ''' ))                   
    
    
    if uc==1:
        obj.displayBike()
    elif uc==2:
        n=int(input("Enter the qty:---"))
        obj.rentforBike(n)
    elif uc==3:
        break    
    else: 
        print("invalid input")
        # obj.displayBike()