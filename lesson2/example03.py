def monthname(nummonth):
    month = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"]
    month = month[nummonth - 1]
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
        SeasonsName = int(NumMonth / 3)
        SeasonsName = list_seasons[SeasonsName]
        # месяц/3 и 12 прировнять к 0, обрезаем всё после запятой и получим ключ
        #Получается
        #месяц  деление на 3    INT Время года
        #0	    0	            0	Зима
        #1	    0,333333333	    0	Зима
        #2	    0,666666667	    0	Зима
        #3	    1	            1	Весна
        #4	    1,333333333	    1	Весна
        #5	    1,666666667	    1	Весна
        #6	    2	            2	Лето
        #7	    2,333333333	    2	Лето
        #8	    2,666666667	    2	Лето
        #9	    3	            3	Осень
        #10	    3,333333333	    3	Осень
        #11	    3,666666667	    3	Осень

        break
    else:
        print("Месяцов всего 12")
        continue
if NumMonth == 0:
    NumMonth = 12
print("Месяц:", monthname(NumMonth), "\nВремя года:", SeasonsName)
