import matplotlib.pyplot as plt
import numpy as np
import math

pi_value = math.pi
print(pi_value)

a, b, l_1, l_2 = 1, 2, 500, 400
k_1, k_2 = 2 * math.pi / l_1, 2 * math.pi / l_2
x1 = np.linspace(0, 10 * l_1, 1000)
t1 = 0
x2 = np.linspace(0, 10 * l_1, 1000)
t2 = 0
v_1, v_2 = 3 * 10 ^ 11, 3 * 10 ^ 11
omiga1, omiga2 = k_1 * v_1, k_2*v_2
alpha1, alpha2 = 0, 0
phi1, phi2 = omiga1 * t1 - k_1 * x1 + alpha1, omiga2 * t2 - k_2 * x2 + alpha2
E1 = a * np.cos(phi1)
E2 = b * np.cos(phi2)
E_rms = E1 + E2
A_Strength = 2 * a * np.cos((phi1-phi2)/2)
I_Strength = A_Strength * A_Strength

plt.plot(x1 / l_1, E1, label='E1', color='blue')
plt.plot(x2 / l_1, E2, label='E2', color='red')
plt.title('t=0')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.show()

plt.plot(x1 / l_1, E1 + E2, label='E1', color='blue')
plt.plot(x1 / l_1, A_Strength, label='A', color='red')
plt.title('t=0')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.show()

plt.plot(x1 / l_1, I_Strength, label='I', color='red')
plt.title('t=0')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.show()