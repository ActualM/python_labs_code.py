import numpy as np

def matrix():
    matrix = np.random.rand(5, 5)


    min_value = np.min(matrix)
    max_value = np.max(matrix)

    return matrix, min_value, max_value


matrix, min_val, max_val = matrix()

print("Сгенерированная матрица:")
print(matrix)

print("\nМинимальное значение:", min_val)
print("Максимальное значение:", max_val)
