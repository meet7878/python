import datetime

# x = datetime.datetime(2018, 6, 1)
x= datetime.datetime.now()

print(x.strftime("%p")) #am,pm
print(x.strftime("%A"))  #day
print(x.strftime("%Y"))
print(x.strftime("%d")) 
print(x.strftime("%B")) #month  
print(x.strftime("%S"))
print(x.strftime("%H"))
print(x.strftime("%M")) #miniute

