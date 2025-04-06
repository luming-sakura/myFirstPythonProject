import math

def compute_sequence(n_max):
    z = [0] * (n_max + 1)
    z[2] = 2
    for n in range(2, n_max):
        z[n+1] = 2 ** (n - 0.5) * math.sqrt(1 - math.sqrt(1 - 4 ** (1 - n) * z[n] ** 2))
    return z

n_max = 40
z = compute_sequence(n_max)
for n in range(2, n_max + 1):
    print(f"z[{n}] = {z[n]}, 误差 = {abs(z[n] - math.pi)}")
    '''当n>=30时，舍入误差会显著影响计算结果。在计算过程中，涉及到大量的乘方和开方运算，这些运算会放大初始的舍入误差。特别是在计算 sqrt{1 - 4^{1-n} z_n^2}时，当 n 很大时，4^{1-n} z_n^2 会变得非常小，导致计算结果的不稳定性增加。'''