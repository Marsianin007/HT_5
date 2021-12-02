# 1. Створіть функцію, всередині якої будуть записано список із п'яти користувачів (ім'я та пароль).
#   Функція повинна приймати три аргументи: два - обов'язкових (<username> та <password>) і третій - необов'язковий параметр <silent> (значення за замовчуванням - <False>).
#   Логіка наступна:
#       якщо введено коректну пару ім'я/пароль - вертається <True>;
#       якщо введено неправильну пару ім'я/пароль і <silent> == <True> - функція вертає <False>, інакше (<silent> == <False>) - породжується виключення LoginException

def check_user(username, password, silent = False):
    user_pass_list = [("vlad", 12092003), ("artem", 666777),  ("misha_god", 1111), ("sasha_2005", 30043002), ("alex", 123456789)]
    check_flag = False
    for i in user_pass_list:
        if username in i and i[1] == password:
            print("True")
            check_flag = True
            return True

    if check_flag != True and silent == True:
        print("False")
        return False
    elif check_flag != True and silent == False:
        raise Exception('LoginException')
        

    


check_user("vlad", 1209200, True)

