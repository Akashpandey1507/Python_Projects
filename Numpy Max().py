import numpy as np

# Creating 5x4 array
arr = np.arange(1, 20+1).reshape(5,4)
print(arr)
print()

# # If no axis mentioned, then it works on the entire array
print(np.argmax(arr))

# If axis=1, then it works on each row
print(np.argmax(arr, axis=1))

# If axis=0, then it works on each column
print(np.argmax(arr, axis=0))

