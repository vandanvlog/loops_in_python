# this is to calculate total property tax

TAX_FACTOR = 0.0065

# now print the number of the property

print('enter the property lot number')
lot = int(input('Enter your property lot = '))

while lot != 0 :
    print('Enter the property value number ')
    value = float(input('Enter your property value = '))

    tax = value * TAX_FACTOR

    print(f'your property tax = ${tax: .2f}')

    # enter your new value
    print('enter the property lot number')
    lot = int(input('Enter your property lot = '))
