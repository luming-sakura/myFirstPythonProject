i = 1
All = 10000
for i in range(1,21):
    import random
    num = random.randint(1,10)
    if All > 0:
        if num >= 5:
            All -= 1000
            print(f'员工{i},绩效分{num},高于5，...，还剩{All}')
        else :
            print(f'员工{i}，绩效分{num}，低于5，...,还剩{All}')
    else:
        print('没钱了，下次一定')
        break
    i += 1


