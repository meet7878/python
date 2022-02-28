

def checkbalance():
    money = 10000
    withdraw = 5000
    try:   
        balance = money - withdraw
        if(balance<=2000):
            print('Insufficent')
           
    finally:
        print(balance)
checkbalance()
    
    
