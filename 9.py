# Функции для вычисления суммы цифр и проверки на простоту
def sum_digits(n):
    """Рекурсивная функция для подсчета суммы цифр натурального числа."""
    if n < 10:
        return n
    else:
        last_digit = n % 10  # Получаем последнюю цифру
        remaining_number = n // 10  # Убираем последнюю цифру
        return last_digit + sum_digits(remaining_number)
def is_prime(n, divisor=2):
    """
    Рекурсивная функция для проверки, является ли число простым,
    использующая метод пробного деления до √n.
    """
    if n <= 1:
        return False
    elif divisor * divisor > n:
        return True
    elif n % divisor == 0:
        return False
    else:
        return is_prime(n, divisor + 1)
# Основной скрипт для взаимодействия с пользователем
if __name__ == "__main__":
    try:
        # Запрашиваем ввод числа
        n = int(input("Введите натуральное число больше 1: "))

        # Подсчет суммы цифр
        digit_sum = sum_digits(n)
        print(f"Сумма цифр числа {n}: {digit_sum}")

        # Проверка числа на простоту
        prime_check_result = "YES" if is_prime(n) else "NO"
        print(prime_check_result)
    except ValueError:
        print("Ошибка ввода!")