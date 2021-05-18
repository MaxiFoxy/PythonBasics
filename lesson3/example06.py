def explode(separator, string, limit=0):
    """
    Переделывает строку в массив через разделяемый символ
    :param separator: Разделитель
    :param string: Строка
    :param limit: количество значений
    :return: Ввыводит массив
    """
    run = []
    n = 0
    i = 0
    try:
        limit=int(limit)
    except ValueError:
        print("Значение limit должнобыть типа INT")
    while True:
        if limit <= i and limit > 0:
            break
        try:
            run.append(string[n:string.index(separator, n)].strip())
            n = string.index(separator, n) + 1
        except ValueError:
            run.append(string[n:].strip())
            break
        i+=1
    separator = None
    string = None
    limit = None
    return run

def int_func0(text): #такой себе вариант так как при большой букве он будет менять на другой символ
    letter = chr(ord(text[0]) - 32)
    print(letter)
    text = letter + text[1:]
    return text


def int_func(text):
    if text[0] != text[0].upper():
        text = text[0].upper()+text[1:]
        return text
    else:
        return text

run = explode(" ", input("Введител текст: "))
str=""
for i in run:
    str+=int_func(i)+" "

print(str)

#print(run.title())