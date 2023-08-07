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

# Calculates the first derivative of f(x)
def first_derivative(x, a, delta_x):
    if x < 0:
        return (f(x, a) - f(x - delta_x, a)) / delta_x
    else:
        return (f(x + delta_x, a) - f(x, a)) / delta_x

# Calculates the second derivative of f(x)
def second_derivative(x, a, delta_x):
    if x < 0:
        return (np.exp(-delta_x) - 2*np.exp(-x) + np.exp(delta_x) - a*delta_x) / (delta_x**2)
    else:
        return 2

# Define parameters
delta_x = 0.01

# Test values
x_values = np.array([-1.5, -0.5, -0.2, 0, 0.2, 0.5, 1.5])

# Calculate the first derivatives using the finite difference scheme
for a in [0, 1, 2]:
    first_derivatives = [first_derivative(x, a, delta_x) for x in x_values]

# Calculate second derivatives using the central finite difference scheme
for a in [0, 1, 2]:
    second_derivatives = [second_derivative(x, a, delta_x) for x in x_values]

# Calculate the analytical derivatives
for a in [0, 1, 2]:
    analytical_derivatives = [fm(x, a) for x in x_values]

# Print the results and compare (subquestion d))
print("\nSubquestion d)\n")
for i, x in enumerate(x_values):
    print(f"For x = {x:.2f}:")
    print(f"Analytical f'(x) = {analytical_derivatives[i]:.4f}")
    print(f"Finite Difference f''(x) ≈ {second_derivatives[i]:.4f}")
    print(f"Difference: {abs(analytical_derivatives[i] - second_derivatives[i]):.4f}\n")

print("------------------------\n")
print("Subquestion e)\n")

# Print the results of subquestion e)
for i, x in enumerate(x_values):
    print(f"For x = {x:.2f}, f'(x) ≈ {first_derivatives[i]:.4f}\n")

def first_derivative_approx_one_sided(x, a, delta_x):
    if x < 0:
        return (f(x, a) - f(x - delta_x, a)) / delta_x
    else:
        return (f(x + delta_x, a) - f(x, a)) / delta_x

def first_derivative_approx_central(x, a, delta_x):
    return (f(x + delta_x, a) - f(x - delta_x, a)) / (2 * delta_x)


# Calculate the first derivatives using both schemes
first_derivatives_one_sided = [first_derivative_approx_one_sided(x, a, delta_x) for x in x_values]
first_derivatives_central = [first_derivative_approx_central(x, a, delta_x) for x in x_values]

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(x_values, first_derivatives_one_sided, label='One-Sided Scheme')
plt.plot(x_values, first_derivatives_central, '--', label='Central Scheme')
plt.axhline(y=0, color='black', linestyle='--', linewidth=0.8)
plt.xlabel('x')
plt.ylabel("f'(x)")
plt.title("Comparison of Finite Difference Schemes for f'(x)")
plt.legend()
plt.grid(True)
plt.show()

