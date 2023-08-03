import numpy as np
import matplotlib.pyplot as plt
import math

# f(x)
def f(x, a):
    if (x > 0):
        f_pos = x**2
        return f_pos                    # x > 0
    else:
        f_neg = math.e**(-x) + a
        return f_neg                    # x < 0

# f'(x)
def fm(x, a):
    if (x > 0):
        fm_pos = 2*x
        return fm_pos                   # x > 0
    else:
        fm_neg = -math.e**(-x) + a
        return fm_neg                   # x < 0

# Subquestion b) *{
# Generate separate linspace arrays for x < 0 and x > 0
N = 1000
x_neg = np.linspace(-1, 0, N)[1:] #remove the first element by indexing
x_pos = np.linspace(0, 1, N)[1:] #remove the first element by indexing
# Subquestion b) }*

# Generates a "normal" linspace
#x_neg = np.linspace(-5, 0)
#x_pos = np.linspace(0, 5)

# Define the coefficients for each scheme in the "Finite Difference Coefficients for the First Derivative" table
schemes = [
    {"coeffs": [0, 0, 0, -1, 1, 0, 0, 0], "shifts": [-3, -2, -1, 0, 1, 2, 3, 4]},  # First row in the table
    {"coeffs": [0, 0, -1/2, 0, 1/2, 0, 0, 0], "shifts": [-3, -2, -1, 0, 1, 2, 3, 4]},  # Second row in the table
    {"coeffs": [0, 1/12, -2/3, 0, 2/3, -1/12, 0, 0], "shifts": [-3, -2, -1, 0, 1, 2, 3, 4]},  # Third row in the table
    {"coeffs": [-1/60, 3/20, -3/4, 0, 3/4, -3/20, 1/60, 0], "shifts": [-3, -2, -1, 0, 1, 2, 3, 4]},  # Fourth row in the table
]

# Plotting the functions for a:
for a in [0, 1, 2]:
    plt.figure(figsize=(10, 5))
    plt.title(f"2.3 Discontinuities for a = {a}")
    plt.xlabel("x-axis")
    plt.ylabel("y-axis")

    # Plot for x < 0
    y_neg = [f(x, a) for x in x_neg]
    ym_neg = [fm(x, a) for x in x_neg]
    plt.plot(x_neg, y_neg, label='f(x) for x < 0')
    plt.plot(x_neg, ym_neg, label="f'(x) for x < 0")

    # Plot for x > 0
    y_pos = [f(x, a) for x in x_pos]
    ym_pos = [fm(x, a) for x in x_pos]
    plt.plot(x_pos, y_pos, label='f(x) for x > 0')
    plt.plot(x_pos, ym_pos, label="f'(x) for x > 0")

    plt.legend()
    plt.grid(True)
    plt.show()