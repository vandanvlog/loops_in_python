

for r in range(6):
    for c in range(r+1):
        print(f'#',f'{c}',end="")
    print('#')



rows = 5

for i in range(rows):
    print("#", " " * i, "#", sep="")