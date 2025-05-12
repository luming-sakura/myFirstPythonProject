import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt
from scipy.integrate import quad

time = np.array([0, 10, 15, 20, 22.5, 30])
velocity = np.array([0, 227.04, 362.78, 517.35, 602.97, 901.67])


# Part 1: Linear spline interpolation to find velocity at t=16
linear_spline = interpolate.interp1d(time, velocity)
velocity_at_16_linear = linear_spline(16)

print("Part 1: Using Linear Splines")
print(f"Velocity at t=16 seconds: {velocity_at_16_linear:.2f} m/s")

# Part 2: Using quadratic splines (a₅=0) for the next questions
quadratic_spline = interpolate.make_interp_spline(time, velocity, k=2)

# a) Find velocity at t=16 seconds using quadratic splines
velocity_at_16_quadratic = quadratic_spline(16)
print("\nPart 2: Using Quadratic Splines (a₅=0)")
print(f"a) Velocity at t=16 seconds: {velocity_at_16_quadratic:.2f} m/s")


# b) Find acceleration at t=16 seconds
def velocity_derivative(t):
    delta = 0.001
    return (quadratic_spline(t + delta) - quadratic_spline(t)) / delta

acceleration_at_16 = velocity_derivative(16)
print(f"b) Acceleration at t=16 seconds: {acceleration_at_16:.2f} m/s²")


# c) Find distance covered between t=11 and t=16 seconds
def velocity_function(t):
    return float(quadratic_spline(t))

distance_covered, *rest = quad(velocity_function, 11, 16)

print(f"c) Distance covered between t=11 and t=16 seconds: {distance_covered:.2f} m")

t_smooth = np.linspace(0, 30, 1000)
v_linear = linear_spline(t_smooth[100:])
v_quadratic = quadratic_spline(t_smooth)

plt.figure(figsize=(10, 6))
plt.plot(time, velocity, 'go', label='Data Points')
plt.plot(t_smooth[100:], v_linear, 'r-', label='Linear Spline')
plt.plot(t_smooth, v_quadratic, 'b--', label='Quadratic Spline')
plt.axvline(x=16, color='gray', linestyle=':', label='t=16s')
plt.axhline(y=velocity_at_16_quadratic, color='gray', linestyle=':', label=f'v(16)={velocity_at_16_quadratic:.2f} m/s')
plt.axvspan(11, 16, alpha=0.2, color='yellow', label='Integration Region (t=11 to t=16)')
plt.xlabel('Time (s)')
plt.ylabel('Velocity (m/s)')
plt.title('Rocket Velocity vs Time with Spline Interpolations')
plt.legend()
plt.grid(True)

acceleration = [velocity_derivative(t) for t in t_smooth]
plt.figure(figsize=(10, 6))
plt.plot(t_smooth, acceleration, 'r-', label='Acceleration (derivative of quadratic spline)')
plt.axvline(x=16, color='gray', linestyle=':', label='t=16s')
plt.axhline(y=acceleration_at_16, color='gray', linestyle=':', label=f'a(16)={acceleration_at_16:.2f} m/s²')
plt.xlabel('Time (s)')
plt.ylabel('Acceleration (m/s²)')
plt.title('Rocket Acceleration vs Time from Quadratic Spline')
plt.legend()
plt.grid(True)
plt.show()

print("\nComparison with results shown in Image 1:")
print("Linear (1st order polynomial): Our result = {:.2f} m/s, Image shows = 393.69 m/s".format(velocity_at_16_linear))
print("Quadratic (2nd order polynomial): Our result = {:.2f} m/s, Image shows = 392.19 m/s".format(velocity_at_16_quadratic))
