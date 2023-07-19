# Задача 14: Требуется вывести все целые степени двойки
# (т.е. числа вида 2^k), не превосходящие числа N.

# Нам понадобится счетчик count, для имитации степени двойки,
# а также переменная deuce, для того, чтобы складывать в неё
# результат возведения двойки в степень по циклу.
count = 0
deuce = 1

# Вводим число N с клавиатуры:
print("Введите число N ")
n = int(input())

if n == 1:
    print(1)
# Ищем числа - степени двойки
else:
    for i in range(n, 0, -1):
        i -= 1
        while i % 2 == 0 and i > 0:
            i /= 2
            count += 1

# Выводим степени двойки в консоль
    for i in range(count, 0, -1):
        while deuce <= n:
            deuce *= 2
            if deuce <= n:
                print(deuce)


