while True:
    try:
        x = int(input("Введите положительное число: "))
        y = int(input("Введите отрицательное цисло: "))
        break
    except ValueError:
        print("Ведите число")
        continue

#x^-y = 1/x^y
def my_func(x, y):
    y=-y
    c = x
    while y>=2:
        x*=c
        y-=1
    run = 1/x
    return run

print(my_func(x, y))

print(x**y)