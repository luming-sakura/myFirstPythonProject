import random

num_1 = random.randint(1,100)
time = 0
flag = True
while flag ==1:
    a1 = int(input('input a random number'))
    time += 1
    if a1 == num_1:
        print('the number is right')
        flag = False
    else:
        if a1 > num_1:
            print('higher')
        else:
            print('lower')
print(f'you have tried {time} times')




