# 2. Створіть функцію для валідації пари ім'я/пароль за наступними правилами:
#   - ім'я повинно бути не меншим за 3 символа і не більшим за 50;
#   - пароль повинен бути не меншим за 8 символів і повинен мати хоча б одну цифру;
#   - щось своє :)
#   Якщо якийсь із параментів не відповідає вимогам - породити виключення із відповідним текстом.




def validation_user(user_name, password):
    check_flag = False
    for i in password:
        if i.isdigit() == True:
            check_flag = True

    if len(user_name) < 3:
        raise Exception('login length must be >= 3')

    if len(user_name) > 50:
        raise Exception('login length must be <= 50')

    if len(password) < 8:
        raise Exception('password length must be >= 8')

    if check_flag == False:
        raise Exception('password must include at least 1 digit')


validation_user("Marsianin", "kjfsdfdsd9")
