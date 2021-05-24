import math


def squareroot(num1):

    if num1 < 0:

        raise ValueError ("Number cannot be negative")

    else:

        return math.sqrt(num1)


op1 = (int(input("Introduce a number: ")))

try:

    print(squareroot(op1))

except ValueError as NegativeNumberError:

    print(NegativeNumberError)

print("Program finished")

def myAge(age):

    if age < 0:

        raise TypeError("Hey, it is impossible to have negative age!")

    if age < 20:

        return "You are really young!"

    elif age < 40:

        return "You are young!"

    elif age < 65:

        return "You are mature!"

    elif age < 100:

        return "Now you are mature!"

print (myAge(32))