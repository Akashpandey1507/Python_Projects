
import datetime as dt

# "--------------------------------------------------------"
Birth_of_Year = input("Enter the Birth of Years: ")
if len(Birth_of_Year) == 4:
    if Birth_of_Year.isnumeric():
        if int(Birth_of_Year) < dt.datetime.now().year:
            Birth_of_Year = int(Birth_of_Year)
        else:
            print('Enter the correct years')
    else:
        print('The Birth Years should be in Numeric Value. ')
else:
    print("Enter the Correct Years in YYYY Format. ")
# "--------------------------------------------------------"
Birth_of_Month = input("Enter the Birth of Month: ")
if len(Birth_of_Month) <= 2:
    if Birth_of_Month.isnumeric():
        Birth_of_Month = int(Birth_of_Month)
    else:
        print('The Birth Month should be in Numeric Value. ')
else:
    print("Enter the Correct Month in MM Format. ")
# "--------------------------------------------------------"
Birth_of_Day = input("Enter the Birth of Day: ")
if int(Birth_of_Day) <= 31:
    if Birth_of_Day.isnumeric():
        Birth_of_Day = int(Birth_of_Day)
    else:
        print('The Birth Days should be in Numeric Value. ')
else:
    print("Enter the Correct days is not greater than 31. ")
# "--------------------------------------------------------"
# imput from user of their dob or other date
dob = dt.datetime(Birth_of_Year,Birth_of_Month,Birth_of_Day,0,0,0)
# year
dob_year = dob.year
#Month
dob_month = dob.month
#Day
dob_day = dob.day

# Current Date
current_date = dt.datetime.now()
# Current Year
current_date_Year = current_date.year
#Current month
current_date_month = current_date.month
# Current Day
current_date_Day = current_date.day

Calculation = f'{current_date_Year-dob_year} Years, {current_date_month-dob_month} Months and {current_date_Day-dob_day} Days.'

print(Calculation)