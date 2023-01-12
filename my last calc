"""
Name: total
Discribtion: calculate the total of two number
Author: Aminah
"""
while True:
    try:
        # using exception handling
        number1 = int(input("Input  the number:"))
        number2 = int(input("Input  the number:"))
        b = number1, number2

        z = (input("select the operator (+,-,*,/): "))


        def add(x, y):
            return x + y


        # This function subtracts two numbers
        def subtract(x, y):
            return x - y


        # This function multiplies two numbers
        def multiply(x, y):
            return x * y


        # This function divides two numbers
        def divide(x, y):
            return x / y


        # calculate the total of 2 number
        if z == '+':
            print(number1, '+', number2, '=', add(number1, number2))
        elif z == '-':
            print(number1, '-', number2, '=', subtract(number1, number2))
        elif z == '*':
            print(number1, '*', number2, '=', multiply(number1, number2))
        elif z == '/':
            print(number1, '/', number2, '=', divide(number1, number2))

        else:
            print("error, please check your code")

    except ZeroDivisionError:
        print('Cannot divide by zero')

    except:
        print("error, please check your code")

    # check if user wants another calculation
    # break the while loop if answer is no
    next_calculation = input("Let's do next calculation? (yes/no): ")
    if next_calculation == "no":
        break
