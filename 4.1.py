n = int(input("Введите количество чисел N: "))
numbers = []
for _ in range(n): #задает количество n
    num = int(input("Введите число: "))
    numbers.append(num)
print(sum(numbers)) #суммирует все введенные числа