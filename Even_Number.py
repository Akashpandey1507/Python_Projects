num = []
even_num = []

for i in range(10):
    ask_num = int(input('Enter the number: '))
    num.append(ask_num)

print(num)

for i in num:
    if i % 2 == 0:
        even_num.append(i)

print(f'The Even number is: {even_num}')