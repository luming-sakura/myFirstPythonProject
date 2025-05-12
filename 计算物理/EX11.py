import math
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

x_data = [1, 2, 3, 4, 5, 6]
y_data = [0.7, 1.7, 3.3, 7.3, 10.9, 22.7]

ln_y = [math.log(y) for y in y_data]
n = len(x_data)
sum_x = sum(x_data)
sum_ln_y = sum(ln_y)
sum_x_ln_y = sum(x * y for x, y in zip(x_data, ln_y))
sum_x_squared = sum(x**2 for x in x_data)

b = (n * sum_x_ln_y - sum_x * sum_ln_y) / (n * sum_x_squared - sum_x ** 2)
ln_a = (sum_ln_y - b * sum_x) / n
a = math.exp(ln_a)

print(f"手动拟合结果：a = {a:.4f}, b = {b:.4f}")

x_smooth = np.linspace(min(x_data), max(x_data), 300)
y_manual_fit = [a * math.exp(b * x) for x in x_smooth]
y_given_model = 0.407 * np.exp(0.679 * x_smooth)

plt.figure(figsize=(8, 5))
plt.scatter(x_data, y_data, color='blue', label='原始数据', s=50)
plt.plot(x_smooth, y_manual_fit, color='green', linestyle='--', linewidth=2,
         label=f'手动拟合: y = {a:.3f} * e^({b:.3f}x)')
plt.plot(x_smooth, y_given_model, color='red', linestyle='-', linewidth=2,
         label='给定模型: y = 0.407 * e^(0.679x)')
plt.title('指数拟合对比图（手动实现）')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()
