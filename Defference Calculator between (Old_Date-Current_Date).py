
# Defference Calculator between (Old_Date - Current_Date)

import datetime

'''-----------------------------------------'''
Year = input('Enter the Year: ')
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
Month = input('Enter the Month: ')
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
Day = input('Enter the Day: ')
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
Your_Date = datetime.datetime(Year, Month, Day)
print(f'Your Date is: {Your_Date}')
    
Today_Date = datetime.datetime.now()

Deff = f"The deffenece in both date is: {Today_Date.year-Your_Date.year} Years, {-(Today_Date.month - Your_Date.month)} Months and {-(Today_Date.day - Your_Date.day)} Days."
print(Deff)