# Create the Disctionary from List from talking input from Users thru While Loop

keys = []  # creating a empty list for keys
value = [] # creating a empty list for values

inp = int(input('Enter the Range Values: '))
i = 0

while i < inp:  # while looping for 5 times
    # take input from user as Keys
    ask_key = input('Enter you Keys: ').title()
    # take v=input from user as value of Keys
    ask_value = input('Enter you Values: ').title()
    # append ask key with keys empty list 
    keys.append(ask_key)
    # append ask value input with values empty list
    value.append(ask_value)
    i +=1

# print both list
print(keys)
print(value)

# Create a empty dist()
dictionary = {}

d = 0 
ranges = len(keys) # Create the length of keys

while d < ranges: # create while loop

    # set keys
    key = keys[d]
    # set values
    values = value[d]
    # addition list() to dist()
    dictionary[key] = values
    d += 1 


# use loop for print readable
for k, val in dictionary.items():
    print(f"{k} : {val}")