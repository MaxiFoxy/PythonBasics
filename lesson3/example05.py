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

def sum_array(array, value):
    """
    считает сумму чиссел в массиве при встрече знака спец знака останавливает сложение
    если небыло спец знака просто суммирует цисла в массиве
    :param array: принимает массив значений
    :return: выводит значение суммы, и стоп символа
    """
    n=0
    for i in array:
        try:
            i = int(i)
            n+=i
        except ValueError:
            if value == i:
                break
            else:
                continue
    return n,i

sums=0 #сумма всех чисел

while True:
    print("Введите /q чтобы остановить вычасления")
    run = explode(" ", input("Введите числа через пробел: "))
    #print(run)
    run, stop = sum_array(run, "/q")
    sums += run
    print("SUM:",sums)
    if stop == "/q":
        break
    else:
        continue