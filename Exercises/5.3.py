import numpy as np
import matplotlib.pyplot as plt

# Initial conditions
R = 25
D = 25
total_steps = 500000

# Lists to store data for plotting
time_list = []
R_list = []
D_list = []

for step in range(total_steps):
    # Calculate rates of all events
    rate_D_to_R = 0.1 * D
    rate_R_to_D = 0.1 * R
    rate_DR = 0.01 * D * R
    rate_RD = 0.01 * D * R
    total_rate = rate_D_to_R + rate_R_to_D + rate_DR + rate_RD

    # Append data to lists
    time_list.append(step)
    R_list.append(R)
    D_list.append(D)
    
    # Generate random numbers
    r1 = np.random.uniform(0, 1)
    r2 = np.random.uniform(0, 1)
    
    # Calculate time until next event
    time_until_next_event = -np.log(r1) / total_rate
    
    # Determine which event occurs
    if r2 * total_rate < rate_D_to_R:
        D -= 1
        R += 1
    elif r2 * total_rate < rate_D_to_R + rate_R_to_D:
        R -= 1
        D += 1
    elif r2 * total_rate < rate_D_to_R + rate_R_to_D + rate_DR:
        D -= 1
        R += 1
    else:
        R -= 1
        D += 1

# After the simulation, print the final counts
print("Final Republican count:", R)
print("Final Democratic count:", D)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(time_list, R_list, label='Republicans')
plt.plot(time_list, D_list, label='Democrats')
plt.xlabel('Time')
plt.ylabel('Population Count')
plt.title('Political Loyalties Simulation')
plt.legend()
plt.show()

