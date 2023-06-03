Marksheet = {
    'Hindi':int(input('Enter the Hindi mark: ')),
    'Math': int(input('Enter the Math mark: ')),
    'Physics': int(input('Enter the Physics mark: ')),
    'Chemistry': int(input('Enter the Chemistry mark: ')),
    'English': int(input('Enter the English mark: ')),
    'Computer': int(input('Enter the Computer mark: '))
}
Marksheet['Total_Mark'] = sum(Marksheet.values())
Marksheet['Percentage'] = (Marksheet['Total_Mark'] / 600)*100
if Marksheet['Percentage'] >= 60:
    Marksheet['Pass Or Fail'] = '1st Rank (Pass)'
    for k,i in Marksheet.items():
        print(k,':',i)
elif Marksheet['Percentage'] >= 45:
    Marksheet['Pass Or Fail'] = '2nd Rank (Pass)'
    for k,i in Marksheet.items():
        print(k,':',i)
elif Marksheet['Percentage'] >= 33:
    Marksheet['Pass Or Fail'] = '3rd Rank (Pass)'
    for k,i in Marksheet.items():
        print(k,':',i)
elif Marksheet['Percentage'] < 33:
    Marksheet['Pass Or Fail'] = 'Failed'
    for k,i in Marksheet.items():
        print(k,':',i)
else:
    print('Invalid')