n = int(input('Array size : '))
l = [None] * n

for i in range(len(l)):
    l[i] = int(input(f'{{{i}}} : '))
print(f'List : {l}\n')

currentSize = n
remove = input('Number to remove : ')
while remove.lower() != 'done':
    remove = int(remove)
    found = False
    for i in range(currentSize):
        if l[i] == remove:
            l[i] = None
            found = True
            break
    if found:
        nl = [None] * (currentSize - 1)
        idx = 0
        for i in range(currentSize):
            if l[i] != None:
                nl[idx] = l[i]
                idx += 1
        l = nl
        print(f'Current list : {l}\n')
        currentSize -= 1
    else:
        print('Number not found!\n')
    remove = input('Number to remove : ')

print(f'\nList : {l}')