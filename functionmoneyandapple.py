def greetings():
    print("WELCOME TO CARLITO STORE! The fruit available for today is an apple.")

def appleTotal(pocketMoney, price_apple):
    totalApples = pocketMoney // price_apple
    return totalApples

def changeTotal(pocketMoney, price_apple):
    Applesmax = price_apple % pocketMoney
    return Applesmax

def display():
    pocketMoney = float(input("How much money do you have in your pocket right now?:\n-> "))
    price_apple = float(input("How much is the price for each apple?:\n-> "))
    appleF = appleTotal(pocketMoney, price_apple)
    changeF = changeTotal(price_apple, pocketMoney)
    print(f'You can buy {appleF} apple(s) and your change is {changeF} pesos.')

greetings()
display()