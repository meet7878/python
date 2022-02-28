class speed:
     
     def __init__(self):
         self.speed =10 #public
         self.__speed_limit = 20#private
         self.__speed__cross =30#private
     
     def getspeed (self):
             return self.speed
 
     def getspeed_limit(self):
             return self.__speed_limit       
     
     def getcrosslimit(self):
             return self.__speed__cross 

obj=speed()
obj.speed =100 #not data hiding
obj.__speed_limit=200 #not print because speed limit variable are private
obj.__speed__cross=300
print(obj.getspeed(),obj.getspeed_limit(),obj.getcrosslimit())   