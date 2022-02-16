# def pypart(n):
     
    # outer loop to handle number of rows
    # n in this case
# for i in range(0, 5):
     
       
#         for j in range(0, i+1):
         
#             # printing stars
#             print("* ",end="")
      
        
#         print("\r")
 
rows = int(input("Enter number of rows: "))

for i in range(rows):
    for j in range(i+1):
        print("* ", end="")
    print("\n")