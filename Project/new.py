import copy # Used for creating non-linked copies of states
import numpy as np # General matrix compute platform
import matplotlib.pyplot as plt # Used for plotting and analysis
from math import ceil # Helpful for rounding off floats to conservative ceilings
from itertools import combinations # Produces the sets of combinations for pairs

class NBody:
    def __init__(self, Xi=None, masses=None, G=6.67408e-11):

      # Init State and Masses
      self.Xi = Xi # Set the initial state matrix
      self.masses = masses # Set the body masses array

      # Set gravitational constant
      # This really shouldn't change but it's fun for some special cases
      self.G = G

      # History is where we'll store the results of the simulation
      # We will not define a history without a sim so it's none for now
      self.history = None
      self.energies = None

    def get_energy(self, X):
      """
      Inputs:
      - X: The current state to determine the energy for
      - masses: Array of masses corresponding to the bodies
      - G: Gravitational constant, needed for potential energy
      Returns:
      - KE: Total kinetic energy of the system in joules
      - PE: Total potential energy of the system in joules
      """

      # Useful Variables
      N, D = X.shape # Get the number of bodies, and dimensionality
      D = D // 2 # Get the number of dimensions, are we 2d or 3d?
      R = X[:, :D] # Submatrix with all positions
      V = X[:, D:] # Submatrix with all velocities

      # Determine Kinetic Energy
      # 1/2 * mass * v ^ 2
      KE = 0
      for i in range(N):
          KE += 0.5 * self.masses[i] * np.linalg.norm(V[i]) ** 2

      # Determine Potential Energy
      # (-G * m_i * m_j) / r_ij
      PE = 0
      for body_i, body_j in self.pairs:
          r = np.linalg.norm(R[body_j] - R[body_i]) # Distance between bodies
          PE -= self.masses[body_i] * self.masses[body_j] / r
      PE *= self.G # Multiplying is expensive so I only do one at the end

      return KE, PE

    def get_state_deriv(self, X):
      """
      Inputs:
      - X: The current state to determine the state derivative for
      Returns:
      - Xdot: The corresponding state derivative for the input state
      """

      # Useful Variables
      N, D = X.shape # Get the number of bodies, and dimensionality
      D = D // 2 # Get the number of dimensions, are we 2d or 3d?
      R = X[:, :D] # Submatrix with all positions
      V = X[:, D:] # Submatrix with all velocities

      # Build Placeholder Structure
      Xdot = np.zeros_like(X) # Xdot is the same size as X
      Xdot[:, :D] = V # Fill in velocities from state

      # Iterate Over Pairs and Fill Out Acceleration
      # self.pairs gets defined when we start a sim
      # body_i, body_j are the indices of the bodies
      for body_i, body_j in self.pairs:

          # Get vector from body_i => body_j and its magnitude
          r1, r2 = R[body_i], R[body_j] # Positions of body_i and body_j
          r_vec = r2 - r1 # Vector from body_i => body_j
          r = np.linalg.norm(r_vec) # Distance from body_i => body_j

          # Find Force from body_i => body_j
          F = self.G * self.masses[body_i] * self.masses[body_j] * r_vec / r**3
          a1 =  F / self.masses[body_i] # Compute acceleration for body_i
          a2 = -F / self.masses[body_j] # Compute acceleration for body_j

          # Apply acceleration to body_i and body_j
          Xdot[body_i, D:] += a1
          Xdot[body_j, D:] += a2

      return Xdot

    def rk4(self, X, dt, evaluate):
        """
        Inputs:
        - X: Current state of system
        - dt: Integration Timestep
        - evaluate: Function that will return the derivative for the state
        Returns:
        - X: Updated state one timestep later
        """
        # Calculate Terms
        k1 = evaluate(X)
        k2 = evaluate(X + 0.5*k1*dt)
        k3 = evaluate(X + 0.5*k2*dt)
        k4 = evaluate(X + k3*dt)

        # Update X
        X_prime = (1/6.)*(k1 + 2*k2 + 2*k3 + k4)
        return X + X_prime * dt

    def run_simulation(self, T, dt):
      """
      Inputs:
      - T: Total runtime of simulation
      - dt: Timestep for integration
      Returns:
      - history: Matrix of the history of states
      """

      # Check to ensure initial conditions and masses have been set
      assert self.Xi is not None
      assert self.masses is not None

      # Setup Sim Params
      iters = ceil(T / dt) # Number of simulation iterations

      # Init History
      N, D = self.Xi.shape
      self.history = np.zeros((iters+1, N, D))
      self.history[0] = self.Xi # First history is our initial conditions

      # Determine Force Pair Indexes
      self.pairs = list(combinations(range(N), 2))

      # Init Energies
      self.energies = np.zeros((iters+1, 3))
      KE, PE = self.get_energy(self.Xi)
      self.energies[0] = np.array([KE, PE, KE+PE])

      # Run Simulation Iterations
      X = copy.deepcopy(self.Xi) # Copy as to not modify Xi
      for i in range(iters):
          X = self.rk4(X, dt, self.get_state_deriv) # Get new state
          self.history[i+1] = X # Store new state
          KE, PE = self.get_energy(X) # Get new state's energy
          self.energies[i+1] = np.array([KE, PE, KE+PE]) # Store energy
      return self.history

    def earth_stable_orbit(r):
      """
      Inputs:
      - r: Altitude of orbit above earth's surface in meters
      Returns:
      - v: Velocity in m/s to sustain a stable circular orbit
      """
      G = 6.67408e-11
      massE = 5.974e24 # Mass in kg
      rE = 6.3781e6 # Radius in m
      return np.sqrt(G * massE / (r + rE))

      massE, rE = 5.974e24, 6.3781e6 # Earth properties
      r = 760e3 # Satellite Orbit Altitude

      # Setting up initial state
      X = np.array([[0, 0, 0, 0],
                    [rE + r, 0, 0, earth_stable_orbit(r)]])
      masses = [massE, 250] # Earth and Small Sat

      TwoBody = NBody(Xi=X, masses=masses) # Initialize sim instance
      T, dt =  500 * 60, 1 # Simulation for 500 minutes at a 1 second timestep
      history = TwoBody.run_simulation(T, dt) # Run the sim and get history

    def plot_orbit(self):
        # Positions for Plotting Earth Circle
        theta = np.linspace(0, 2 * np.pi, 150)
        rE = 6.3781e6 # Radius in m
        x = rE * np.cos(theta)
        y = rE * np.sin(theta)

        # Plot Earth Surface
        plt.plot(x, y, label="Earth Surface", linestyle='dashed')

        # Plot the satellite orbit
        x = self.history[:, 1, 0] # [all sim steps, body 1, first variable in state]
        y = self.history[:, 1, 1] # [all sim steps, body 1, second variable in state]
        plt.plot(x, y, label="Low Earth Orbit", linewidth=1)
        plt.axis('equal')
        plt.legend(loc='upper right')
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.show()

