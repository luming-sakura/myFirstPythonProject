import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

years = np.array([1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990])
population = np.array([106.46, 123.08, 132.12, 152.27, 180.67, 205.05, 227.23, 249.46])

normed_x = years-1920

degree = 7
coeffs = np.polyfit(normed_x, population, degree)
poly = np.poly1d(coeffs)

print("七次多项式拟合函数:")
print(poly)

pop_2000_pred = poly(2000-1920)
print(f"\n外推预测: 2000年人口 = {pop_2000_pred:.2f} 百万")

years_fine = np.linspace(1920, 2000, 400)
population_fine = poly(years_fine-1920)

plt.figure(figsize=(10, 6))
plt.plot(years_fine, population_fine, label=f'{degree}次多项式拟合曲线', color='blue')
plt.scatter(years, population, color='red', label='原始数据')
plt.scatter([2000], [pop_2000_pred], color='green', zorder=5, label='外推点')
plt.scatter([2000], [281.42], color='red', zorder=5, label='原始数据')
plt.axvspan(1920, 1990, label='拟合区域', zorder=0, alpha=0.1, color='purple')

plt.title("1920-1990年美国人口数据与七次多项式拟合外推")
plt.xlabel("年份")
plt.ylabel("人口 (百万)")
plt.legend()
plt.grid(True)
plt.show()

# 对外推合理性的讨论：
print("\n讨论：")
print("使用七次多项式对已有数据进行拟合可以较好地通过已有数据点，但是容易出现过拟合现象。过度拟合噪声导致。"
      "在此案例中,这是由于7次多项式对于数据'过拟合'.")
print("例如，对于2000年的预测，由于多项式高次项引起的振荡效应，外推结果完全偏离实际情况。")