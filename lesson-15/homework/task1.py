import matplotlib.pyplot as plt
import numpy as np

# Task 1
x = np.linspace(-10, 10, 100)
y = x**2 - 4*x + 4
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Plot of f(x) = x² -4x +4')
plt.show()