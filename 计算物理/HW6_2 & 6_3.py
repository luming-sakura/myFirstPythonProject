import numpy as np
import matplotlib.pyplot as plt

def lagrange_interp(x_nodes, y_nodes, x_eval):
    P = np.zeros_like(x_eval, dtype=float)
    n = len(x_nodes)
    for i in range(n):
        # Compute L_i(x_eval)
        li = np.ones_like(x_eval, dtype=float)
        for j in range(n):
            if j != i:
                li *= (x_eval - x_nodes[j]) / (x_nodes[i] - x_nodes[j])
        P += y_nodes[i] * li
    return P

# Problem 2: f(x) = 1 / (1 + x^2)
f2 = lambda x: 1 / (1 + x**2)
x2_nodes = np.linspace(-1, 1, 6)
y2_nodes = f2(x2_nodes)

x2_eval = np.linspace(-1, 1, 300)
y2_true = f2(x2_eval)
y2_interp = lagrange_interp(x2_nodes, y2_nodes, x2_eval)

plt.figure()
plt.plot(x2_eval, y2_true, label='True f(x)')
plt.plot(x2_eval, y2_interp, label='P₅(x)')
plt.plot(x2_nodes, y2_nodes, 'o', label='Nodes')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Problem 2: Lagrange Interpolation of 1/(1+x²)')
plt.legend()
plt.grid(True)

# Problem 3: f(x) = sin(pi*(x + 1/2))
f3 = lambda x: np.sin(np.pi * (x + 0.5))
x3_nodes = np.linspace(-1, 1, 6)
y3_nodes = f3(x3_nodes)

x3_eval = np.linspace(-1, 1, 300)
y3_true = f3(x3_eval)
y3_interp = lagrange_interp(x3_nodes, y3_nodes, x3_eval)

plt.figure()
plt.plot(x3_eval, y3_true, label='True f(x)')
plt.plot(x3_eval, y3_interp, label='P₅(x)')
plt.plot(x3_nodes, y3_nodes, 'o', label='Nodes')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Problem 3: Lagrange Interpolation of sin(π(x+0.5))')
plt.legend()
plt.grid(True)

plt.show()
