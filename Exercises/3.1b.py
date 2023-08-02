import numpy as np
import matplotlib.pyplot as plt

# Define parameters
alpha = 205
t0 = 0
tf = 100
dt = 0.01
x0 = 0

# Initialize variables
time_values = np.arange(t0, tf + dt, dt)                    # An array that stores the discrete time values
                                                            # from t0 to tf with a step size of dt.
numerical_solution_implicit = np.zeros_like(time_values, dtype=np.longdouble)    # An array that holds the numerical approximation
                                                            # of x(t) at each time step.
numerical_solution_implicit[0] = x0                         

# Implicit Euler method
for i in range(1, len(time_values)):
    current_time = time_values[i]                           # Current time at each iteration.
    previous_solution = numerical_solution_implicit[i - 1]  # The numerical solution at the
                                                            # previous time step.
    
    # Solve the implicit equation using the Newton-Raphson method
    def implicit_equation(x_next):
        # Calculate the value of x(t+dt) using the implicit Euler formula
        calculated_value = previous_solution + alpha * (np.sin(current_time + dt) - x_next) * dt
    
        # Calculate the difference between the calculated value and the unknown value (x_next)
        difference = x_next - calculated_value
    
        # Return the difference
        return difference
    
    # Use Newton-Raphson to find the solution for x_next
    x_next_guess = previous_solution    # Initialize x_next_guess to the previous numerical solution,
                                        # since it's a reasonable guess for the next value for x(t+dt)
    for _ in range(10):
        # Iteratively refines the guess using the Newton-Raphson method to find a value that
        # satisfies the implicit step for each time-step. This ensures an accurate numerical
        # approximation of the solution.
        x_next_guess -= implicit_equation(x_next_guess) / (1 + alpha * dt * np.cos(current_time + dt))
    
    numerical_solution_implicit[i] = x_next_guess

# Analytical solution
# Exact solution of ODE for the given parameter alpha, and the initial condition x(0)=0.
x_values_analytical = (alpha / (1 + alpha**2)) * (np.exp(-alpha * time_values) - np.cos(time_values) + alpha * np.sin(time_values))

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(time_values, numerical_solution_implicit, label='Implicit Euler')
plt.plot(time_values, x_values_analytical, label='Analytical Solution')
plt.xlabel('t')
plt.ylabel('x(t)')
plt.legend()
plt.title('Comparison of Implicit Euler Method with Analytical Solution (alpha = 205)')
plt.grid(True)
plt.show()




# COMMENT TO SELF: 
# ANGÅENDE OPGAVE 3.1c:
# DEN "FEJLER" NÅR ALPHA BLIVER STOR. FOR IMPLICIT EULER METHOD KAN DEN IKKE BLIVE MEGET HØJERE END 40????