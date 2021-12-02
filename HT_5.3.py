# 3. На основі попередньої функції створити наступний кусок кода:
#   а) створити список із парами ім'я/пароль різноманітних видів (орієнтуйтесь по правилам своєї функції) - як валідні, так і ні;
#   б) створити цикл, який пройдеться по цьому циклу і, користуючись валідатором, перевірить ці дані і надрукує для кожної пари значень відповідне повідомлення, наприклад:
#      Name: vasya
#      Password: wasd
#      Status: password must have at least one digit
#      -----
#      Name: vasya
#      Password: vasyapupkin2000
#      Status: OK
#   P.S. Не забудьте використати блок try/except ;)

user_pass_list = [("vlad", "vlad2003"), ("artem", "a"),  ("misha_god", "1111223344"), ("sasha_2005", "30043002"), ("alex", "123456789")]

class ShortLogin(Exception):
    pass
class LongLogin(Exception):
    pass
class ShortPass(Exception):
    pass
class NoDigit(Exception):
    pass
class DemonNum(Exception):
    pass


def validation_user(user_name, password):
    check_flag = False
    for i in password:
        if i.isdigit() == True:
            check_flag = True

    if len(user_name) < 3:
        raise ShortLogin('Login length must be >= 3')

    if len(user_name) > 50:
        raise LongLogin('Login length must be <= 50')

    if len(password) < 8:
        raise ShortPass('Password length must be >= 8')

    if len(password) == 13:
        raise DemonNum ('Pass can not be len 13')

    if check_flag == False:
        raise NoDigit('Password must include at least 1 digit')


def check_each_user():
    for i in user_pass_list:
        print("")
        print("Name: " + i[0])
        print("Password: " + i[1])
        try:
            validation_user(i[0], i[1])
        except ShortLogin:
            print("Status: " + "Login must be >= 3")
        except LongLogin:
            print("Status: " + "Login must be <= 50")
        except ShortPass:
            print("Status: " + "Password must be >= 8")
        except NoDigit:
            print("Status: " + "Password must include at least 1 digit")
        except DemonNum:
            print("Status: " + "pass can not be len 13")
        else:
            print("Status: OK")

check_each_user()
        

