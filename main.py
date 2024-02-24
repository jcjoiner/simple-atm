# Problem Set 6
# Simple ATM

'''
    Implement a program that simulates a simple ATM machine with withdrawal, deposit, and balance inquiry functionalities.
'''

import random
import os

# Account will start randomly between 0 and 1000
# Create a menu with options to: withdrawl, deposit, check balance, or exit
# Queue the user choose a menu option

os.system("clear")
balance = random.uniform(0, 1000)

while True:
    print("MENU")
    print("1: Check balance")
    print("2: Deposit")
    print("3: Withdrawl")
    print("0: Exit")
    print("----------------------------------------")

    option = float(input("Enter a menu option: "))

    if option == 0:
        break
    if option == 1:
        os.system("clear")
        print(f"Your balance is ${balance:.2f}.\n")
    if option == 2:
        deposit = float(input("How much would you like to deposit: $"))
        balance = balance + deposit
        os.system("clear")
        print(f"Your new balance is ${balance:.2f}.\n")
    if option == 3:
        withdrawl = float(input("How much would you like to withdrawl: $"))
        balance = balance - withdrawl
        if balance < 0:
            os.system("clear")
            print(f"YOUR BALANCE IS ${balance:.2f}!\n")
        else:
            os.system("clear")
            print(f"Your new balance is ${balance:.2f}.\n")
