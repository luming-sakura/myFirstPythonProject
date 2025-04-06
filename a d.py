import numpy as np
import matplotlib.pyplot as plt


def diffraction_angles(d, wavelength, theta_i, max_order=5):
    """
    计算龙基光栅的衍射角度
    :param d: 光栅周期
    :param wavelength: 光波的波长
    :param theta_i: 入射角（弧度制）
    :param max_order: 最大衍射阶数
    :return: 各阶的衍射角度（以弧度表示）
    """
    # 计算衍射角度的公式
    angles = []
    for m in range(-max_order, max_order + 1):
        # 衍射方程：m * λ = d * (sin(θi) + sin(θm))
        sin_theta_m = (m * wavelength / d) - np.sin(theta_i)

        # 限制 sin 的值在 -1 到 1 之间
        if -1 <= sin_theta_m <= 1:
            theta_m = np.arcsin(sin_theta_m)
            angles.append((m, theta_m))

    return angles
# 参数设置
wavelength = 650e-9  # 光波波长 (650 nm)
d = 1e-6            # 光栅周期 (1 µm)
theta_i = np.deg2rad(0)  # 入射角 0° (正射入射)

# 计算衍射角度
angles = diffraction_angles(d, wavelength, theta_i, max_order=5)

# 绘制衍射图像
plt.figure(figsize=(8, 6))
for m, theta_m in angles:
    plt.plot([m, m], [0, 1], label=f"m={m}, θ={np.rad2deg(theta_m):.2f}°", marker='o')

plt.title("Diffraction Angles for Langevin Grating")
plt.xlabel("Diffraction Order (m)")
plt.ylabel("Intensity")
plt.legend()
plt.grid(True)
plt.show()


def interference_intensity(angles, wavelength, d, theta_i):
    """
    计算各阶衍射的干涉强度
    :param angles: 各阶衍射角度 (θm)
    :param wavelength: 光波的波长
    :param d: 光栅周期
    :param theta_i: 入射角
    :return: 干涉强度列表
    """
    intensities = []
    for m, theta_m in angles:
        phase_difference = 2 * np.pi * d * (np.sin(theta_m) - np.sin(theta_i)) / wavelength
        intensity = np.cos(phase_difference / 2) ** 2
        intensities.append((m, intensity))

    return intensities
# 计算干涉强度
intensities = interference_intensity(angles, wavelength, d, theta_i)

# 绘制干涉强度图
plt.figure(figsize=(8, 6))
orders = [m for m, _ in intensities]
intensity_values = [I for _, I in intensities]

plt.bar(orders, intensity_values, color='blue', alpha=0.7)
plt.title("Interference Intensity for Langevin Grating")
plt.xlabel("Diffraction Order (m)")
plt.ylabel("Intensity")
plt.grid(True)
plt.show()
