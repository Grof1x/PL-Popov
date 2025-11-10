def fibonacci_sum(n):
    if n == 0 or n == 1:
        return n
    prev = 0
    curr = 1
    result = 1
    for _ in range(2, n + 1):
        next_num = prev + curr  # следующее число равно 0 + 1
        result += next_num #складывает следующее число и получает результат
        prev, curr = curr, next_num
    return result

n = int(input("Введите N: "))
print(fibonacci_sum(n))