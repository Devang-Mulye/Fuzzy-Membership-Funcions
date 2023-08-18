import numpy as np
import matplotlib.pyplot as plt

def trapezoidal_mf(x, a, b, c, d):
    return np.maximum(0, np.minimum.reduce([(x - a) / (b - a),
                                             np.ones_like(x),
                                             (d - x) / (d - c)]))

# Define the range of x values
x = np.linspace(0, 10, 100)

# Trapezoidal membership function parameters
a_trap = 3
b_trap = 4
c_trap = 7
d_trap = 9

# Calculate membership degrees
trapezoidal_degrees = trapezoidal_mf(x, a_trap, b_trap, c_trap, d_trap)

# Plot the membership function
plt.plot(x, trapezoidal_degrees, label='Trapezoidal')
plt.title('Fuzzy Membership Function (Trapezoidal)')
plt.xlabel('x')
plt.ylabel('Membership Degree')
plt.legend()
plt.grid()
plt.show()
