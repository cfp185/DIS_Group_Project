import numpy as np
import matplotlib.pyplot as plt

# Initial conditions
R = 0
D = 50
U = 0
total_steps = 500000

# Lists to store data for plotting
time_list = []
R_list = []
D_list = []
U_list = []

for step in range(total_steps):
    # Calculate rates of all events
    rate_D_to_U = 0.1 * D
    rate_R_to_U = 0.1 * R
    rate_U_to_D = 0.05 * U
    rate_U_to_R = 0.05 * U
    rate_DR = 0.01 * D * R
    rate_UR = 0.01 * U * R
    rate_RD = 0.01 * R * D
    rate_UD = 0.01 * U * D
    total_rate = (
        rate_D_to_U + rate_R_to_U + rate_U_to_D + rate_U_to_R +
        rate_DR + rate_UR + rate_RD + rate_UD
    )
    
    # Append data to lists
    time_list.append(step)
    R_list.append(R)
    D_list.append(D)
    U_list.append(U)
    
    # Generate random numbers
    r1 = np.random.uniform(0, 1)
    r2 = np.random.uniform(0, 1)
    
    # Calculate time until next event
    time_until_next_event = -np.log(r1) / total_rate
    
    # Determine which event occurs
    if r2 * total_rate < rate_D_to_U:
        D -= 1
        U += 1
    elif r2 * total_rate < rate_D_to_U + rate_R_to_U:
        R -= 1
        U += 1
    elif r2 * total_rate < rate_D_to_U + rate_R_to_U + rate_U_to_D:
        U -= 1
        D += 1
    elif r2 * total_rate < rate_D_to_U + rate_R_to_U + rate_U_to_D + rate_U_to_R:
        U -= 1
        R += 1
    elif r2 * total_rate < rate_D_to_U + rate_R_to_U + rate_U_to_D + rate_U_to_R + rate_DR:
        D -= 1
        U += 1
    elif r2 * total_rate < rate_D_to_U + rate_R_to_U + rate_U_to_D + rate_U_to_R + rate_DR + rate_UR:
        U -= 1
        R += 1
    elif r2 * total_rate < rate_D_to_U + rate_R_to_U + rate_U_to_D + rate_U_to_R + rate_DR + rate_UR + rate_RD:
        R -= 1
        U += 1
    else:
        U -= 1
        D += 1

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(time_list, R_list, label='Republicans')
plt.plot(time_list, D_list, label='Democrats')
plt.plot(time_list, U_list, label='Undecided')
plt.xlabel('Time')
plt.ylabel('Population Count')
plt.title('Political Affiliation Simulation (with Undecided)')
plt.legend()
plt.show()

# Plotting R and D
plt.figure(figsize=(10, 6))
plt.plot(time_list, R_list, label='Republicans')
plt.plot(time_list, D_list, label='Democrats')
plt.xlabel('Time')
plt.ylabel('Population Count')
plt.title('Political Affiliation Simulation (with Undecided)')
plt.legend()
plt.show()
