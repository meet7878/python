a=5
b=0


try:
    #c=int("meet")
    c=a/b
except ZeroDivisionError:
    print("zerodivisioon error")
except ValueError:
    print("Invalid literal for int with base 10")

print("done")