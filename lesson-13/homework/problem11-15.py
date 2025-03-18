import numpy as np

matrix_3x3 = np.random.random((3, 3))
determinant = np.linalg.det(matrix_3x3)

A = np.random.random((3, 4))
B = np.random.random((4, 3))
matrix_product = np.dot(A, B)

matrix_3x3_rand = np.random.random((3, 3))
vector_3x1 = np.random.random((3, 1))
matrix_vector_product = np.dot(matrix_3x3_rand, vector_3x1)

A_system = np.random.random((3, 3))
b_system = np.random.random((3, 1))
solution_x = np.linalg.solve(A_system, b_system)

matrix_5x5 = np.random.random((5, 5))
row_sums = matrix_5x5.sum(axis=1)
column_sums = matrix_5x5.sum(axis=0)

print(determinant)
print(matrix_product)
print(matrix_vector_product)
print(solution_x)
print(row_sums)
print(column_sums)
