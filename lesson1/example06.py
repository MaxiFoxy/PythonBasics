A = int(input("Введите 1-й результат: "))
B = int(input("Введите желаемый результат: "))
i: int = 1
print(f"{i}-й день: ", float(A))
while True:
    A = A + A * 0.1
    i = i + 1
    print(f"{i}-й день: ", float(A))
    if A >= B:
        break