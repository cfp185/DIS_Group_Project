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
delta_talpha = 0.001
delta_tbeta = 1.0
delta_tgamma = 0.25

# Solving for alpha using Runge-Kutta method
t_rkalpha, f_rkalpha = runge_kutta(f0, t0, t_end, delta_talpha)

# Solving for beta using Runge-Kutta method
t_rkbeta, f_rkbeta = runge_kutta(f0, t0, t_end, delta_tbeta)

# Solving for alpha using Euler method
t_euleralpha, f_euleralpha = euler(f0, t0, t_end, delta_talpha)

# Solving for gamma using Euler method
t_eulergamma, f_eulergamma = euler(f0, t0, t_end, delta_tgamma)

# Plotting the results for alpha
fig_alpha, ax_alpha = plt.subplots()
ax_alpha.plot(t_rkalpha, f_rkalpha, label="Runge-Kutta alpha-value")
ax_alpha.plot(t_euleralpha, f_euleralpha, '--', label="Euler alpha-value")

ax_alpha.set_xlabel('t')
ax_alpha.set_ylabel('f(t)')
ax_alpha.legend()
ax_alpha.grid(True)
plt.show()

# Check the difference at the end of the interval
difference = np.abs(f_rkalpha[-1] - f_euleralpha[-1])

# Plotting the results for beta
fig_beta, ax_beta = plt.subplots()
ax_beta.plot(t_rkalpha, f_rkalpha, label="Runge-Kutta alpha-value")
ax_beta.plot(t_rkbeta, f_rkbeta, '--', label="Runge-Kutta beta-value")

ax_beta.set_xlabel('t')
ax_beta.set_ylabel('f(t)')
ax_beta.legend()
ax_beta.grid(True)
plt.show()

# Plotting the results for gamma
fig_gamma, ax_gamma = plt.subplots()
ax_gamma.plot(t_euleralpha, f_euleralpha, label="euler beta-value")
ax_gamma.plot(t_eulergamma, f_eulergamma, label="euler gamma-value")

ax_gamma.set_xlabel('t')
ax_gamma.set_ylabel('f(t)')
ax_gamma.legend()
ax_gamma.grid(True)
plt.show()

