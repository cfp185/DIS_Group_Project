import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Define the coordinates of the points A, B, C, and D
A = (-1, -1, -1)
B = (1, 1, -1)
C = (-1, 1, 1)
D = (1, -1, 1)

# Define the ropes as line segments
ropes = [
    [A, C],
    [A, D],
    [B, C],
    [B, D]
]

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the ropes as line segments
for rope in ropes:
    rope_x = [rope[0][0], rope[1][0]]
    rope_y = [rope[0][1], rope[1][1]]
    rope_z = [rope[0][2], rope[1][2]]
    ax.plot(rope_x, rope_y, rope_z, marker='o')

# Set labels for axes
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Set title
ax.set_title('Square Sun Sail Ropes in 3D')

plt.show()

