import numpy as np

vector_a = np.array([1, 2, 3, 4, 5])
print(f"vector_a = {vector_a}")
print(f'vector_a^2 = {vector_a**2}')

matrix_a = np.array([(1, 2), (3, 4)])
print(f'matrix_a = \n{matrix_a}')

zeros_b = np.zeros((2, 2))
print(f'zeros_b = \n{zeros_b}')

ones_c = np.ones((2, 2))
print(f'ones_c = \n{ones_c}')

total = matrix_a + zeros_b + ones_c
print(f'total = \n{total}')
