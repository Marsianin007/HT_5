# 5. Запишіть в один рядок генератор списку (числа в діапазоні від 0 до 100), сума цифр кожного елемент якого буде дорівнювати 10.
#   Перевірка: [19, 28, 37, 46, 55, 64, 73, 82, 91]


arr = [num for num in range(100) if num // 10 + num % 10 == 10]
print (arr)