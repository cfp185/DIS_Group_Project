import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the coordinates of the points A, B, C, and D
A = (-1, -1, -1)
B = (1, 1, -1)
C = (-1, 1, 1)
D = (1, -1, 1)

# Extract coordinates for plotting
x = [A[0], B[0], C[0], D[0], A[0]]
y = [A[1], B[1], C[1], D[1], A[1]]
z = [A[2], B[2], C[2], D[2], A[2]]

# Create a 3D plot
fig = plt.figure()
ax = plt.figure().add_subplot(projection='3d')

# Plot the ropes
ax.plot(x, y, z)

# Set labels for axes
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Set title
ax.set_title('Square Sun Sail Ropes in 3D')

plt.show()


