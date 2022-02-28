def fun3(**detail):
                                                                                                                             # for i in fun3:
         
    for key,value in detail.items():  #syntax
          print(key,value)
    
    detail["meet"]="not a name" 
    
    return detail            
          
          
    
   
    

detail={"meet":"name","kishan":"name2"}
x=fun3(**detail)  
print(x)