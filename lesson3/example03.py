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
        if limit <= i:
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
    #limit = None
    return run

def sum_max_two_values(*value):
    """
    Показывает сумму 2 больших значений из массива чисел
    :param value: массив чисел
    :return: выводит сумму 2 больших значений
    """
    sort = sorted(value)
    sort.reverse()
    return int(sort[0]) + int(sort[1])

print(sum_max_two_values(*explode(",",input("Введите числа через запятую: "),3))) #превращает строку в массив с ограничением 3 значения массива, и показывает сумму 2 больших чисел
