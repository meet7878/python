import array as ar

#print max value
a=[]
size=int(input("Enter size of the list index:"))
for i in  range(size):
     val=int(input("Enter the Number inside the index "))
     a.append(val)

max=a[0]       
for i in range(size):
    if(a[i]>max):
        max=a[i]
print("max number =",max) 
print("\n") 

# #print First max value and second max value
# print("Next program are.........:-")
# print("First max value and second max value:-")
# a=[]
# size=int(input("Enter the total index"))
# for i in range(size):
#   value=int(input("Ente value inside index"))
#   a.append(value)    
# a.sort()
# print(" first max value=",a[size-1])
# print(" second max value=",a[size-2])
# print("\n")
       

# #minimum Array value print heare...
# print("Next program are.........:-") 
# print(" minimum  value :-")                                                                                                    
# a=[]
# size=int(input("Enter size of the list index:-"))
# for i in  range(size):
#      val=int(input("Enter the Number inside the index:-"))
#      a.append(val)

# min=a[0]       
# for i in range(size):
#     if(a[i]<min):
#         min=a[i]
# print("min number =",min)
# print("\n")  

# print("Next program are.........:-")
# print("First min value and second min value:-")
# #print the first min value and second min value
# a=[]
# size=int(input("Enter the total index:-"))
# for i in range(size):
#   value=int(input("Ente value inside index:-"))
#   a.append(value)    
# a.sort()
# print(" first min value=",a[0])
# print(" second min value=",a[1])
       



      