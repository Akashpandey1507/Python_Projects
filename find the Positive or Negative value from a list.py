

numeric_list = [] # Creating empty list

positive = [] # Creating a empty list for getting Positive number
negative = [] # Creating a empty list for getting Negative number

# range for set a range for ask input from user
range_num = int(input('Enter the Range Number: '))

i = 0
while i < range_num:
    # ask number from user
    ask_num = int(input('Enter the Number: '))
    # add the ask number to main list
    numeric_list.append(ask_num)
    # increament of 1 in i
    i +=1

# print the main list incluidng negative and positive values
print(f"List is: {numeric_list}")

# againt playing loop for get positive and negative number sepretely
for i in numeric_list:
    # conditions for negative value
    if i < 0:
        # add in negative empty list of all negative value from the list
        negative.append(i)

    # condition for positive number
    elif i > 0:
        # add in positive empty list of all positive value from the list
        positive.append(i)

# print both list of Positive and Negative after seprated
print(f'The Positive number from list is: {positive}.')
print(f'The Negative number from list is: {negative}.')


