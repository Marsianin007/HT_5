# 6. Всі ви знаєте таку функцію як <range>. Напишіть свою реалізацію цієї функції.
#   P.S. Повинен вертатись генератор.
#   P.P.S. Для повного розуміння цієї функції - можна почитати документацію по ній: https://docs.python.org/3/library/stdtypes.html#range

def new_range(finish, start = 0, step = 1):
    num = start
    while num < finish:
        yield num
        num += step

for i in new_range(5):
    print(i)


