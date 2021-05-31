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
    run = input("Введите числа через пробел: ").split(' ')
    #print(run)
    run, stop = sum_array(run, "/q")
    sums += run
    print("SUM:",sums)
    if stop == "/q":
        break
    else:
        continue