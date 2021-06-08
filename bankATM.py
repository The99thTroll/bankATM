import random
import math
import time

class ATM (object):
    #Constructor for our class
    def __init__(self, userName = '', cardNum = '', pinNum = '', balance = 0):
        self.userName = userName
        self.cardNum = cardNum
        self.pinNum = pinNum
        self.balance = balance
        
    #Basic hello message    
    def signIn(self):
        printWithBuffer("Welcome " + self.userName + " to WhiteHat ATMs!")
        time.sleep(1.5)
        
    #Just show the user their balance
    def showBalance(self):
        printWithBuffer("Current Balance: $" + str(self.balance))
        time.sleep(1.5)
        
    #Allows the user to add money
    def depositMoney(self):
        print("")
        amount = takeInput(prompt = 'How much do you wish to desposit? $')
        self.balance += int(amount)
        printWithBuffer("Transaction Complete! New Balance: $" + str(self.balance))
        time.sleep(1.5)
        
    #Allows the user to remove money
    def withdrawMoney(self):
        print("")
        amount = takeInput(prompt = 'How much do you wish to withdraw? $')
        
        if int(amount) > self.balance:
            printWithBuffer("[ERROR] Amount exceeds current balance")
            time.sleep(1.25)
            return
        
        self.balance -= int(amount)
        printWithBuffer("Transaction Complete! New Balance: $" + str(self.balance))
        time.sleep(1.5)
    
    #Basic bye message    
    def signOut(self):
        print("Thank you " + self.userName + " for using WhiteHat ATMs!")
        time.sleep(1.5)
        
def takeInput(prompt = '', minCharecters = 0, maxCharecters = 100):
    #This function is meant to help streamline question input
    while True:
        data = input(prompt)
        
        if len(data) < minCharecters:
            print("\nResponse too short!\nA minimum length of " + str(minCharecters) + " charecters is required.\n")
        elif len(data) > maxCharecters:
            print("\nResponse too long!\nA max length of " + str(maxCharecters) + " charecters is allowed.\n")
        elif data == "cancel":
            print("Operation cancelled.")
            return None
        else:
            return data

#Simple Function to reduce total lines of code
def printWithBuffer(text):
    print("")
    print(text)
    print("")
    
#Take in the user's basic data
name = takeInput(prompt = "What's your name? ", minCharecters = 2, maxCharecters = 64)
cardNum = takeInput(prompt = "What's your card number? ", minCharecters = 15, maxCharecters = 19)
pinNum = takeInput(prompt = "What's your pin number? ", minCharecters = 4, maxCharecters = 4)

#Use the data we took to create an ATM instance
atmInstance = ATM(
    userName = name, 
    cardNum = cardNum,
    pinNum = pinNum,
    balance = math.floor(random.random() * 2500)
    )

atmInstance.signIn()

while True:
    #Display options to users
    whatToDo = input("""
    [WhiteHat ATMs]
1) Check Balance
2) Deposit Money
3) Withdraw Money
4) Log Out
                     
Please Select A Number: """)
    
    #Execute the user's decisions
    if whatToDo == "1":
        atmInstance.showBalance()
    elif whatToDo == "2":
        atmInstance.depositMoney()
    elif whatToDo == "3":
        atmInstance.withdrawMoney()
    elif whatToDo == "4":
        atmInstance.signOut()
        break
    else:
        printWithBuffer("[ERROR] Invalid Number")
        time.sleep(0.75)