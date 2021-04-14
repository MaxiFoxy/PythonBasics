Rating = []
while True:
    print("Для выхода введите любое значени кроме цифр")
    try:
        RatingInput = int(input("Введите число: "))
        Rating.append(RatingInput)
        Rating = sorted(Rating)
        Rating.reverse()
        print("Пользователь ввел число:", RatingInput, "Результат", Rating)
    except ValueError:
        print("Итог:", Rating)
        break