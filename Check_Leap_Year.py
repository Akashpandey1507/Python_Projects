
def Leap_Year():
    Year = int(input("Enter the year you want to check? "))

    if Year % 4 == 0:
        if Year % 100 == 0:
            if Year % 400 == 0:
                return (f"The {Year} is a leap year")
            else:
                return (f"The {Year} is not a leap year")
        else:
            return (f"The {Year} is a leap year")
    else:
        return (f"The {Year} is not a leap year")


print(Leap_Year())

