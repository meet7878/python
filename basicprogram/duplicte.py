from re import L


n=int(input("Enter num"))
L=[]

for i in range(n):
    s=input("enter the num")
    L.append(s)

print("my list",L)         
nonduplicate=set(L)
print(nonduplicate)