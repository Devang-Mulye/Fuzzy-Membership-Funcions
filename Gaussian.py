import numpy as np
import matplotlib.pyplot as plt

def gaussian_mf(x, mean, sigma):
    return np.exp(-0.5 * ((x - mean) / sigma) ** 2)

# Define the range of x values
x = np.linspace(0, 10, 100)

# Gaussian membership function parameters
mean_gaussian = 5
sigma_gaussian = 2

# Calculate membership degrees
gaussian_degrees = gaussian_mf(x, mean_gaussian, sigma_gaussian)

# Plot the membership function
plt.plot(x, gaussian_degrees, label='Gaussian')
plt.title('Fuzzy Membership Function (Gaussian)')
plt.xlabel('x')
plt.ylabel('Membership Degree')
plt.legend()
plt.grid()
plt.show()
