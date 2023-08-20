import numpy as np

def calculate_hamiltonian(S):
    N = S.shape[0]  # Assuming S is an N x N matrix
    H = 0
    
    for i in range(N):
        for j in range(N):
            # Calculate contributions from neighboring spins (periodic boundary conditions)
            left_neighbor = S[i, (j - 1) % N]
            right_neighbor = S[i, (j + 1) % N]
            top_neighbor = S[(i - 1) % N, j]
            bottom_neighbor = S[(i + 1) % N, j]
            
            H -= S[i, j] * (left_neighbor + right_neighbor + top_neighbor + bottom_neighbor)
    
    return H

def calculate_magnetisation(S):
    total_spins = S.size
    magnetisation = np.sum(S) / total_spins
    return magnetisation

def calculate_energy_change(S, i):
    N = S.shape[0]  # Assuming S is an N x N matrix
    row, col = divmod(i, N)  # Convert 1D index to 2D coordinates
    
    # Calculate current energy contribution of the spin at location i
    current_energy = 2 * S[row, col] * (
        S[row, (col - 1) % N] + S[row, (col + 1) % N] +
        S[(row - 1) % N, col] + S[(row + 1) % N, col]
    )
    
    # Flip the spin at location i
    S[row, col] *= -1
    
    # Calculate new energy contribution of the flipped spin at location i
    new_energy = 2 * S[row, col] * (
        S[row, (col - 1) % N] + S[row, (col + 1) % N] +
        S[(row - 1) % N, col] + S[(row + 1) % N, col]
    )
    
    # Calculate the change in energy
    energy_change = new_energy - current_energy
    
    return energy_change

def spin_flip(S, i, temperature):
    N = S.shape[0]  # Assuming S is an N x N matrix
    row, col = divmod(i, N)  # Convert 1D index to 2D coordinates

    delta_E = calculate_energy_change(S, i)
    alpha = min(1, np.exp(-delta_E / temperature))
    
    if np.random.rand() < alpha:
        S[row, col] *= -1  # Accept the flip
    
    return S

# Example usage
N = 3
S = np.array([[1, -1, 1],
              [-1, 1, -1],
              [1, -1, 1]])
i = 4  # Flipping the spin at (1, 1)
temperature = 1.0
energy = calculate_hamiltonian(S)
print("Total Energy:", energy)
magnetisation = calculate_magnetisation(S)
print("Magnetisation:", magnetisation)
energy_change = calculate_energy_change(S, i)
print("Energy Change:", energy_change)
new_S = spin_flip(S.copy(), i, temperature)
print("Updated Spin Configuration:\n", new_S)



