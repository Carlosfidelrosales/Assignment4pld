def acquireNameAgeAddress():
   _name = input("\033[1m\033[30m\033[93mPlease enter your full name:\n-> ")
   _age = int(input("\033[1m\033[30m\033[93mPlease enter your age:\n-> "))
   _address = input("\033[1m\033[30m\033[93mPlease enter your full address:\n-> ")
   return _name, _age, _address

def display(nameF, ageF, addressF):
    print(f"\033[1m\033[30m\033[93mHi, my name is {nameF}. I am {ageF} years old and I live in {addressF}.")
    

name, age, address = acquireNameAgeAddress()
display(name, age, address)