def greetings():
    print("\033[1m\033[30m\033[93mWELCOME TO CARLITO STORE! The fruit available for today is an apple.")


def change_apple(pocketMoney, price_apple):
    if pocketMoney >=  price_apple:
        change = pocketMoney % price_apple
        apple_max = pocketMoney // price_apple
        print(f"You can buy {apple_max:,.0f} apple(s) and your change is {change:,.2f} pesos.")
    else:
        price_apple > pocketMoney
        insufficient_money = price_apple - pocketMoney
        print(f"I am sorry but you don't have enough money. You must need atleast additional {insufficient_money:,.2f} pesos in order to buy an apple.")

greetings()
change_apple(pocketMoney = float(input("How much money do you have in your pocket right now?: ")), price_apple = float(input("How much is the price for each apple?: ")))




