def Func(self):
      return self['car']

car = [
  {'car': 'Ford', 'year': 2005},
  {'car': 'Mitsubishi', 'year': 2000},
  {'car': 'BMWww', 'year': 2019},
  {'car': 'VW', 'year': 2011}
]

car.sort(key=Func)
print(car)



# #   #next
# name=["meet","dev","kishan"]
# name.sort()
# print(name)

# # #next
# name=["meet","dev","kishan"]
# name.sort(reverse=True)
# print(name)


# #next

# def fun2(self):
#     return len(self)
# name=["meet","ved","kishan"]

# name.sort(reverse=True,key=fun2)
# print(name)