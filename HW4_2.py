import numpy as np
import matplotlib.pyplot as plt

def expanded_single(x):
    x = np.float32(x)
    return (x**12 - 12*x**11 + 66*x**10 - 220*x**9 + 495*x**8 - 792*x**7 +
            924*x**6 - 792*x**5 + 495*x**4 - 220*x**3 + 66*x**2 - 12*x + 1)

def direct_single(x):
    x = np.float32(x)
    return (x - 1)**12

x_values = np.linspace(0.7, 1.3, 1000)

expanded_single_values = [expanded_single(x) for x in x_values]
direct_single_values = direct_single(x_values)

plt.plot(x_values, expanded_single_values, label="Expanded (Single Precision)")
plt.plot(x_values, direct_single_values, label="Direct (Single Precision)", linestyle="--")
plt.xlabel("x")
plt.ylabel("Value")
plt.title("Expanded & Direct Calculation")
plt.legend()
plt.grid()
plt.show()

relative_errors = np.abs((expanded_single_values - direct_single_values) / direct_single_values)

plt.plot(x_values, relative_errors, label="Relative Error (Single Precision)")
plt.xlabel("x")
plt.ylabel("Relative Error")
plt.title("Relative Error of Expanded (x-1)^12 (Single Precision)")
plt.legend()
plt.grid()
plt.show()

def horner_double(x):
    return 1 + x*(-12 + x*(66 + x*(-220 + x*(495 + x*(-792 + x*(924 + x*(-792 + x*(495 + x*(-220 + x*(66 + x*(-12 + x)))))))))))

horner_values = [horner_double(x) for x in x_values]

horner_errors = np.abs((horner_values - direct_single_values) / direct_single_values)

plt.plot(x_values, relative_errors, label="Expanded (Single Precision)")
plt.plot(x_values, horner_errors, label="Horner (Double Precision)", linestyle="--")
plt.xlabel("x")
plt.ylabel("Relative Error")
plt.title("Error Comparison: Expanded vs Horner Method")
plt.legend()
plt.grid()
plt.show()