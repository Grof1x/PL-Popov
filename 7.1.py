# Функция для вычисления НОД
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Подпрограмма для деления дробей и приведения к несократимому виду
def divide_fractions(A, B, C, D):
    numerator = A * D  # Числитель результата
    denominator = B * C  # Знаменатель результата
    common_divisor = gcd(numerator, denominator)
    # Сокращение дроби
    reduced_numerator = numerator // common_divisor
    reduced_denominator = denominator // common_divisor
    print(f"{reduced_numerator}/{reduced_denominator}")

# Проверка принадлежности точки кругу
def is_point_inside_circle(x, y, center_x, center_y, radius):
    distance_squared = ((x - center_x) ** 2 + (y - center_y) ** 2)
    return distance_squared <= radius ** 2

# Основной код
if __name__ == "__main__":
    # Часть 1: деление дробей
    print("--- Деление дробей ---")
    A = int(input("Введите числитель первой дроби: "))
    B = int(input("Введите знаменатель первой дроби: "))
    C = int(input("Введите числитель второй дроби: "))
    D = int(input("Введите знаменатель второй дроби: "))
    divide_fractions(A, B, C, D)
    # Часть 2: проверка точек внутри окружности
    print("\n--- Точки внутри окружности ---")
    center_x, center_y = map(float, input("Центр окружности x,y: ").split())
    radius = float(input("Радиус окружности R: "))
    n_points = int(input("Количество проверяемых точек N: "))
    points = []
    for i in range(n_points):
        point = tuple(map(float, input(f"Введите координаты точки {i + 1}: ").split()))
        points.append(point)
    count_inside = sum(is_point_inside_circle(x, y, center_x, center_y, radius) for x, y in points)
    print(f"\nКоличество точек внутри окружности: {count_inside}")