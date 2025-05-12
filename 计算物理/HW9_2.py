import numpy as np

# 被积函数
def f(x):
    return np.sin(np.sqrt(100 * x))**2

# 复化梯形规则
def trap(N):
    h = 1.0 / N
    x = np.linspace(0, 1, N+1)
    y = f(x)
    return h * (0.5*y[0] + y[1:-1].sum() + 0.5*y[-1])

# 复化 Simpson 规则 (要求 N 必须是偶数)
def simpson(N):
    if N % 2 != 0:
       N += 1
    h = 1.0 / N
    x = np.linspace(0, 1, N+1)
    y = f(x)
    return (h/3) * (y[0] + y[-1] + 4 * y[1:-1:2].sum() + 2 * y[2:-1:2].sum())

# 目标精度
eps = 1e-10

print("(a) 复化梯形规则")
N = 2
I_prev = trap(N)
print(f"N = {N:6d},  I = {I_prev:.12f},  Δ = {'—':>12}")
while True:
    N *= 2
    I_curr = trap(N)
    err = abs(I_curr - I_prev)
    print(f"N = {N:6d},  I = {I_curr:.12f},  Δ = {err:.2e}")
    if err < eps:
        break
    I_prev = I_curr

print("\n(b) 复化 Simpson 规则")
N = 2
I_prev = simpson(N)
print(f"N = {N:6d},  I = {I_prev:.12f},  Δ = {'—':>12}")
while True:
    N *= 2
    I_curr = simpson(N)
    err = abs(I_curr - I_prev)
    print(f"N = {N:6d},  I = {I_curr:.12f},  Δ = {err:.2e}")
    if err < eps:
        break
    I_prev = I_curr
