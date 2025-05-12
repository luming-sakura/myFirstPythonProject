import numpy as np

def f(x):
    return np.sin(x)

def romberg_integration(f, a, b, max_n):
    R = np.zeros((max_n, max_n), dtype=np.float64)

    R[0, 0] = (b - a) / 2 * (f(a) + f(b))

    for i in range(1, max_n):
        h = (b - a) / (2 ** i)
        sum_f = sum(f(a + (2 * k - 1) * h) for k in range(1, 2 ** (i - 1) + 1))
        R[i, 0] = 0.5 * R[i - 1, 0] + h * sum_f

        for k in range(1, i + 1):
            R[i, k] = R[i, k - 1] + (R[i, k - 1] - R[i - 1, k - 1]) / (4 ** k - 1)

    return R

a = 0
b = np.pi
max_n = 7

R = romberg_integration(f, a, b, max_n)

np.set_printoptions(precision=8, suppress=True)
for i in range(max_n):
    row = ["{:.8f}".format(R[i, j]) if j <= i else "" for j in range(max_n)]
    print("\t".join(row))

'''
当 n 增大时，Romberg 表中的数值迅速趋于真实值（2），因为该方法是利用 Richardson 外推优化的复合梯形法，收敛速度是指数级的。尤其是对于解析性良好的函数（如sinx），Romberg 方法表现非常优秀。
'''