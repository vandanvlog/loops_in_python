
print(f' program 1')
print('---------')
print()

for row in range(8):
    for col in range(6):
        print('*', end='')
    print()
print()


print(f'program 2')
print('----------')
print()
for row in range(6):
    for col in range(row + 1):
        print('*', end='')
    print()