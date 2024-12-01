# write a progrram calculate their squares

print("Numbers  Squares ")
print('-----------------------')

print(' enter the number, you get squres value ')
numbers = int(input('Enter the number here ==> '))

for yournumber in range(numbers + 1):
    squres = yournumber ** 2
    print(f'{yournumber}\t{squres}')