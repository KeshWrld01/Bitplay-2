# Program to check if user input numbers are equal without using any comparison operator.

def checkIfSame(number1, number2):

    # Use XOR operator as a^a is always 0
    if ((number1 ^ number2) != 0):
        print("Numbers are not equal")
    else:
        print("Both numbers are equal")

# Taking input
number1 = int(input("Enter first number to compare: "))
number2 = int(input("Enter second number to compare: "))

checkIfSame(number1, number2)
