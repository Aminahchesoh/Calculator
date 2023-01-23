"""
Name: total
Distribution: calculate the total of two number
Author: Aminah
"""


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


while True:
    try:
        # using exception handling
        number1 = int(input("Input  the first number:"))
        number2 = int(input("Input  the second number:"))
        z = (input("select the operator (+,-,*,/): "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    try:
        # calculate the total of 2 number
        if z == '+':
            print(number1, '+', number2, '=', add(number1, number2))
        elif z == '-':
            print(number1, '-', number2, '=', subtract(number1, number2))
        elif z == '*':
            print(number1, '*', number2, '=', multiply(number1, number2))
        elif z == '/':
            print(number1, '/', number2, '=', divide(number1, number2))
    except ZeroDivisionError:
        print('Cannot divide by zero')

    # check if user wants another calculation
    # break the while loop if answer is no
    next_calculation = input("Let's do next calculation? (yes/no): ")
    if next_calculation == "no":
        break

    else:
        print("please choose the correct operator")
