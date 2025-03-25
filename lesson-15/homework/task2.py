import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2*np.pi, 100)
y1 = np.sin(x)
y2 = np.cos(x)
plt.plot(x, y1, linestyle='-', color='blue', marker='o', label='sin(x)')
plt.plot(x, y2, linestyle='--', color='red', marker='s', label='cos(x)')
plt.xlabel('x')
plt.ylabel('Value')
plt.title('Sine and Cosine Functions')
plt.legend()
plt.show()