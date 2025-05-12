import numpy as np
import matplotlib.pyplot as plt
import mpmath

mpmath.mp.dps = 34
def func1(x):
    return (x - 1) ** 7
def func2(x):
    return mpmath.power(x, 7) - 7 * mpmath.power(x, 6)\
        + 21 * mpmath.power(x, 5) - 35 * mpmath.power(x, 4)\
        + 35 * mpmath.power(x, 3) - 21 * mpmath.power(x, 2) + 7 * x - 1



x = np.linspace(0.9, 1.1, 100)
y1 = [func1(i) for i in x]


plt.subplot(231)
plt.plot(x, y1, label='(x - 1)^7')
plt.xlabel('x')
plt.ylabel('Value')
plt.suptitle('Comparison of (x - 1)^7 and its Expansion')
plt.legend()
# plt.show()

x = np.linspace(0.99, 1.01, 100)
y1 = [func1(i) for i in x]
plt.subplot(232)
plt.plot(x, y1, label='(x - 1)^7')
plt.xlabel('x')
plt.ylabel('Value')
plt.legend()
#plt.show()

x = np.linspace(0.998, 1.002, 100)
y1 = [func1(i) for i in x]
plt.subplot(233)
plt.plot(x, y1, label='(x - 1)^7')
plt.xlabel('x')
plt.ylabel('Value')
plt.legend()

x = np.linspace(0.9, 1.1, 100)
y2 = [func2(i) for i in x]
plt.subplot(234)
plt.plot(x, y2, 'x', label='Expansion of (x - 1)^7')
plt.xlabel('x')
plt.ylabel('Value')
plt.legend()

x = np.linspace(0.99, 1.01, 100)
y2 = [func2(i) for i in x]
plt.subplot(235)
plt.plot(x, y2,'x', label='Expansion of (x - 1)^7')
plt.xlabel('x')
plt.ylabel('Value')
plt.legend()

x = np.linspace(0.998, 1.002, 50)
y2 = [func2(i) for i in x]
plt.subplot(236)
plt.plot(x, y2, 'x', label='Expansion of (x - 1)^7')
plt.xlabel('x')
plt.ylabel('Value')
plt.legend()

plt.show()