

from re import X


age=[1,2,3,4,18,59]

def fun(x):
    if x<18:
        return False
     
    else:
        return True
    
result=list(filter(fun,age))
print(result)

