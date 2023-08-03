import numpy as np
import matplotlib.pyplot as plt

def f_prime(t, f):
    return 1 + np.sin(t) * f

def runge_kutta(f0, t0, t_end, delta_t):
    t_values = np.arange(t0, t_end + delta_t, delta_t)
    f_values = [f0]
    
    for t in t_values[:-1]:
        k1 = f_prime(t, f_values[-1])
        k2 = f_prime(t + 0.5 * delta_t, f_values[-1] + 0.5 * k1 * delta_t)
        k3 = f_prime(t + 0.5 * delta_t, f_values[-1] + 0.5 * k2 * delta_t)
        k4 = f_prime(t + delta_t, f_values[-1] + k3 * delta_t)
        
        f_next = f_values[-1] + (delta_t / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)
        f_values.append(f_next)
    
    return t_values, np.array(f_values)

def euler(f0, t0, t_end, delta_t):
    t_values = np.arange(t0, t_end + delta_t, delta_t)
    f_values = [f0]
    
    for t in t_values[:-1]:
        f_next = f_values[-1] + delta_t * f_prime(t, f_values[-1])
        f_values.append(f_next)
    
    return t_values, np.array(f_values)

# Initial conditions
f0 = 0
t0 = 0
t_end = 15
delta_t = 0.001

# Solving using Runge-Kutta method
t_rk, f_rk = runge_kutta(f0, t0, t_end, delta_t)

# Solving using Euler method
t_euler, f_euler = euler(f0, t0, t_end, delta_t)

# Plotting the results
plt.plot(t_rk, f_rk, label="Runge-Kutta")
plt.plot(t_euler, f_euler, label="Euler")
plt.xlabel('t')
plt.ylabel('f(t)')
plt.legend()
plt.grid(True)
plt.show()
