# keep eye on temperature on machine

MAX_TEMP = 102.5

# get the inout from the machine anout the temeprature

temperature = float(input('What is the temperature right now : '))

#  now give alert massage

while temperature > MAX_TEMP :

    print("Danger ..... Danger ....")
    print('your temperature is too high ')
    print(' turn down machine now immediately')
    print('Wait for  5 minutes and check it agin ')

    temperature = float(input('what is the temperature now = '))

# if the temperature os norm`al then
print('now this temperature is normal now, check after 15 minutes ')