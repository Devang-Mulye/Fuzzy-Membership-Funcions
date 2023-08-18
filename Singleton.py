import numpy as np
import matplotlib.pyplot as plt

def singleton_mf(x, center):
    return np.where(x == center, 1, 0)

# Define the range of x values
x = np.linspace(0, 10, 100)

# Singleton membership function center
center_singleton = 5

# Calculate membership degrees
singleton_degrees = singleton_mf(x, center_singleton)

# Plot the membership function
plt.plot(x, singleton_degrees, label='Singleton')
plt.title('Fuzzy Membership Function (Singleton)')
plt.xlabel('x')
plt.ylabel('Membership Degree')
plt.legend()
plt.grid()
plt.show()
