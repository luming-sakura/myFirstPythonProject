import numpy as np
import math

# 定义被积函数
f = lambda x: 1.0 / (1 + x**2)
I_exact = math.pi / 4

def trapezoid(f, a, b, n):
    """
    复合梯形法
    """
    h = (b - a) / n
    x = np.linspace(a, b, n+1)
    y = f(x)
    return (h/2) * (y[0] + 2 * np.sum(y[1:-1]) + y[-1])

def simpson(f, a, b, n):
    """
    复合 Simpson 法 (n 必须为偶数)
    """
    if n % 2 == 1:
        n += 1
    h = (b - a) / n
    x = np.linspace(a, b, n+1)
    y = f(x)
    S = y[0] + y[-1] + 4*np.sum(y[1:-1:2]) + 2*np.sum(y[2:-2:2])
    return S * h / 3

# Romberg 方法
def romberg(f, a, b, max_k=6):
    """
    Romberg 级化积分，返回 R 矩阵
    R[k,m] = 外推后结果
    """
    R = np.zeros((max_k+1, max_k+1))
    for k in range(max_k+1):
        n = 2**k
        R[k,0] = trapezoid(f, a, b, n)
    for k in range(1, max_k+1):
        for m in range(1, k+1):
            R[k,m] = R[k,m-1] + (R[k,m-1] - R[k-1,m-1]) / (4**m - 1)
    return R

# 设置测试网格 n
ns = [2**k for k in range(3, 12)]  # n = 8,16,...,2048
results = {}

for method_name, method in [('Trapezoid', trapezoid), ('Simpson', simpson)]:
    hs = []
    errs = []
    for n in ns:
        h = 1.0 / n
        I_n = method(f, 0, 1, n)
        err = abs(I_n - I_exact)
        hs.append(h)
        errs.append(err)
    # 转为数组并过滤掉 err=0 的点，避免 log(0)
    hs = np.array(hs)
    errs = np.array(errs)
    mask = errs > 0
    # 拟合 log(err) = p*log(h) + C
    p, C = np.polyfit(np.log(hs[mask]), np.log(errs[mask]), 1)
    results[method_name] = {'h': hs, 'err': errs, 'p_est': p}

# Romberg 误差：取 R[k,k]
R = romberg(f, 0, 1, max_k=6)
romberg_errs = [abs(R[k,k] - I_exact) for k in range(1, 7)]
romberg_h = [1.0 / (2**k) for k in range(1, 7)]
# 同样过滤零误差
errs_r = np.array(romberg_errs)
h_r = np.array(romberg_h)
mask_r = errs_r > 0
p_romberg, _ = np.polyfit(np.log(h_r[mask_r]), np.log(errs_r[mask_r]), 1)
results['Romberg'] = {'h': romberg_h, 'err': romberg_errs, 'p_est': p_romberg}

# 输出各方法收敛阶
print("Method      p_estimate")
for name, res in results.items():
    print(f"{name:10s} {res['p_est']:.2f}")

# 对不同误差容限，求最小 n
epsilons = [10**(-k) for k in range(2, 13)]
min_ns = {name: [] for name in ['Trapezoid', 'Simpson', 'Romberg']}
for eps in epsilons:
    # 梯形与 Simpson
    for name, method in [('Trapezoid', trapezoid), ('Simpson', simpson)]:
        n = 2
        while True:
            I_n = method(f, 0, 1, n)
            if abs(I_n - I_exact) < eps:
                min_ns[name].append(n)
                break
            n *= 2
    # Romberg: 寻找最小 k
    for k in range(1, 7):
        if abs(R[k,k] - I_exact) < eps:
            min_ns['Romberg'].append(2**k)
            break
    else:
        min_ns['Romberg'].append(None)

print("\nEpsilon and minimal n: trapezoid / simpson / romberg")
print("eps", epsilons)
for name in ['Trapezoid', 'Simpson', 'Romberg']:
    print(name, min_ns[name])