import numpy as np
import matplotlib.pyplot as plt

# # a)
# # Define the function f(x) = sin(x)
# def f(x):
#     return np.sin(x)

# # Define the analytical derivative f'(x) = cos(x)
# def f_prime(x):
#     return np.cos(x)

# # Define the grid size
# N = 20
# theta = 0

# # Create the grid
# x = np.linspace(theta, 2 * np.pi, N, endpoint=False)

# # Compute the grid spacing
# delta_x = 2 * np.pi / N

# # Evaluate the numerical derivative using the formula
# numerical_derivative = (np.roll(f(x), -1) - f(x)) / delta_x

# # Account for periodicity by wrapping the last point to the first point
# numerical_derivative[-1] = (f(x[0] + delta_x) - f(x[-1])) / delta_x

# # Compute the true derivative
# true_derivative = f_prime(x)

# # Plot the results
# plt.plot(x, numerical_derivative, label='Numerical Derivative')
# plt.plot(x, true_derivative, label='True Derivative')
# plt.xlabel('x')
# plt.ylabel('Derivative')
# plt.legend()
# plt.title('Numerical vs. True Derivative of f(x) = sin(x)')
# plt.grid(True)
# plt.show()



#b)

# Compute the numerical derivatives using the given schemes
coefficients = {
    'O(Delta_x)': np.array([0, 0, 0, -1, 1, 0, 0]),
    'O(Delta_x^2)': np.array([0, 0, -0.5, 0, 0.5, 0, 0]),
    'O(Delta_x^4)': np.array([0, 1 / 12, -2 / 3, 0, 2 / 3, -1 / 12, 0]),
    'O(Delta_x^6)': np.array([-1 / 60, 3 / 20, -3 / 4, 0, 3 / 4, -3 / 20, 1 / 60])
}

numerical_derivatives = {}
for scheme, coeffs in coefficients.items():
    # Initialize an array to store the shifted values
    shifted_values = np.zeros_like(x)

    # Apply the coefficients to the function values using a loop
    for i in range(len(coeffs)):
        shifted_values += coeffs[i] * np.roll(f(x), -i)

    # Calculate the numerical derivative
    numerical_derivative = shifted_values / delta_x

    numerical_derivatives[scheme] = numerical_derivative

# Compute the true derivative
true_derivative = f_prime(x)
