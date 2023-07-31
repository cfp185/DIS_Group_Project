import numpy as np
import matplotlib.pyplot as plt
@np.vectorize

def f(x,z):
    return x * np.exp(x) - z        # Defining f(x).

def Df(x):
    return np.exp(x) * (x + 1)      # Defining F(x).

# With  a for-loop:
#def my_lambertw(z):
#    x0 = 0.0
#    xn = x0
#    for _ in range (100):           # a) Implement my_lambertw.
#        fxn = f(xn, z)              #    f(x) 
#        Dfxn = Df(xn)               #    F(x)
#        xn = xn - (fxn / Dfxn)      #    Newton's method (1.3)
#    return xn

# With a while-statement:
def my_lambertw(z):
    x0 = 0.0
    xn = x0

    while True:  # Use a while loop with a termination condition
        fxn = f(xn, z)
        Dfxn = Df(xn)
        xn_new = xn - (fxn / Dfxn)
        
        if abs(xn_new - xn) < 1e-5:  # Check if the change in xn is smaller than the tolerance
            break
        
        xn = xn_new

    return xn

my_lambertw_vectorized = np.vectorize(my_lambertw)  # Vectorize my_lambertw() so it works on arrays.

# Test:
z_values = np.array([1.0, 2.0, 3.0])
result = my_lambertw_vectorized(z_values)
print(result)

# Plot the graph of f(x) vs. F(x) to see the converge.
x_vals = np.linspace(0, 5, 1000)
plt.plot(x_vals, f(x_vals, z_values[0]), label='f(x)')
plt.plot(x_vals, Df(x_vals), label='F(x)')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Graph of f(x) and F(x)')
plt.grid(True)
plt.show()
