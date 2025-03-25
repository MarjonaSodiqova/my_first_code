import matplotlib.pyplot as plt
import numpy as np
import math

x = np.linspace(-2, 2, 100)
x_positive = np.linspace(0, 2, 100)

plt.figure(figsize=(10, 8))


plt.subplot(2, 2, 1)
plt.plot(x, x**3, color='blue')
plt.title('f(x) = x³')
plt.xlabel('x')
plt.ylabel('f(x)')
 
plt.subplot(2, 2, 2)
plt.plot(x, np.sin(x), color='green')
plt.title('f(x) = sin(x)')
plt.xlabel('x')
plt.ylabel('f(x)')

plt.subplot(2, 2, 3)
plt.plot(x, np.exp(x), color='red')
plt.title('f(x) = e^x')
plt.xlabel('x')
plt.ylabel('f(x)')

plt.subplot(2, 2, 4)
plt.plot(x_positive, np.log(x_positive + 1), color='purple')
plt.title('f(x) = log(x+1)')
plt.xlabel('x')
plt.ylabel('f(x)')

plt.tight_layout()
plt.show()