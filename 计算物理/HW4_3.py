'''
半精度浮点数（Half-precision floating-point）通常使用16位二进制表示，遵循IEEE 754标准。其结构如下：
- 1位符号位
- 5位指数位
- 10位尾数位

对于半精度浮点数，机器精度约为 2^(-10) ≈ 9.77 *10^(-4)

半精度浮点数的范围取决于指数位。其表示的范围大约为：
- 最小正数（最小非零正数）：2^(-14) ≈ 6.10 * 10^(-5)
- 最大正数：2^（15）*(2 - 2^（-10) ）≈ 65504
'''
' 舍入误差 '
import numpy as np

a = np.float16(1.0)
b = np.float16(0.0001)

result = np.float16(0.0)
for _ in range(10000):
    result += b

print(f"累加结果: {result}")
print(f"误差: {abs(result - 1.0)}")