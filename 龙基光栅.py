import matplotlib.pyplot as plt
import numpy as np
import math
pi = math.pi
Lambda = 0.0000005
theta = np.linspace(-0.04, 0.04, 1000)
d = 0.000030
a = 0.000015
N = 10
k = 2 * pi / Lambda
delta = k * d * np.sin(theta)
alpha = k * a * np.sin(theta) / 2
I_d = ((np.sin(alpha)) / alpha) ** 2
beta = delta / 2
I_i = (np.sin(N * beta) / np.sin(beta)) ** 2 / N ** 2
A_0 = 1
I_total = A_0 * I_d * I_i
K_2 = 1
K_1 = K_2 * d / a
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
ax1.plot(np.sin(theta), I_d, label='I_d', color='red', linestyle='dashed')
ax1.plot(np.sin(theta), I_i, label='I_i', color='darkgreen')
ax1.set_xlabel(r'$\sin \theta$')
ax1.set_ylim(0, 1)
# ax1.set_ylabel('Y-axis')
ax1.legend(loc='upper right')

ax2.plot(np.sin(theta), I_d, label='I_d', color='red', linestyle='dashed')
ax2.plot(np.sin(theta), I_total, label='I_total', color='darkgreen')
ax2.set_xlabel(r'$\sin \theta$')
ax2.set_ylim(0, 1)
# plt.ylabel('Y-axis')
ax2.legend(loc='upper right')

plt.show()
