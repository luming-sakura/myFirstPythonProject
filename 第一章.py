import matplotlib.pyplot as plt
import numpy as np
import math

x1 = np.linspace(-50, 50, 1)
y = np.linspace(-50, 50, 1)
d_1 = 100
f_1 = 400
n = 1.5
r = float(f_1) * (n - 1)
m = r * r - (d_1 / 2) ** 2
h = r - np.sqrt(m)
t = h - r + np.sqrt(r ** 2 - x1 ** 2)
plt.plot(x1, y, t, color='red', linestyle='dashed')

plt.show()