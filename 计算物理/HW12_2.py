import matplotlib.pyplot as plt
from matplotlib import rcParams

# 1. 配置中文字体
rcParams['font.sans-serif'] = ['SimHei']
rcParams['axes.unicode_minus'] = False

class LCG:
    def __init__(self, seed: int = 1, a: int = 1664525, c: int = 1013904223, m: int = 2**32):
        self.state = seed & m
        self.a = a
        self.c = c
        self.m = m

    def rand(self) -> int:
        """返回 0 <= X < m 的下一个伪随机整数"""
        self.state = (self.a * self.state + self.c) % self.m
        return self.state

    def rand_float(self) -> float:
        """返回 0.0 <= x < 1.0 的浮点伪随机数"""
        return self.rand() / self.m

# 设置不同参数集
param_sets = [
    {'name': 'a=4, c=1, m=2**31-1', 'a': 4, 'c': 1, 'm': 2**31-1},
    {'name': 'a=13, c=14, m=482', 'a': 13, 'c': 14, 'm': 482},
    {'name': 'a=6, c=5, m=27', 'a': 6, 'c': 5, 'm': 27},
    {'name': 'a=4, c=1, m=9', 'a': 4, 'c': 1, 'm': 9},

]

N = 2000

plt.figure()

# 对每种参数集计算并绘图
for params in param_sets:
    rng = LCG(seed=654321, a=params['a'], c=params['c'], m=params['m'])
    running_means = []
    cum_sum = 0.0
    for i in range(1, N + 1):
        cum_sum += rng.rand_float()
        running_means.append(cum_sum / i)
    plt.plot(range(1, N + 1), running_means, label=params['name'])

plt.axhline(0.5, linestyle='--', label='理论期望 = 0.5')
plt.xlabel('迭代次数')
plt.ylabel('累计均值')
plt.ylim(0.45, 0.58)
plt.title('不同 LCG 参数下累计均值随迭代次数的变化')
plt.legend()
plt.tight_layout()
plt.show()

