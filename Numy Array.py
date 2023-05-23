
import numpy as np

# Import numpy as np and see the version
print(np.__version__)

# How to create a 1D array?

num = int(input(' Enter the number to create array: '))
array = np.arange(num)

print(f"The Array is: {array}.")

print('----------------------------------------------------------------')

Start_num = int(input(' Enter the Start number to create array: '))
End_num = int(input(' Enter the Ends number to create array: '))
array = np.arange(Start_num, End_num+1)

print(f"The Array is: {array}.")

print('----------------------------------------------------------------')

Start_num = int(input(' Enter the Start number to create array: '))
End_num = int(input(' Enter the Ends number to create array: '))
Step_num = int(input(' Enter the Step number to create array: '))
array = np.arange(Start_num, End_num+1, Step_num)

print(f"The Array is: {array}.")