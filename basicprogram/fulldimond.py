def triangle(n):
     
    
    k = n - 1
 
    
    for i in range(0, n):
           
        for j in range(0, k):
            print(end=" ")        
        k = k - 1
             
        for j in range(0, i+1):                   
            print("* ", end="")             
        print("\r")
 
n = int(input("Enter number of rows: "))
triangle(n)

num=4

for i in range(num,0,-1):
    for j in range(0,num-i):
        print(end=" ")
    for j in range(0,i):
        print("*",end=" ")
    print()        