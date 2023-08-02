import numpy as np
import matplotlib.pyplot as plt

order1 = 1
coefficients = np.array([0, 0, 0, -1, 1, 0, 0])  # Coefficients for first-order accuracy
numerical_derivative = np.sum(coefficients * np.roll(f(x), -order2 // 1)) / delta_x

order2 = 2
coefficients = np.array([0, 0, -0.5, 0, 0.5, 0, 0])  # Coefficients for second-order accuracy
numerical_derivative = np.sum(coefficients * np.roll(f(x), -order2 // 2)) / delta_x

order4 = 4
coefficients = np.array([0, 1/12, -2/3, 0, 2/3, -1/12, 0])  # Coefficients for fourth-order accuracy
numerical_derivative = np.sum(coefficients * np.roll(f(x), -order2 // 4)) / delta_x

order6 = 6
coefficients = np.array([-1/60, 3/20, -3/4, 0, 3/4, -3/20, 1/60])  # Coefficients for sixth-order accuracy
numerical_derivative = np.sum(coefficients * np.roll(f(x), -order2 // 6)) / delta_x

