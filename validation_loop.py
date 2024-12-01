# this program calculate retail pricese
MARK_UP = 2.5 # the mark up price
another = "y" #  variable to control the loop

# process one or more item
while another == 'y' or  another == "Y":
    wholesale = float(input("Enter the item's wholesale cost = "))

    while wholesale < 0:
        print(' Enter valid cost your cost is nagative')
        wholesale = float(input('Enter the valid cost ='))

    retail = wholesale * MARK_UP

    print(f' your retail price is = ${retail:,.2f}')

    #  add another price
    another = input('Do you have another itema  ?' + 'Enter y for yes= ')





