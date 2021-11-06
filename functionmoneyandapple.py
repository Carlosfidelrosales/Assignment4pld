def greetings():
    print("WELCOME TO CARLITO STORE! The fruit available for today is an apple.")

def appleTotal(pocketMoney, price_apple):
    totalApples = pocketMoney // price_apple
    return totalApples

def changeTotal(pocketMoney, price_apple):
    Applesmax = price_apple % pocketMoney
    return Applesmax

