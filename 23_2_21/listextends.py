fruits = ['apple', 'banana', 'cherry']

cars = ['Ford', 'BMW', 'Volvo']

fruits.extend(cars)

print(fruits)

#next
myTuple = ("meet", "ved", "Vicky")

x = "#".join(myTuple)

print(x)

#next2

myDict = {"name": "meet", "country": "india"}
add = "demo"
x = add.join(myDict)
print(x)

#next3
myList=[1,2,3]
myList.append(4)
myList.append(5)
myList.append(6)
myList.append(7)
for i in range(9, 11):
   myList.append(i)
   print(myList)
   

# #next4
l=["hello","meet","good","say","hyy"]
print(l[:3]) # 3 before print
print(l[2:]) #2 after value print
print(l[2:4]) #startin ending print
print(l[:])  #all print
print(l[::-1]) #reverse print

#next5
print(min([1, 2, 3]))
print(max([1, 2, 3]))