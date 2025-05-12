import numpy as np

x_values = np.array([0.8, 0.9, 1.0, 1.1, 1.2])
f_values = np.array([1.334900088177337, 1.86570597834893, 2.718281828459045, 4.163309543192145, 6.755260649292601])

def forward_diff(f_values, h):
    f_prime = (f_values[1:] - f_values[:-1]) / h
    f_double_prime = (f_values[2:] - 2 * f_values[1:-1] + f_values[:-2]) / (h**2)
    f_triple_prime = (f_values[3:] - 3 * f_values[2:-1] + 3 * f_values[1:-2] - f_values[:-3]) / (h**3)
    return f_prime, f_double_prime, f_triple_prime

h_values = [0.1, 0.01, 0.001, 0.0001]
for h in h_values:
    f_prime, f_double_prime, f_triple_prime = forward_diff(f_values, h)
    print(f"当h={h}时，")
    print(f"  f'(x)近似值: {f_prime}")
    print(f"  f''(x)近似值: {f_double_prime}")
    print(f"  f'''(x)近似值: {f_triple_prime}")
    print()
'''
a)分析：
h=0.1：对于较大的h值，计算结果通常较为粗糙，可能偏离实际解。
h=0.01, h=0.001：较小的h值会提供更精确的结果，但计算机的浮动误差开始影响结果的准确性。
h=0.0001：在这个值下，数值误差可能会因为太小的步长而增大，导致最终的近似结果变差。
通常情况下，h=0.01或h=0.001是一个较好的选择，它们在精度和数值稳定性之间取得了良好的平衡。
b)h越小不一定越好。当h值非常小时，计算中涉及的分母（如h、h²等）会导致数值变得非常小，从而增加计算误差。
例如，有限差分公式在计算导数时，h值越小，公式中的差值越小，导致计算机误差放大，最终结果变得不准确。
因此，最优的h值是通过实际计算得到的，它能够在精度和稳定性之间找到一个合适的平衡。
'''