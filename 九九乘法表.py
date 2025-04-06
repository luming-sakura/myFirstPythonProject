i = 1
'''for i in range(1,10):
    for j in range(1,i+1):
        print(f'{i}*{j}= {i*j}\t',end='')
    print()'''

while i < 10:
    lab = 1
    while lab <= i:
        print(f'{i}*{lab} = {i*lab} \t',end='')
        lab += 1
    i += 1
    print()