
number = int(input('Enter the number: ')) # take input in numeric

for row in range(1, number+1): # for rows
    for col in range(1,number+1): # for columns
        print('*',end='  ') #for print in same line
    print() # for change line

# Output Like this; 
'''
*  *  *  *  *  *  *  *  *  *  
*  *  *  *  *  *  *  *  *  *
*  *  *  *  *  *  *  *  *  *
*  *  *  *  *  *  *  *  *  *
*  *  *  *  *  *  *  *  *  *
*  *  *  *  *  *  *  *  *  *
*  *  *  *  *  *  *  *  *  *
*  *  *  *  *  *  *  *  *  *
*  *  *  *  *  *  *  *  *  *
*  *  *  *  *  *  *  *  *  *
'''

