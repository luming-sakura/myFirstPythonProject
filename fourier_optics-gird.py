import numpy as np
import matplotlib.pyplot as plt


def generate_patterns(size):
    patterns = []
    grid = np.zeros((size, size))
    for i in range(0, size, size // 10):
        grid[i, :] = 1
        grid[:, i] = 1
    patterns.append(grid)
    horizontal = np.zeros((size, size))
    for i in range(0, size, size // 10):
        horizontal[i, :] = 1
    patterns.append(horizontal)
    vertical = np.zeros((size, size))
    for i in range(0, size, size // 10):
        vertical[:, i] = 1
    patterns.append(vertical)
    diagonal = np.zeros((size, size))
    for i in range(-size, size, size // 10):
        diagonal += np.eye(size, size, k=i)
    patterns.append(diagonal)
    return patterns
def generate_spectrums(size):
    spectrums = []

    # (a) 网格频谱
    spectrum_a = np.zeros((size, size))
    for i in range(-3, 4):
        for j in range(-3, 4):
            spectrum_a[size // 2 + i * 8, size // 2 + j * 8] = 1

    spectrums.append(spectrum_a)

    # (b) 水平线频谱
    spectrum_b = np.zeros((size, size))
    for i in range(-3, 4):
        spectrum_b[size // 2 + i * 8, size // 2] = 1
    spectrums.append(spectrum_b)

    # (c) 垂直线频谱
    spectrum_c = np.zeros((size, size))
    for i in range(-3, 4):
        spectrum_c[size // 2, size // 2 + i * 8] = 1
    spectrums.append(spectrum_c)

    # (d) 斜对角线频谱
    spectrum_d = np.zeros((size, size))
    for i in range(-3, 4):
        spectrum_d[size // 2 - i * 8, size // 2 + i * 8] = 1
    spectrums.append(spectrum_d)

    return spectrums


def plot_all():
    """
    绘制所有图案和频谱
    """
    size = 64  # 图像大小
    patterns = generate_patterns(size)
    spectrums = generate_spectrums(size)
    titles = ['(a) Grid', '(b) Horizontal Lines', '(c) Vertical Lines', '(d) Diagonal Lines']

    plt.figure(figsize=(12, 8))
    for i, (pattern, spectrum) in enumerate(zip(patterns, spectrums)):
        # 图案
        plt.subplot(4, 2, 2 * i + 1)
        plt.title(f"{titles[i]} - Pattern")
        plt.imshow(pattern, cmap='gray')
        plt.axis('off')

        # 频谱
        plt.subplot(4, 2, 2 * i + 2)
        plt.title(f"{titles[i]} - Spectrum")
        plt.imshow(np.log(1 + spectrum), cmap='hot')
        plt.axis('off')

    plt.tight_layout()
    plt.show()


# 运行绘制
plot_all()
