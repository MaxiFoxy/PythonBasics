print("Регистрация")
while True:
    #    if input("если вы зарегестированы введите: Вход \n иначе нажмите Enter \n >>>>") == "Вход":
    #        break
    Name = input("Введите имя: ")
    Login = input("Введите Login: ")
    Password = input("Введите Пароль: ")
    RepeatPassword = input("Повторите пароль: ")
    if not Name or not Login or not Password or not RepeatPassword:
        print("Какое-то поле не заполнено")
        continue
    elif RepeatPassword != Password:
        while RepeatPassword != Password:
            print("Пароли не совподают")
            Password = int(input("Введите Пароль: "))
            RepeatPassword = int(input("Повторите пароль: "))
        print(f"{Name}, вы успешно зарегестрированы")
        break
    elif RepeatPassword == Password:
        print(f"{Name}, вы успешно зарегестрированы")
        break
    else:
        print('Упс! Что-то пошло не так!\nОбратитесь к Администратору')
        continue
if Name and Login and Password and RepeatPassword:
    print("Авторизация")
    while True:
        AuthLogin = input("Введите Login: ")
        AuthPassword = input("Введите пароль: ")
        if AuthPassword == Password and AuthLogin == Login:
            print(f"{Name}, вы успешно авторизовались!")
            break
        else:
            print(f"Логин или Пароль не правильный!")
            continue
    print("{}! Добро пожаловать! Ваш логин: {}".format(Name, Login))
print("Конец")
