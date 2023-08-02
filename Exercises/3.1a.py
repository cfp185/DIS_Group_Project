import numpy as np
import matplotlib.pyplot as plt

# Define parameters
alpha = 205
t0 = 0
tf = 100
dt = 0.01
x0 = 0

# Initialize variables
time_values = np.arange(t0, tf + dt, dt)            # An array that stores the discrete time values
                                                    # from t0 to tf with a step size of dt.
numerical_solution = np.zeros_like(time_values)     # An array that holds the numerical approximation
                                                    # of x(t) at each time step.
numerical_solution[0] = x0

# Explicit Euler method
for i in range(1, len(time_values)):
    current_time = time_values[i]                                   # Current time at each iteration.
    previous_solution = numerical_solution[i - 1]                   # The numerical solution at the
                                                                    # previous time step.
    x_prime = alpha * (np.sin(current_time) - previous_solution)    # Stores x'(t) with respect to
                                                                    # time, calculated using the given ODE.
    delta_x = x_prime * dt                                          # The change in the numerical
                                                                    # solution x(t) at each time step using
                                                                    # the explicit Euler Method
    numerical_solution[i] = previous_solution + delta_x

# Analytical solution
x_values_analytical = (alpha / (1 + alpha**2)) * (np.exp(-alpha * time_values) - np.cos(time_values) + alpha * np.sin(time_values))

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(time_values, numerical_solution, label='Explicit Euler')
plt.plot(time_values, x_values_analytical, label='Analytical Solution')
plt.xlabel('t')
plt.ylabel('x(t)')
plt.legend()
plt.title('Comparison of Explicit Euler Method with Analytical Solution (alpha = 205)')
plt.grid(True)
plt.show()

