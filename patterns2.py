 # now we are taking input for the pattern

total_rows = int(input('you many row you want to print = '))

for r in range(total_rows):
    for c in range(r + 1):
        print("*", end=" ")
    print()