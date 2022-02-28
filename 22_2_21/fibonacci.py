n=int(input("Enter the num"))
x=0
y=1
z=0
  
  
for i in range(n):
    
    x=y
    y=z
    z=x+y
    print(z,end="")       
    
    #output 11235
    