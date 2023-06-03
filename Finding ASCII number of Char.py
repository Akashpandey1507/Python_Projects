

print('----------Print ASCII Number------------')

text = input('Enter the text: ') # take text input from user

for i in text: 
    ascii_code = ord(i)
    print(f"{i} : {ascii_code}")

