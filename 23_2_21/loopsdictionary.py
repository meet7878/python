dic1 =	{
  "meet": "hello",
  "ved": "hello",
  "year": 2022
}
for x in dic1:
   print(dic1[x])
   
print("\n")   

for x in dic1.values():
      print(x)
print("\n")       
  
for x, y in dic1.items():
      print(x, y)

dic1["color"]="red"
print(dic1)


# dic1.clear()
# print(dic1)