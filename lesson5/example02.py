file = open('file.txt', 'r').readlines()
print("первый вариант")
k = 0
for string in file:
    i = 0
    n = 0
    while True:
        i += 1
        try:
            s = n
            # print(string[s:string.index(" ",n)]) # вывод полной строки
            run = string[n:n + s if len(string[s:string.index(" ", n)]) >= s else string.index(" ",n)]  # если значений больше 10 то просто к значению n прибовляем 10 иначе смотри где следующий пробел
            # print(string.index(" ",n))# ищем пробел от индекса n
            n = string.index(" ", n) + 1  # прибовляем к найденому индексу 1 что бы он не зацыклился
        except ValueError:
            run = string[s:s + 10]
            run = None
            break
    k += 1
    print("Строка:",k,"| Кол.слов:",i)
#----------------------
print("второй вариант")
k = 0
for k,string in enumerate(file):
    print("Строка:",k,"| Кол.слов:",len(string.split(" ")))
print("всего",k,"строк")
file.close()