
# Write a function that takes a list of integers and returns a new list with only the unique values

list = [] # Create the empty list 

# run te loop
for i in range(10):
    ask_num = int(input('Enter the Number: ')) # Ask the number from user
    if ask_num not in list:  # Check if the number is already in the list, if it's not then add to the
        list.append(ask_num)    # list otherwise do nothing

print("The Unique Numbers are : ", list)