
print('----------------Welcome to Lambda------------------')

choose = input('''Please press -
1 For Finding Sqaure
2 For Finding Cube
3 For Finding The Table

Choose::: ''')

if choose == '1':
    number = int(input(('Enter the number for Sqaure: ')))
    Sqaure = lambda x : x**2
    print(f"The Square is: {Sqaure(number)}")

elif choose == '2':
    number = int(input(('Enter the number for Cube: ')))
    Cube = lambda x : x**3
    print(f"The Cube is: {Cube(number)}")

elif choose == '3':
    number = int(input(('Enter the number for Table: ')))
    Table = lambda x : [x * i for i in range(1,11)]
    print(f"The Table is: {Table(number)}")


print('----Continue-----')
