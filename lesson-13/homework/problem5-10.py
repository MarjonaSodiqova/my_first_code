import numpy as np

array_10x10 = np.random.random((10, 10))
min_value, max_value = array_10x10.min(), array_10x10.max()

vector_30 = np.random.random(30)
mean_value = vector_30.mean()

matrix_5x5 = np.random.random((5, 5))
normalized_matrix = (matrix_5x5 - matrix_5x5.min()) / (matrix_5x5.max() - matrix_5x5.min())

matrix_5x3 = np.random.random((5, 3))
matrix_3x2 = np.random.random((3, 2))
product_5x2 = np.dot(matrix_5x3, matrix_3x2)

matrix_3x3_A = np.random.random((3, 3))
matrix_3x3_B = np.random.random((3, 3))
dot_product = np.dot(matrix_3x3_A, matrix_3x3_B)

matrix_4x4 = np.random.random((4, 4))
transpose_matrix = matrix_4x4.T

print(min_value, max_value)
print(mean_value)
print(normalized_matrix)
print(product_5x2)
print(dot_product)
print(transpose_matrix)
