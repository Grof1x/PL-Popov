import numpy as np

# Задача 1: Нахождение количества элементов, кратных k, и максимального среди них
def task1(matrix, k):
    divisible_elements = matrix[(matrix % k == 0)]
    if len(divisible_elements) == 0:
        print("Нет элементов, кратных k.")
        return None, None
    count = len(divisible_elements)
    max_element = np.max(divisible_elements)
    return count, max_element

# Задача 2: Нахождение наибольшего элемента по модулю и создание новой матрицы
def task2(matrix):
    abs_matrix = np.abs(matrix)
    max_value = np.max(abs_matrix)
    index = np.unravel_index(np.argmax(abs_matrix), matrix.shape)
    new_matrix = np.delete(np.delete(matrix, index[0], axis=0), index[1], axis=1)
    return max_value, new_matrix

# Главная программа
if __name__ == "__main__":
    # Чтение размера матрицы
    size = int(input("Введите порядок квадратной матрицы: "))
    matrix = np.array([list(map(int, input().split())) for _ in range(size)])
    # Чтение параметра k для первой задачи
    k = int(input("Введите значение k: "))

    # Решение первой задачи
    count, max_element = task1(matrix, k)
    if count is not None:
        print(f"Кратных k элементов: {count}, Наибольший из них: {max_element}")
    # Решение второй задачи
    max_value, new_matrix = task2(matrix)
    print(f"Наибольший элемент по модулю: {max_value}\nНовая матрица:\n{new_matrix}")