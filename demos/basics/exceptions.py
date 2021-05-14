print('Programm to divide two integers')


def divideints(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        print('Cannot divide by zero')


num1 = int(input('1º: '))
num2 = int(input('2º: '))

print(divideints(num1, num2))



