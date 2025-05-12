import math
import numpy as np
from mpmath import mp

def e_sum(x, N):
    S = 0.00
    for i in range(N):
        S = S + math.pow(x, i) / math.factorial(i)
    print(S)
e_sum(10, 30)
e_sum(-2, 20)
e_sum(2, 30)
e_sum(-10, 30)

# 单精度
def e_sum_negative_float32(x, N):
    S = np.float32(0.00)
    x_negative = x * (-1)
    for i in range(N):
        S = S + math.pow(x_negative, i) / math.factorial(i)
        K = 1 / S
    print(K)
e_sum_negative_float32((-2), 30)
e_sum_negative_float32((-10), 30)

# 双精度
def e_sum_negative_float64(x, N):
    S = 0.00
    x_negative = x * (-1)
    for i in range(N):
        S = S + math.pow(x_negative, i) / math.factorial(i)
        K = 1 / S
    print(K)
e_sum_negative_float64((-2), 30)
e_sum_negative_float64((-10), 30)


# 四精度
def e_sum_negative_float128(x, N):
    mp.dps = 34
    S = mp.mpf(0.00)
    x_negative = x * (-1)
    for i in range(N):
        S = S + math.pow(x_negative, i) / math.factorial(i)
        K = 1 / S
    print(K)
    print(type(K))
e_sum_negative_float128((-2), 30)
e_sum_negative_float128((-10), 30)


'''
我们发现，当调用函数为e_sum时，x=10,2，-2的值与标准值相差不大，但是当x=-10时，差距较大；此时采用e_sum_negative函数，x=-10时与标准值相差不大

正向级数（e_sum）在N=30时已接近收敛，且所有项均为正数，累加时无符号震荡，浮点数误差较小。其倒数 1/S 的误差被显著抑制。

交替级数（e_sum_negative)在N=30 时尚未完全收敛，且正负项相消导致中间结果震荡，放大了浮点数精度误差。
'''
