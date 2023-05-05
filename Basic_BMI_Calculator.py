def BMI_Calculator():
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


print(BMI_Calculator())


