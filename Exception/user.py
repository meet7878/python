class BalanceException(Exception):
    pass 

def checkbalance():
    money = 10000
    withdraw = 10000
    try:   
        balance = money - withdraw
        if(balance<=2000):
            print('Insufficent')
            #   raise BalanceException('Insufficeeimt')
        
     
    # except BalanceException as be:
    #     print(be)
    finally:
        print(balance)
checkbalance()
    
    
