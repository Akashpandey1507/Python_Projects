basic_salary = int(input('Enter the Basic Salary:: '))

dearness_allowance = basic_salary * 40 / 100
house_rent_allowance = basic_salary * 20 / 100

gross_salary = round((basic_salary + dearness_allowance + house_rent_allowance),0)

print("Basic Salary: ",basic_salary)
print("Dearness Allowance (40%) : ",dearness_allowance)
print("House Rent Allowance (20%): ",house_rent_allowance)
print("Gross Salary: ",gross_salary)