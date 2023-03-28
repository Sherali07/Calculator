from sympy import *

x = Symbol('x')
f = x**3 + 2*x**2 + 3*x + 4
y = integrate(f, x)


def add(x, y):
    return x+y


def subtract(x, y):
    return x-y


def multiply(x, y):
    return x*y


def divide(x, y):
    return x/y


def factorial(num):
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    return fact


print("select operation.")
print("1.Add")
print("2.Subtract")
print("3.multiply")
print("4.divide")
print("5.factorial")
print("6.derivative")
print("7.integration")

while True:
    choice = input("Enter choice(1/2/3/4/5/6/7): ")

    if choice in ('1', '2', '3', '4', '5', '6', '7'):
        try:

            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number"))
        except ValueError:
            print("invalid input. Please enter a number.")
            continue

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))

        elif choice == '5':
            num = int(input("Enter a number: "))
            print("Factorial of", num, "is", factorial(num))

        elif choice == '6':

            dfdx = diff(f, x)
            print("The derivative of f(x) = {} is f'(x) = {}".format(f, dfdx))

        elif choice == '7':

             print("The integral of f(x) = {} is F(x) = {}".format(f, y))

        next_calculation = input("Next calculation? (yes/no): ")
        if next_calculation == "no":
            break
        else:
            print("Invalid Input")
