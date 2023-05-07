import datetime

'''-----------------------------------------'''
Year = input('Enter the Birth Year: ')
if len(Year) == 4 :
    if Year.isnumeric():
        if Year < '2024':
            Year = int(Year)
        else:
            print('Year should Not be greater than 2023')
    else:
        print('Year should be only numeric value')
else:
    print('Your Year Length should be less than 5')
'''-----------------------------------------'''
Month = input('Enter the Birth Month: ')
if len(Month) < 3:
    if Month.isnumeric():
        if Month < '13':
            Month = int(Month)
        else:
            print('Month should Not be greater than 12')
    else:
        print('Months should be only numeric value')
else:
    print('Your Months Length should be less than 3')
'''-----------------------------------------'''
Day = input('Enter the Birth Day: ')
if len(Day) < 3:
    if Day.isnumeric():
        if Day < '32':
            Day = int(Day)
        else:
            print('Days should Not be greater than 31')
    else:
        print('Day should be only numeric value')
else:
    print('Your Days Length should be less than 3')
'''-----------------------------------------''' 
Birth_Date = datetime.datetime(Year, Month, Day)
print(f'Your Date of Birth is: {Birth_Date}')
    
Today_Date = datetime.datetime.now()

Age = f"Hi, You are {Today_Date.year-Birth_Date.year} Years Old, {-(Today_Date.month - Birth_Date.month)} Months and {-(Today_Date.day - Birth_Date.day)} Days."
print(Age)