def earth_stable_orbit(r):
    """
    Inputs:
    - r: Altitude of orbit above earth's surface in meters
    Returns:
    - v: Velocity in m/s to sustain a stable circular orbit
    """
    G = 6.67408e-11
    massE = 5.974e24 # Mass in kg
    rE = 6.3781e6 # Radius in m
    return np.sqrt(G * massE / (r + rE))

# Earth properties
massE, rE = 5.974e24, 6.3781e6
r = 760e3 # Satellite Orbit Altitude

# Setting up initial state
X = np.array([[0, 0, 0, 0],
              [rE + r, 0, 0, earth_stable_orbit(r)]])
masses = [massE, 250] # Earth and Small Sat

# Initialize sim instance
TwoBody = NBody(Xi=X, masses=masses)
T, dt =  500 * 60, 1 # Simulation for 500 minutes at a 1 second timestep

# Run the simulation
TwoBody.run_simulation(T, dt)

# Plot the results
TwoBody.plot_orbit()





names = ["Newton", "Red Apple", "Green Apple", "Yellow Apple"]
X = np.array([
    [1.81899E+8, 9.83630E+8, -1.58778E+8, -1.12474E+1, 7.54876E+0, 2.68723E-1],
    [-5.67576E+10, -2.73592E+10, 2.89173E+9, 1.16497E+4, -4.14793E+4, -4.45952E+3],
    [4.28480E+10, 1.00073E+11, -1.11872E+09, -3.22930E+04, 1.36960E+04, 2.05091E+03],
    [-1.43778E+11, -4.00067E+10, -1.38875E+07, 7.65151E+03, -2.87514E+04, 2.08354E+00]
])
masses = np.array([1.98854E+30, 3.30200E+23, 4.86850E+24, 5.97219E+24])

# Time Step is an hour!
SolarSystem = NBody(Xi=X, masses=masses)
T, dt = 2 * 365 * 24 * 60**2, 10 ** 2 # 2 Years, 1 hour step
history = SolarSystem.run_simulation(T, dt)

fig = plt.figure(figsize=(7,7))
ax = fig.add_subplot(111,projection='3d')
colors = ["gray", "red", "green", "yellow"]
for i in range(X.shape[0]):
    c = colors[i]
    x = history[:, i, 0]
    y = history[:, i, 1]
    z = history[:, i, 2]
    ax.plot3D(x, y, z, color='gray', label=names[i], linewidth=0.2,
             markevery=[0], marker='o', ms=10, mfc=c, mec="black", mew=0.5)

ax.set(xlabel='X')
ax.set(ylabel='Y')
ax.set(zlabel='Z')

ax.grid(False)  # Turn off grid
ax.xaxis.pane.fill = False  # No color on face x axis
ax.yaxis.pane.fill = False  # No color on face y axis
ax.zaxis.pane.fill = False  # No color on face z axis

ax.legend(markerscale=0.375)
plt.show()