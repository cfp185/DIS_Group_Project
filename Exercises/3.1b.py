import numpy as np
import matplotlib.pyplot as plt

# Define parameters
alpha = 0.1
t0 = 0
tf = 100
dt = 0.01
x0 = 0

time_values = np.arange(t0, tf + dt, dt)            # An array that stores the discrete time values
                                                    # from t0 to tf with a step size of dt.

# Implicit Euler method
def implicitEuler(dt, alpha, time_values):    
    x_values = np.zeros_like(time_values)
    x_values[0] = x0
    for i in range(1, len(time_values)):
        x_values[i] = (x_values[i - 1] + dt*alpha*np.sin(time_values[i]+dt)) / (1+dt*alpha)
    return x_values

# Analytical solution
x_values_analytical = (alpha / (1 + alpha**2)) * (np.exp(-alpha * time_values) - np.cos(time_values) + alpha * np.sin(time_values))


# Plotting
plt.figure(figsize=(10, 6))
#plt.plot(time_values, implicitEuler, label='Implicit Euler')
#plt.plot(time_values, x_values_analytical, label='Analytical Solution')
plt.plot(time_values, implicitEuler(dt, alpha, time_values),label='Implicit Euler')
plt.plot(time_values, x_values_analytical, '--', label='Analytical Solution')
plt.xlabel('t')
plt.ylabel('x(t)')
plt.legend()
plt.title('Comparison of Implicit Euler Method with Analytical Solution (alpha = 0.1)')
plt.grid(True)
plt.show()

