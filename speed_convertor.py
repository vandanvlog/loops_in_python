
# this program converts the speed 60 KPH
# through 130 KPH (in the icrement of 10)
# to MPH

START_SPEED = 60   # starting speed
END_SPEED = 131    # ending speed
INCREMENT = 10    # speed increment
CONVERSION_FACTOR = 0.6214 # Conversion factor

# print the table heading
print('KPH]MPH')
print('------------')

# print the speed
for kph in range(START_SPEED, END_SPEED, INCREMENT):
    mph = kph * CONVERSION_FACTOR
    print(f'{kph}\t{mph: .1f}')