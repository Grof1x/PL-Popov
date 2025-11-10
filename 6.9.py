import random
# Первая задача
def task1():
    n = int(input("Введите количество элементов массива: "))
    array = []
    # Ввод массива вещественных чисел
    for i in range(n):
        element = float(input(f"Введите {i + 1}-й элемент массива: "))
        array.append(element)
    # Нахождение минимального по модулю элемента
    min_abs_element = min(array, key=abs)
    # Массив в обратном порядке
    reversed_array = array[::-1]
    print("\nМинимальный по модулю элемент:", min_abs_element)
    print("Исходный массив в обратном порядке:", reversed_array)
# Вторая задача
def task2():
    size = 10
    a = [random.uniform(-100, 100) for _ in range(size)]
    b = [random.uniform(-100, 100) for _ in range(size)]
    # Исходные массивы
    print("\nИсходный массив A:", a)
    print("Исходный массив B:", b)
    # Меняем местами содержимое массивов
    a[:], b[:] = b[:], a[:]
    # Преобразованные массивы
    print("\nПреобразованный массив A:", a)
    print("Преобразованный массив B:", b)
# Выполнение задач
task1()
task2()