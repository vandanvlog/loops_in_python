# program defination = count the commission for the sales man


# create the veriable to controll the loop
keep_going = 'y'

# calculate series of commission

while keep_going == 'y':
    # calculate the commission
    sales = float(input('Enter the amount of sales =  ' ))
    commission_rate = float(input('enter the amount of the commission per sales = '))

    # calculation
    commission = sales * commission_rate

    # display commissiion rate
    print(f'this your commission for this month ${commission:,.2f}')

    # if user want to count more commissions then
    keep_going = input('do you want to count another ' + 'commission( Enter y if yes):  ')