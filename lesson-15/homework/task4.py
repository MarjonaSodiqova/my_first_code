import matplotlib.pyplot as plt
import numpy as np

np.random.seed(42)
x = np.random.uniform(0, 10, 100)
y = np.random.uniform(0, 10, 100)
colors = np.random.rand(100)
sizes = np.random.randint(20, 100, 100)

plt.figure(figsize=(8, 6))
plt.scatter(x, y, c=colors, s=sizes, marker='s', alpha=0.7, cmap='viridis')
plt.colorbar()

plt.title('Random Scatter Plot')
plt.xlabel('X values')
plt.ylabel('Y values')
plt.grid(True)

plt.xlim(0, 10)
plt.ylim(0, 10)

plt.show()