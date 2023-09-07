#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      acer
#
# Created:     07/09/2023
# Copyright:   (c) acer 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#calculator

num1 = input("Enter 1st number: ")
num2 = input("Enter 2nd number: ")

operator = input("Enter operation: +,-,*,/")

# when we enter the number, it is in string formate
# to convert string to integer we can use type conversion
num1 = int(num1)
num2 = int(num2)

if operator == '+':
    print(num1 + num2)
elif operator == '-':
    print(num1 - num2)
elif operator == '*':
    print(num1 * num2)
elif operator == '/':
    print(num1 / num2)
else:
    print("invalid choice")