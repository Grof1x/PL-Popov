import math

# ========== ЗАДАЧА 1 ==========
print("=== ЗАДАЧА 1: ВЫЧИТАНИЕ СУММЫ ЦИФР ===")

def sum_digits(n):
    return sum(int(d) for d in str(n))

number = int(input("Введите число: "))
steps = 0
current = number

print(f"\nПроцесс для числа {number}:")
while current > 0:
    digit_sum = sum_digits(current)
    print(f"{current} - {digit_sum} = {current - digit_sum}")
    current -= digit_sum
    steps += 1
print(f"Количество действий: {steps}")
# ========== ЗАДАЧА 2 ==========
print("\n=== ЗАДАЧА 2: ТРИ МАССИВА ===")
arrays = []
for i in range(3):
    print(f"Введите массив {i+1} (числа через пробел):")
    arr = list(map(int, input().split()))
    arrays.append(arr)
for i, arr in enumerate(arrays, 1):
    if arr:  # если массив не пустой
        product = math.prod(arr)
        average = sum(arr) / len(arr)
        print(f"\nМассив {i}: {arr}")
        print(f"Произведение: {product}")
        print(f"Среднее арифметическое: {average:.2f}")
    else:
        print(f"\nМассив {i} пуст!")