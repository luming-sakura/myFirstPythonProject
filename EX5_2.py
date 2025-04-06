import math

def f(x):
    return 2 - x - math.exp(-x)

def secant_method(x0, x1, tol=1e-8, max_iter=10000):
    iter_count = 0
    while abs(x1 - x0) > tol and iter_count < max_iter:
        # 计算割线的公式
        if f(x1) == f(x0):  # 防止除零错误
            print("Division by zero error in Secant method.")
            return None

        x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))

        x0, x1 = x1, x2

        iter_count += 1

    return x1


x0 = 0
x1 = 10
root = secant_method(x0, x1)
print(f"The root is approximately: {root}")
