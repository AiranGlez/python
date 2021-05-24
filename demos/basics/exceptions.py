print('Programm to divide two integers')


def divideints(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        print('Cannot divide by zero')


while True:
    try:
        num1 = int(input('1º: '))
        num2 = int(input('2º: '))
        break
    except ValueError:
        print("Introduced values are invalid")

print(divideints(num1, num2))



