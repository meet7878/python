r=6
for row in range(1,r+1):
    for col in range(0,2*r):
        if (row==1 and col%2!=0) or row==col or row+col==10:
            print("*",end='')
        else:
            print(" ",end=' ')
    print()                            