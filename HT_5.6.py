# 6. Всі ви знаєте таку функцію як <range>. Напишіть свою реалізацію цієї функції.
#   P.S. Повинен вертатись генератор.
#   P.P.S. Для повного розуміння цієї функції - можна почитати документацію по ній: https://docs.python.org/3/library/stdtypes.html#range





def new_range(*arg):
    arg = list(arg)
    arg = list(map(int, arg))
    if len(arg) == 1:
        finish = arg[0]
        num = 0
        step = 1
        while num < finish and step > 0:
            yield num
            num += step

    if len(arg) == 2:
        finish = arg[1]
        num = arg[0]
        step = 1
        while num < finish and step > 0:
            yield num
            num += step

    if len(arg) == 3:
        finish = arg[1]
        num = arg[0]
        step = arg[2]
        while num < finish and step > 0:
            yield num
            num += step

        while num > finish and step < 0:
            yield num
            num += step

for i in new_range(0, 10):
    print(i)

#for i in new_range(5):
#    print(i)
