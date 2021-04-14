def monthname(nummonth):
    month = ("Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь")
    month = month[nummonth-1]
    return month

print("1 способ")
Seasons = {"Зима": (12, 1, 2), "Весна": (3, 4, 5), "Лето": (6, 7, 8), "Осень": (9, 10, 11)}
while True:
    try:
        NumMonth = int(input("Введите номер месяца: "))
    except ValueError:
        print("Введите число например 12 >>> (Декабрь, Зима)")
        continue
    if 1 <= NumMonth <= 12:
        for key in Seasons:
            try:
                if Seasons[key][Seasons[key].index(NumMonth)]:
                    SeasonsName = key
                    break
            except ValueError:
                continue
        break
    else:
        print("Месяцов всего 12")
        continue

print("Месяц:", monthname(NumMonth), "\nВремя года:", SeasonsName)

print("2 Способ")
list_seasons = ("Зима", "Весна", "Лето", "Осень")
while True:
    try:
        NumMonth = int(input("Введите номер месяца: "))
    except ValueError:
        print("Введите число например 12 >>> (Декабрь, Зима)")
        continue
    if 1 <= NumMonth <= 12:
        if NumMonth == 12:
            NumMonth = 0
        SeasonsName=int(NumMonth/3)
        SeasonsName = list_seasons[SeasonsName]
        #месяц/3 и 12 прировнять к 0, обрезаем всё после запятой и получим ключ
        break
    else:
        print("Месяцов всего 12")
        continue
if NumMonth == 0:
    NumMonth = 12
print("Месяц:", monthname(NumMonth), "\nВремя года:", SeasonsName)