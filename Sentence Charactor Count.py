
def count_characters():
    Senntences = input('Enter you Sentnces: ')
    Senntences = Senntences.replace(' ','')
    count = {}
    for i in Senntences:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    
    for Char,Counts in count.items():
        print(f'{Char} : {Counts}')



print(count_characters())


