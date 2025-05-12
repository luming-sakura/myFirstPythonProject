import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = ['SimHei']      # Windows 下常见的中文黑体
plt.rcParams['axes.unicode_minus'] = False
# 数据
x = np.array([-1.00, 0.00, 1.27, 2.55, 3.82, 4.92, 5.02])
y = np.array([-14.58, 0.00, 0.00, 0.00, 0.00, 0.88, 11.17])

n = len(x) - 1
h = x[1:] - x[:-1]

# 构造三对角矩阵求解内部二阶导 M[1:n]
A = np.zeros((n-1, n-1))
b = np.zeros(n-1)
for i in range(1, n):
    if i > 1: A[i-1, i-2] = h[i-1]
    A[i-1, i-1] = 2*(h[i-1] + h[i])
    if i < n-1: A[i-1, i] = h[i]
    b[i-1] = 6*((y[i+1]-y[i])/h[i] - (y[i]-y[i-1])/h[i-1])
M = np.zeros(n+1)
M[1:n] = np.linalg.solve(A, b)

# 评估样条
xx = np.linspace(x[0], x[-1], 300)
yy = np.empty_like(xx)
for k, xi in enumerate(xx):
    i = np.searchsorted(x, xi) - 1
    i = min(max(i, 0), n-1)
    hi = h[i]; x0, x1 = x[i], x[i+1]
    M0, M1 = M[i], M[i+1]
    t1 = M0/(6*hi)*(x1 - xi)**3 + M1/(6*hi)*(xi - x0)**3
    t2 = (y[i]/hi - M0*hi/6)*(x1 - xi) + (y[i+1]/hi - M1*hi/6)*(xi - x0)
    yy[k] = t1 + t2

plt.plot(x, y, 'o', label='原始数据')
plt.plot(xx, yy, label='自然三次样条')
plt.xlabel('Voltage (V)'); plt.ylabel('Current (mA)')
plt.legend(); plt.grid(True)
plt.show()
