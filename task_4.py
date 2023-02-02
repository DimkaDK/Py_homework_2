"""
Задача 4: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
Пример 10: 0, 1, 2, 3
"""

number = int(input("Введите число: "))
i = 1
product = 2
degrees = []
degrees.append(0)
while product <= number:
    product *= 2
    degrees.append(i)
    i += 1
print(f"Все целые степени двойки, не превосходящие {number}: {degrees}")
