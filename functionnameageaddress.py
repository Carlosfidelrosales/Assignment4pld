def acquireNameAgeAddress():
   _name = input("Please enter your full name:\n-> ")
   _age = int(input("Please enter your age:\n-> "))
   _address = input("Please enter your full address:\n-> ")
   return _name, _age, _address

def display(nameF, ageF, addressF):
    print(f"Hi, my name is {nameF}. I am {ageF} years old and I live in {addressF}.")
    

name, age, address = acquireNameAgeAddress()
display(name, age, address)