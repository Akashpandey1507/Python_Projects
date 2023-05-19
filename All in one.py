
print('Welcome to home')

choose = input('''Please press -
1 For Fahrenheit to Celcius Converter
2 For Multiple Inputs with Python using While Loop
3 For Show Tables
4 For Check Leap Year
5 For BMI Calculator
6 For Even Number
7 For Sentence Charactor Count
8 For Calculate the Time Value of money for one time investment


Choose::: ''')

if choose == '1':
    In_Fahrenheit = float(input('Enter the tempreture: '))
    To_Calcius = round((In_Fahrenheit - 32) * 5/9,1)
    print(f'Calcius: {To_Calcius}')

elif choose == '2':
    while True:
        reply = input('Please Enter your reply: ')
        if reply.title() == 'Stop': break
        
        print(reply)

elif choose == '3':

    Table_Number = input('Enter the Input for Table: ')
    if Table_Number.isnumeric():
        if len(Table_Number) <= 6:
            Table_Number = int(Table_Number)
        else:
            print("The digit of Table_Number should not be greater 6 Digit")
    else:
        print("The Table Number should be a Numeric value only.")


    for i in range(1,11):
        print(f"{Table_Number} X {i} = {i*Table_Number}")

elif choose == '4':
    Year = int(input("Enter the year you want to check? "))

    if Year % 4 == 0:
        if Year % 100 == 0:
            if Year % 400 == 0:
                print(f"The {Year} is a leap year")
            else:
                print(f"The {Year} is not a leap year")
        else:
            print(f"The {Year} is a leap year")
    else:
        print(f"The {Year} is not a leap year")

elif choose == '5':
    
    # Get the user's weight in kilograms
    weight = float(input("Enter your weight in kg: "))

    # Get the user's height in meters
    height = float(input("Enter your height in cm: "))
    height = height/100 # Change into meter

    # Calculate the BMI using the formula
    bmi = round(weight / (height ** 2),1)    # Print the BMI and the corresponding category
    print("Your BMI is", bmi)
    if bmi < 18.5:
        print("You are underweight.")
    elif bmi < 25:
        print("You have a normal weight.")
    elif bmi < 30:
        print("You are overweight.")
    else:
        print("You are obese.")

elif choose == '6':

    num = []
    even_num = []

    for i in range(10):
        ask_num = int(input('Enter the number: '))
        num.append(ask_num)

    print(num)

    for i in num:
        if i % 2 == 0:
            even_num.append(i)

    print(f'The Even number is: {even_num}')

elif choose == '7':

    Senntences = input('Enter you Sentnces: ')
    Senntences = Senntences.replace(' ','')
    count = {}
    for i in Senntences:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    
    for Char,Counts in count.items():
        print(f'{Char} : {Counts}')

elif choose =='8':
    
    # Calculate the Time Value of money for one time investment

    Amount = float(input('Enter your Investment Amount: '))
    Interest_rate = float(input('Enter your Rate of Interest Rate: '))
    Time = float(input('Enter your Time in Years: '))

    Present_Value = Amount
    Rate = Interest_rate / 100
    Time = Time

    print(f'''Question: If a Person invests Rs. {Present_Value} in an investment which pays {Interest_rate}% of interest, Wthat will be the Future Value of the invested value amount at the end of {Time} years.''')


    Future_Value = round(Present_Value * (1 + Rate) ** Time ,1)

    print(f'The Future Value will be: Rs. {Future_Value}')


        
