print('My application')

user_exam = float(input('Write user exam grade: '))

def evaluation(exam):
    valoration = 'Accepted'
    if exam < 5:
        valoration = 'Rejected'
    return valoration


print(evaluation(user_exam))



