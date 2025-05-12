import numpy as np

# 定义物理常量
G = 6.674e-11
M = 5.974e24
m = 7.348e22
R = 3.844e8
omega = 2.662e-6

# 定义方程f(r)
def f(r):
    return (G * M / r ** 2) - (G * m / (R - r) ** 2) - omega ** 2 * r

# 割线法迭代求解
def secant_method(x0, x1, tol=1e-8, max_iter=100):
    for i in range(max_iter):
        f0 = f(x0)
        f1 = f(x1)
        if np.abs(f1) < tol:
            return x1
        x_next = x1 - f1 * (x1 - x0) / (f1 - f0)
        x0 = x1
        x1 = x_next
    return x1

# 选择两个初始值
r0 = R / 3
r1 = 2 * R / 3
result = secant_method(r0, r1)
print(f"用割线法求得的r值（保留四位有效数字）: {np.format_float_scientific(result, precision = 4)}")