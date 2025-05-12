import math
e = math.e
a = float(1 / e * (e - 1))
# 输入N的值
n = input()
for i in range(int(n)):
    a = 1 - (i + 1) * a
    print(a)
'''
由于双精度的位数导致在进行相减计算时精度缺失，
从而导致相减结果偏大或者偏小。
当相减结果偏大的部分一直累加直至在第18次计算时出现负值，
从而出现加和的情况，偏差值进一步扩大
'''