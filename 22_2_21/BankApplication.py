class bank:
   AccountNo=int(input("Enter the Acoount Number:\n"))
   Couster_Name=input("Enter the customer Name:\n")
   Branch_code=input("Enter the Brnch Code:\n")
   mobile=int(input("Enter the mobile Num:\n")) 
   city=input("Enter the city:\n") 
   country=input("Enter the country\n")

    
   def __init__(self):
        self.Balance=0
        print("please withdraw and deposite to money")
       
   
      
       
   def showAcDetails(self):
        print("Account Number is:",self.AccountNo) 
        print("Customer Name is:",self.Couster_Name)
        print("Branch code is:",self.Branch_code)
        print("mobile Num is",self.mobile)
        print("your city are:",self.city)
        print("country are:",self.country)  
       
            
        
   def deposite(self):
       amount=float(input("please Enter amount "))
       self.Balance+=amount
       print("inserted money are",self.Balance)
       
   def withdraw(self):
       amount=float(input("please withdraw money"))
       
       if self.Balance>=amount:
          self.Balance-=amount
          print("you withdraw money",self.Balance)  
       else:
           print("\n Insuffincent Balance ") 

           
   def display(self):
       print("Available money are",self.Balance)
                              
        

        
obj=bank()

obj.showAcDetails()
obj.deposite()
obj.withdraw()
obj.display()
     