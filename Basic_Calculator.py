def Calculator():
    Number_1 = float(input('Enter the Value 1: '))
    Operator = input('''Press 1 for Add (+),
    Press 2 for Multiply (x),
    Press 3 for Substract (-),
    Press 4 for Divide (/)
    Choose:: ''')
    Number_2 = float(input('Enter the Value 2: '))

    if Operator == '1':
        Add = Number_1 + Number_2
        return (f'The Addition is: {Add}')
    elif Operator == '2':
        Mult = Number_1 * Number_2
        return (f'The Multiplication is: {Mult}')
    elif Operator == '3':
        Sub = Number_1 - Number_2
        return (f'The Substraction is: {Sub}')
    elif Operator == '4':
        Div = Number_1 / Number_2
        return (f'The Division is: {Div}')
    else:
        returm ('Please input the Valid Opration Option')


print(Calculator())