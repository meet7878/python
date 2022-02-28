


# MINUS =lambda x,y: x-y

# print(MINUS(9,4))

# #next:-

# # def MINUS(x,y):
# #     return x-y

# # print(MINUS(9,4))

# #next:2

# a=[(1,14),(8,6),(5,23)]
# a.sort(key=lambda x:x[0])
# print(a)


#next:3



 
 

# mapped = map (lambda x: x % 2 == 0, a)
# print(list(mapped))


a=[1,2,4,6,8]

filt=filter(lambda x: x % 2==0,a)
print(list(filt))


mapping= map(lambda x:x%2==0,a)
print(list(mapping))

