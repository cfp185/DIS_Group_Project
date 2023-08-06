import numpy as np
import matplotlib.pyplot as plt
import math

# f(x)
def f(x, a):
    if x > 0:
        f_pos = x**2
        return f_pos  # x > 0
    else:
        f_neg = math.e**(-x) + a
        return f_neg  # x < 0

# Subquestion b) *{
# Generate separate linspace arrays for x < 0 and x > 0
N = 1000
x_neg = np.linspace(-1, 0, N)[1:]  # remove the first element by indexing
x_pos = np.linspace(0, 1, N)[1:]  # remove the first element by indexing
delta_x = 1/N
# Subquestion b) }*

# Define the coefficients for each scheme in the "Finite Difference Coefficients for the Second Derivative" table
schemes = [
    {"coeffs": [0, 0, 0, 1, -2, 1, 0, 0], "shifts": [-3, -2, -1, 0, 1, 2, 3, 4]},  # First row in the table
    {"coeffs": [0, 0, 1/12, -2/3, 0, 2/3, -1/12, 0], "shifts": [-3, -2, -1, 0, 1, 2, 3, 4]},  # Second row in the table
    {"coeffs": [0, 1/90, -3/20, 3/2, -49/18, 3/2, -3/20, 1/90], "shifts": [-3, -2, -1, 0, 1, 2, 3, 4]},  # Third row in the table
    {"coeffs": [1/560, -8/315, 1/5, -8/5, 205/72, -8/5, 1/5, -8/315], "shifts": [-3, -2, -1, 0, 1, 2, 3, 4]},  # Fourth row in the table
]

# Central second-order finite difference scheme for numerical derivative (O(Δx^2))
def numerical_derivative_second_order(x, a, delta_x):
    result = 0
    for coeff, shift in zip(schemes[2]["coeffs"], schemes[2]["shifts"]):
        result += coeff * f(x + shift * delta_x, a)
    return result / (delta_x**2)

# Calculate and compare the numerical and analytical derivatives for each a value using the second-order scheme
for a in [0, 1, 2]:
    print(f"For a = {a}:")
    
    # Calculate the average absolute difference for x < 0
    abs_diff_neg = [abs(numerical_derivative_second_order(x, a, delta_x) - (2 * x if x > 0 else -math.e**(-x))) for x in x_neg]
    avg_abs_diff_neg = sum(abs_diff_neg) / len(abs_diff_neg)
    
    # Calculate the average absolute difference for x > 0
    abs_diff_pos = [abs(numerical_derivative_second_order(x, a, delta_x) - (2 * x if x > 0 else -math.e**(-x))) for x in x_pos]
    avg_abs_diff_pos = sum(abs_diff_pos) / len(abs_diff_pos)
    
    print(f"Avg. Abs. Diff. (x < 0): {avg_abs_diff_neg:.4f}")
    print(f"Avg. Abs. Diff. (x > 0): {avg_abs_diff_pos:.4f}")
    print("\n")
    
    print("\n")
