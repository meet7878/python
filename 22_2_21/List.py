l=list(range(1,3+1))

l.append(100)
l.append([3,4,5])
l.remove(2)
l.insert(0,10)
l.insert(0,[-1,2,3])
print(l)

var = ['pop', 'rock', 'jazz']


for i in var:
    print("I like", i)

[print(i)  for i in var ]  #for loop in one line  
