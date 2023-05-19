
Amount = float(input('Enter your Investment Amount: '))
Interest_rate = float(input('Enter your Rate of Interest Rate: '))
Time = float(input('Enter your Time in Years: '))

Present_Value = Amount
Rate = Interest_rate / 100
Time = Time

print(f'''Question: If a Person invests Rs. {Present_Value} in an investment which pays {Interest_rate}% of interest, Wthat will be the Future Value of the invested value amount at the end of {Time} years.''')


Future_Value = round(Present_Value * (1 + Rate) ** Time ,1)

print(f'The Future Value will be: Rs. {Future_Value}')

