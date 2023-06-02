# Create the Disctionary from List from talking input from Users

keys = []  # creating a empty list for keys
value = [] # creating a empty list for values

inp = int(input('Enter the Range Values: '))

for i in range(inp):  # looping for 5 times
    # take input from user as Keys
    ask_key = input('Enter you Keys: ').title()
    # take v=input from user as value of Keys
    ask_value = input('Enter you Values: ').title()
    # append ask key with keys empty list 
    keys.append(ask_key)
    # append ask value input with values empty list
    value.append(ask_value)

# print both list
print(keys)
print(value)

# Create a empty dist()
dictionary = {}

# user loop for add items in dist()
for d in range(len(keys)):
    # set keys
    key = keys[d]
    # set values
    values = value[d]
    # addition list() to dist()
    dictionary[key] = values

# use loop for print readable
for k, val in dictionary.items():
    print(f"{k} : {val}")