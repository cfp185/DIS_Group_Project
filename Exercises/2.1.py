import numpy as np
import matplotlib.pyplot as plt


# a)
def f(x):
    return np.sin(x)

def f_prime(x):
    return np.cos(x)

x = np.linspace(0, 2 * np.pi, 20, endpoint=False)
delta_x = 2 * np.pi / 20

numerical_derivative = (np.roll(f(x), -1) - f(x)) / delta_x
numerical_derivative[-1] = (f(x[0] + delta_x) - f(x[-1])) / delta_x
true_derivative = f_prime(x)

# Plot the results
plt.plot(x, numerical_derivative, label='Numerical Derivative')
plt.plot(x, true_derivative, label='True Derivative')
plt.xlabel('x')
plt.ylabel('Derivative')
plt.legend()
plt.title('Numerical vs. True Derivative of f(x) = sin(x)')
plt.grid(True)
plt.show()

#b)
def compute_derivative_periodic(f_vals, coeffs, shifts, h):
    N = len(f_vals)
    N_coeffs = len(coeffs)
    padding = N_coeffs // 2

   
    padded_f_vals = np.concatenate([f_vals[-padding:], f_vals, f_vals[:padding]])

    # Compute the derivative
    derivative = np.zeros(N)
    for i in range(N):
        for coeff, shift in zip(coeffs, shifts):
            derivative[i] += coeff * padded_f_vals[i + shift + padding]
    derivative /= delta_x
    return derivative

schemes = [
    {"coeffs": [0, 0, 0, -1, 1, 0, 0, 0], "shifts": [-3, -2, -1, 0, 1, 2, 3, 4]},  # First row in the table
    {"coeffs": [0, 0, -1/2, 0, 1/2, 0, 0, 0], "shifts": [-3, -2, -1, 0, 1, 2, 3, 4]},  # Second row in the table
    {"coeffs": [0, 1/12, -2/3, 0, 2/3, -1/12, 0, 0], "shifts": [-3, -2, -1, 0, 1, 2, 3, 4]},  # Third row in the table
    {"coeffs": [-1/60, 3/20, -3/4, 0, 3/4, -3/20, 1/60, 0], "shifts": [-3, -2, -1, 0, 1, 2, 3, 4]},  # Fourth row in the table
]

labels = ["$O(\Delta x)$", "$O(\Delta x^2)$", "$O(\Delta x^4)$", "$O(\Delta x^6)$"]
colors = ['blue', 'green', 'red', 'purple']

for scheme, label, color in zip(schemes, labels, colors):
    derivative = compute_derivative_periodic(f(x), scheme["coeffs"], scheme["shifts"], delta_x)
    plt.plot(x, derivative, label=label, color=color)

plt.plot(x, np.cos(x), label="True derivative", color='black', linestyle='dashed')

plt.legend()
plt.xlabel('x')
plt.ylabel('f\'(x)')
plt.title('Numerical derivative schemes')
plt.grid(True)
plt.show()

#c
true_derivative = np.cos(x)

for scheme, label in zip(schemes, labels):
    numerical_derivative = compute_derivative_periodic(f(x), scheme["coeffs"], scheme["shifts"], delta_x)
    max_abs_error = np.max(np.abs(true_derivative - numerical_derivative))
    print(f"Max absolute error for {label}: {max_abs_error}")

#d
N_values = np.logspace(1, 6, 50, dtype=int)

max_abs_errors = {label: [] for label in labels}

# Define the analytical derivative 
def f_prime(x):
    return np.cos(x)

for N in N_values:
    x = np.linspace(0, 2 * np.pi, 20, endpoint=False)
    delta_x = 2 * np.pi / 20
    true_derivative = f_prime(x)
  
    for scheme, label in zip(schemes, labels):
        numerical_derivative = compute_derivative_periodic(f(x), scheme["coeffs"], scheme["shifts"], delta_x)
        max_abs_error = np.max(np.abs(true_derivative - numerical_derivative))
        max_abs_errors[label].append(max_abs_error)

for label, color in zip(labels, colors):
    plt.loglog(N_values, max_abs_errors[label], label=label, color=color)

# Plot settings
plt.legend()
plt.xlabel('N')
plt.ylabel('Max absolute error')
plt.title('Max absolute error of each method as a function of N')
plt.grid(True)
plt.show()

#e
# Best accuracy for second order method
best_accuracy_second_order = min(max_abs_errors["$O(\Delta x^2)$"])
print(f"Best accuracy for second order method: {best_accuracy_second_order}")

# Best accuracy for sixth order method
best_accuracy_sixth_order = min(max_abs_errors["$O(\Delta x^6)$"])
print(f"Best accuracy for sixth order method: {best_accuracy_sixth_order}")

#f
N = 100
x = np.linspace(0, 2 * np.pi, N, endpoint=False)
true_derivative = f_prime(x)

numerical_derivative_fourth_order = compute_derivative_periodic(f(x), schemes[2]["coeffs"], schemes[2]["shifts"], delta_x)

# Compute the max absolute error
max_abs_error_fourth_order_at_N_100 = np.max(np.abs(true_derivative - numerical_derivative_fourth_order))
print(f"Max absolute error: {max_abs_error_fourth_order_at_N_100}")

N_for_second_order = next(N for N, error in zip(N_values, max_abs_errors["$O(\Delta x^2)$"]) if error <= max_abs_error_fourth_order_at_N_100)
print(f"Amount of grid points: {N_for_second_order}")

#g
dx_values = 2 * np.pi / N_values

for i, label in enumerate(labels):
    plt.loglog(dx_values, dx_values**(i+1), label=f"~ $\Delta x^{i+1}$")

plt.loglog(dx_values, 5 * 10**-16 / dx_values, label="5 * $10^{-16}$ / $\Delta x$")

# Compute and plot the max absolute error for each method
for label in labels:
    plt.loglog(dx_values, max_abs_errors[label], label=label)

# Plot settings
plt.xlabel('N')
plt.ylabel('Max Absolute Error')
plt.title('Max Absolute Error vs. Grid Spacing')
plt.legend()
plt.grid(True)
plt.show()


