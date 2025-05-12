import numpy as np

def f(x):
    return x ** 4 - 2 * x + 1

# 梯形
def trapezoidal_rule(a, b, n):
    x = np.linspace(a, b, n+1)
    y = f(x)
    h = (b - a) / n
    integral = (h / 2) * np.sum(y[0:-1] + y[1:])
    return integral

# 辛普森
def simpsons_rule(a, b, n):
    x = np.linspace(a, b, n+1)
    y = f(x)
    h = (b - a) / n
    integral = (h / 3) * (y[0] + 4 * np.sum(y[1:-1:2]) + 2 * np.sum(y[2:-2:2]) + y[-1])
    return integral

# 定义相对误差函数
def calculate_error(approx_value, exact_value):
    return abs(approx_value - exact_value) / exact_value

a = 0
b = 2
exact_value = 4.4


n = 1000
trapezoidal_result = trapezoidal_rule(a, b, n)
trapezoidal_error = calculate_error(trapezoidal_result, exact_value)

simpsons_result = simpsons_rule(a, b, n)
simpsons_error = calculate_error(simpsons_result, exact_value)

print(f"使用梯形法则的积分结果: {trapezoidal_result}")
print(f"梯形法则的相对误差: {trapezoidal_error * 100:.5f}%")

print(f"使用辛普森法则的积分结果: {simpsons_result}")
print(f"辛普森法则的相对误差: {simpsons_error * 100:.5f}%")