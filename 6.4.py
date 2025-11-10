def find_max_and_index(arr):
    """Функция находит максимальный элемент массива и его порядковый номер."""
    if not arr:
        return None, None
    max_value = arr[0]
    index = 0
    for i in range(len(arr)):
        if arr[i] > max_value:
            max_value = arr[i]
            index = i
    return max_value, index
def extract_odd_numbers(arr):
    """Функция получает новый массив из нечётных чисел исходного,
       отсортированных в порядке убывания."""
    odd_numbers = [num for num in arr if num % 2 != 0]
    if len(odd_numbers) == 0:
        print("Нечётных чисел нет.")
        return []

    # Сортируем числа в порядке убывания
    sorted_odds = sorted(odd_numbers, reverse=True)
    return sorted_odds
# Запрашиваем ввод массива у пользователя
input_array = input("Введите элементы массива через пробел: ").split()
array = [int(x) for x in input_array]
# Решение первой задачи
max_val, idx = find_max_and_index(array)
print(f'\nМаксимальное значение: {max_val}, индекс: {idx}\n')
# Решение второй задачи
result = extract_odd_numbers(array)
if result:
    print('Отсортированный список нечётных чисел:', result)
else:
    print('Нечётных чисел нет.')