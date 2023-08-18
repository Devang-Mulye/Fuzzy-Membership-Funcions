import numpy as np
import matplotlib.pyplot as plt

def triangular_mf(x, a, b, c):
    return np.maximum(0, np.minimum.reduce([(x - a) / (b - a),
                                             (c - x) / (c - b)]))

# Define the range of x values
x = np.linspace(0, 10, 100)

# Triangular membership function parameters
a_tri = 2
b_tri = 5
c_tri = 8

# Calculate membership degrees
triangular_degrees = triangular_mf(x, a_tri, b_tri, c_tri)

# Plot the membership function
plt.plot(x, triangular_degrees, label='Triangular')
plt.title('Fuzzy Membership Function (Triangular)')
plt.xlabel('x')
plt.ylabel('Membership Degree')
plt.legend()
plt.grid()
plt.show()
