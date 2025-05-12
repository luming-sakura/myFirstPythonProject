import numpy as np

def simpson(f, a, b, n):
    """
    复合 Simpson 法进行数值积分。

    参数：
    - f: 被积函数，接受 numpy 数组输入
    - a: 积分下限
    - b: 积分上限
    - n: 子区间数（必须为偶数；若为奇数，则自动加一）

    返回：
    - 积分近似值
    """
    # 确保子区间数为偶数
    if n % 2 == 1:
        n += 1
    h = (b - a) / n  # 步长
    x = np.linspace(a, b, n + 1)  # 划分节点
    y = f(x)  # 计算函数值
    S = y[0] + y[-1] + 4 * np.sum(y[1:-1:2]) + 2 * np.sum(y[2:-2:2])
    return S * h / 3

# a) 计算 I = ∫_{-1}^{1} sqrt(1 - x^2) dx
f_a = lambda x: np.sqrt(1 - x**2)
I_a = simpson(f_a, -1, 1, 1000)
print(f"积分 a) ≈ {I_a:.6f} (精确值 = π ≈ {np.pi:.6f})")

# b) 计算 I = ∫_{0}^{π} sin^2 θ dθ
f_b = lambda theta: np.sin(theta)**2
I_b = simpson(f_b, 0, np.pi, 1000)
print(f"积分 b) ≈ {I_b:.6f} (精确值 = π/2 ≈ {np.pi/2:.6f})")

# c) 计算 I = ∫_{0}^{∞} 1/((1+x) √x) dx
# 使用替换 x = tan^2 θ, θ ∈ [0, π/2), 则 dx = 2 tan θ sec^2 θ dθ
# 积分被简化为常数 2 的积分
f_c = lambda theta: 2.0
I_c = simpson(f_c, 0, np.pi/2, 1000)
print(f"积分 c) ≈ {I_c:.6f} (精确值 = π ≈ {np.pi:.6f})")