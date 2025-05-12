import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline, splrep, splev
from scipy.integrate import quad

# Problem 1: Linear spline interpolation for rocket velocity at t=16
t1 = np.array([0, 10, 15, 20, 22.5, 30])
v1 = np.array([0, 227.04, 362.78, 517.35, 602.97, 901.67])
v16_linear = np.interp(16, t1, v1)
print(f"Problem 1: Velocity at t=16 (linear spline) = {v16_linear:.4f} m/s")

# Problem 2: Quadratic spline interpolation for rocket
# We fit a quadratic spline using scipy's splrep (k=2)
t2, v2 = t1, v1
tck2 = splrep(t2, v2, k=2)
v16_quad = splev(16, tck2)
# Approximate acceleration as derivative of spline
# For quadratic, derivative is linear per interval; approximate via finite diff
dv_dt = splev(16, tck2, der=1)
# Distance covered between t=11 and t=16 via numerical integration of spline
dist_11_16 = quad(lambda x: splev(x, tck2), 11, 16)[0]

print(f"Problem 2: Velocity at t=16 (quadratic spline) = {v16_quad:.4f} m/s")
print(f"Acceleration at t=16 ≈ {dv_dt:.4f} m/s²")
print(f"Distance covered between t=11 and t=16 ≈ {dist_11_16:.4f} m")

# Problem 3: Cubic splines (natural and clamped) for zener diode I-V data
V = np.array([-1.00, 0.00, 1.27, 2.55, 3.82, 4.92, 5.02])
I = np.array([-14.58, 0.00, 0.00, 0.00, 0.00, 0.88, 11.17])

cs_natural = CubicSpline(V, I, bc_type='natural')
# For clamped, approximate endpoint slopes as zero
cs_clamped = CubicSpline(V, I, bc_type=((1, 0.0), (1, 0.0)))

V_fine = np.linspace(V.min(), V.max(), 200)
I_nat = cs_natural(V_fine)
I_clamped = cs_clamped(V_fine)

plt.figure(figsize=(8, 4))
plt.plot(V, I, 'o', label='Data')
plt.plot(V_fine, I_nat, label='Natural Cubic')
plt.plot(V_fine, I_clamped, label='Clamped Cubic')
plt.xlabel('Voltage (V)')
plt.ylabel('Current (mA)')
plt.title('Problem 3: Zener Diode I-V Characteristic')
plt.legend()
plt.grid(True)

# Problem 4: Parametric cubic spline reconstruction of a closed curve
x = np.array([2.5, 1.3, -0.25, 0, 0.25, -1.3, -2.5, -1.3, 0.25, 0, -0.25, 1.3, 2.5])
y = np.array([0, -0.25, 1.3, 2.5, 1.3, -0.25, 0, 0.25, -1.3, -2.5, -1.3, 0.25, 0])
# Compute chord-length parameter t
diffs = np.sqrt(np.diff(x)**2 + np.diff(y)**2)
t4 = np.concatenate([[0], np.cumsum(diffs)])
# Natural cubic splines for x(t) and y(t)
cs_x = CubicSpline(t4, x, bc_type='natural')
cs_y = CubicSpline(t4, y, bc_type='natural')
t_fine = np.linspace(t4[0], t4[-1], 100)
x_fine = cs_x(t_fine)
y_fine = cs_y(t_fine)

plt.figure(figsize=(6, 6))
plt.plot(x, y, 'o', label='Data Points')
plt.plot(x_fine, y_fine, '-', label='Cubic Spline Curve')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Problem 4: Parametric Cubic Spline Reconstruction')
plt.axis('equal')
plt.legend()
plt.grid(True)

plt.show()
