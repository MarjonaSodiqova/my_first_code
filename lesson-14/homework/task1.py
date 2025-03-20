import numpy as np

def f_to_c(f):
    return (f - 32) * 5 / 9

vectorized_f_to_c = np.vectorize(f_to_c)
temperatures_f = np.array([32, 68, 100, 212, 77])
temperatures_c = vectorized_f_to_c(temperatures_f)

print(temperatures_c)
