while True:
    try:
        a = int(input(f"Введите первое число: "))
        b = int(input(f"Введите второе число: "))
        print((lambda a, b: a / b)(a, b))
        break
    except ValueError:
        print("Вводите числа")
    except ZeroDivisionError:
        print("На ноль Делить нельзя")