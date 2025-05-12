import numpy as np
import matplotlib.pyplot as plt

V_cm3 = 1000  # 样本体积：1000 cm^3
V = V_cm3 * 1e-6  # 转换为 m^3
rho = 6.022e28  # 原子数密度 (m^-3)
k_B = 1.380649e-23  # Boltzmann 常数 (J/K)
theta_D = 428  # Debye 温度 (K)
N = 50  # Simpson 划分数

def C_v(T):
    u = theta_D / T
    x = np.linspace(0, u, N + 1)
    f = x ** 4 * np.exp(x) / (np.exp(x) - 1) ** 2
    f[0] = 0.0
    dx = u / N
    integral = dx / 3 * (f[0] + f[-1]+ 4 * np.sum(f[1:-1:2])+ 2 * np.sum(f[2:-1:2]))

    return 9 * V * rho * k_B * (T / theta_D) ** 3 * integral



T_vals = np.linspace(5, 500, 200)
C_vals = [C_v(T) for T in T_vals]

plt.figure(figsize=(8, 5))
plt.plot(T_vals, C_vals, lw=2)
plt.xlabel('Temperature $T$ (K)')
plt.ylabel(r'Heat capacity $C_V$ (J/K)')
plt.title('Debye Model Heat Capacity of Aluminum')
plt.grid(True)
plt.tight_layout()
plt.show()
