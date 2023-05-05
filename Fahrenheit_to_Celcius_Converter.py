
def convert():
    s = input('Enter the tempreture: ')
    f = float(s)
    c = round((f - 32) * 5/9,1)
    return (f'Calcius: {c}')

print(convert())
