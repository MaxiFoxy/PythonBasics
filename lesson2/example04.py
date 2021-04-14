string = input("Введите слова: ")
n = 0
while True:
    try:
        s = n
        # print(string[s:string.index(" ",n)]) # вывод полной строки
        print(string[n:n + 10 if len(string[s:string.index(" ", n)]) >= 10 else string.index(" ", n)])  # если значений больше 10 то просто к значению n прибовляем 10 иначе смотри где следующий пробел
        # print(string.index(" ",n))# ищем пробел от индекса n
        n = string.index(" ", n) + 1  # прибовляем к найденому индексу 1 что бы он не зацыклился
    except ValueError:
        print(string[s:s + 10])
        break
