# Central tendency

"""
Central tendency is a measure that represents the typical or central value of a dataset. 
It provides a summary of the distribution and helps understand the "center" of the data. 
The three commonly used measures of central tendency are the mean, mode, and median
"""

import statistics as st # import liabrary

data = [] # Datasets
data = sorted(data) # Sort the dataset

n = int(input('Enter the Datasets len: '))
for i in range(n):
    ask_number = int(input('Enter the number: '))
    data.append(ask_number)

Avrg = st.mean(data) #Calculation of Avrg 
Median = st.median(data) #Calculation of Median 
Mode = st.mode(data) #Calculation of Mode 

print(f"The Average is: {Avrg}")
print(f"The Median is: {Median}")
print(f"The Mode is: {Mode}")


