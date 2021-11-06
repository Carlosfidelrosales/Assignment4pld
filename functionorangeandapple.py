def greetings():
    print("WELCOME TO CARLITO STORE! APPLE IS 20PHP EACH WHILE ORANGE IS 25PHP EACH.")


def OrangesandApples(_apple, _orange):
    apple_total = 20 * _apple
    orange_total = 25 * _orange
    sum = apple_total + orange_total
    return sum


def display():
    _apple = int(input('Enter how many apples do you want to buy:\n-> '))
    _orange = int(input('Enter how many oranges do you want to buy:\n-> '))
    grandtotal = OrangesandApples(_apple, _orange)
    print(f"The total amount is {grandtotal} Pesos.")
 
greetings()
display()