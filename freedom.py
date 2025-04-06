All1 = 20000
consumption = int(input('right down your today\'s consumption'))
while consumption <= All1:
    All1 -= consumption
    print(f'you can have {All1} more consumption')
    consumption += 1000
print('you have no money')
