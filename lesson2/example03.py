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
    if NumMonth <= 12:
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
    if NumMonth <= 12:
        #месяц/4 поставить вес чтобы выровнять или 12 прировнять к 0
        break
    else:
        print("Месяцов всего 12")
        continue