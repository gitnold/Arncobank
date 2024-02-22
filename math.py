# import math
# y = (3, 36, 89, 2, 23, 12, 17)
# x = max(y)
# print("This is the maximum value ",x)

# z = min(y)
# print("This is the minimum value", z)

# #lets get square of two numbers
# a = 12
# b = 10
# pwr = a**b
# print("a raised to b is:", pwr)

# c = math.ceil(23.67808)
# print("The ceil method", c)

# k = math.floor(67.855855)
# print("Round down: ",k)

# #Lets get the volume of a cylinder
# #radius is 20, and length 10 >>>metres
# radius = 20
# length = 10
# volume = math.pi * 20 ** 2 * 10
# print("Volume is", volume, "cubic metres")

# #calculate radius of a cylinder whose volume is 1400m3 and 11.3m high
# Volume = 1400
# height = 11.3
# radius = 1400/math.pi * 11.3 ** -2
# print("The radius is:", radius,"m." )

# #Write a program that takes input and multiplies 2 intgers without using the *operator

# num1 = int(input("Enter first number:"))
# num2 = int(input("Enter second number:"))
# num3 = (num1, num2)
# product = math.prod(num3)
# # print("Product =", product)
# class Print():
#     def printer():
#         print("Welcome to Idyangu!Select as service to continue!")
#         print("1.New id, \n2.Change details, \n3.Lost Id")
#         Id.idyangugreet()

# class Id():
#     def __init__(self):
#         print("welcome")
#     def idyangugreet():
#         print("\n\nWelcome to Idyangu!Select as service to continue!")
#         print("1.New id, \n2.Change details, \n3.Lost Id")
#         idoption = int(input("Enter option number : "))
#         if idoption == 1:
#             newid()
#         elif idoption == 2:
#             changedetails()
#         elif idoption == 3:
#             lostid()
#         else:
#             print("Invalid option!!")
#             printer()
#     def newid():
#         print("Welcome to new id")
        


# Print.printer()



def prompt():
    global balance
    balance = 20000
    print("Welcome to ArncoBank ATM!\n Please select a service: \n1.Deposit funds, \n2.Withdraw, \n3.Checkbalance")   
    serviceno = int(input("Enter service number : "))
    if serviceno == 1:
        depositprompt()
    elif serviceno == 2:
        withdrawprompt()
    elif serviceno == 3:
        check_balance()
    else:
        print("Invalid option!")            
def depositprompt():
        accountno = int(input("\nEnter account no : "))
        pin = str(input("Enter pin : "))
        lpin = len(pin)
        if lpin == 6:
            depositmethod()
        else:
            print("Invalid pin!!")
            prompt() 
def depositmethod():
        print("\nPlease select deposit method : \n1.Cheque, \n2.Cash")
        method = int(input("Enter method number : ")) 
        if method == 1:
            depositchq()
        elif method == 2:
            depositcash()
        else:
            print("Invalid option!!") 
def depositchq():
    chequeno = str(input("\nEnter cheque number(six digits) :")) 
    check = len(chequeno)
    if check == 6:
        print("Cheque deposited successfully! Await communication from Arncobank upon processing!")
    else:
        print("Invalid Cheque number! Cheque not registered!!")                                  
def depositcash():              
        deposit = float(input("\nEnter amount to deposit : "))
        if deposit >= 2000000:
            print("Maximum cash deposit reached!See cashier")
        elif deposit <= 10:
            print("Error!! Deposit amount below minimum deposit allowed!")
        else:
            balance3 = balance + deposit
            print("Deposit successful! Balance is",balance3) 
def withdrawprompt():
        accountno = int(input("\nEnter account no : "))
        pin = str(input("Enter pin : "))
        lpin = len(pin)
        if lpin == 6:
            withdraw()
        else:
            print("Invalid pin!!")
            prompt()                 
def withdraw():
        withdraw = float(input("\nEnter amunt to withdraw : "))
        balance2 = balance - withdraw
        if balance - withdraw <= 500:
            print("Withdrawal failed! Minimum account balance reached")
        else:
            print("Withdrawal successful!\n Balance is", balance2)
def check_balance():
        accountno = int(input("\nEnter account no : "))
        pin = str(input("Enter pin : "))
        lpin = len(pin)
        if lpin == 6:
            print(balance)  
        else:
            print("Invalid pin!!")
            prompt()                 
          


prompt()            