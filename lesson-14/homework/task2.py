import numpy as np

def power_func(base, exp):
    return base ** exp

vectorized_power = np.vectorize(power_func)
bases = np.array([2, 3, 4, 5])
exponents = np.array([1, 2, 3, 4])
results = vectorized_power(bases, exponents)

print(results)
