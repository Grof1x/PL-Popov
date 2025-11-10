# Импортируем библиотеку numpy для удобства работы с матрицами
import numpy as np

# Задание 1: Поиск строк с максимальной и минимальной суммами элементов
def find_max_min_rows(matrix):
    row_sums = matrix.sum(axis=1)  # Суммируем элементы каждой строки
    max_row_idx = np.argmax(row_sums)  # Индекс строки с максимальным значением суммы
    min_row_idx = np.argmin(row_sums)  # Индекс строки с минимальным значением суммы
    print("Строка с наибольшей суммой:")
    print(matrix[max_row_idx])
    print("Сумма:", row_sums[max_row_idx])
    print("\nСтрока с наименьшей суммой:")
    print(matrix[min_row_idx])
    print("Сумма:", row_sums[min_row_idx])

# Задание 2: Преобразование матрицы и вывод нижней треугольной части
def transform_and_print_lower_triangle(matrix):
    transformed_matrix = np.where(matrix >= 0, 1, 0)  # Положительные заменяем на 1, остальные на 0
    lower_triangular = np.tril(transformed_matrix)  # Берём нижнюю треугольную часть
    print("\nНижняя треугольная матрица:")
    print(lower_triangular)

# Основная программа
if __name__ == "__main__":
    # Читаем размер матрицы
    rows = int(input("Введите количество строк матрицы: "))
    cols = int(input("Введите количество столбцов матрицы: "))
    # Создаем пустую матрицу и читаем её элементы
    matrix = np.zeros((rows, cols))
    print("Вводите элементы матрицы построчно:")
    for i in range(rows):
        row_data = list(map(int, input().split()))[:cols]
        matrix[i] = row_data

    # Выполняем первое задание
    find_max_min_rows(matrix)
    # Выполняем второе задание
    transform_and_print_lower_triangle(matrix)