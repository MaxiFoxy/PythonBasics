print('1 способ')
Num = max(list(input("Введите число: ")))
print(f'Самое большое число в числе: {Num}')
print('2 способ')
Num = sorted(list(input("Введите число: ")))
print('Самое большое число в числе: {}'.format(Num[len(Num) - 1]))
print('3 способ')
Num = int(input("Введите число: "))
Max = Num % 10
while True:
    Num = Num // 10
    if Num % 10 > Max:
        Max = Num % 10
    if Num > 9:
        continue
    else:
        print("Самое большое число в числе: ", Max)
        break
