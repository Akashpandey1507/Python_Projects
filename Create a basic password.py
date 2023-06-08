
print('''Please create a password where last 4 digit should be number and before use one symble within [@,#,$]''')
Password = input('Enter the Password: ')

if Password[-4:].isnumeric():
    if Password[0:-5].isalpha():
        if Password[0:-5].capitalize():
            if Password[-5] == '@' or Password[-5] == '#' or Password[-5] == '$':
                print(Password)
            else:
                print('for the symbole should be includ only [@, #, $]')
        else:
            print('Name alfa should be capital formate')
    else:
        print("Fist few digit would be Alfabets")
else:
    print("Last 4 digit would be numeric values")


