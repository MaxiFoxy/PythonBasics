import time
string = input("Введите слова: ")
t1 = time.time()
print(t1)
n = 0
while True:
    try:
        print(string[n:string.index(" ", n)])
        n = string.index(" ", n) + 1
    except ValueError:
        print(string[n:])
        break
t2 = time.time()
times = t2 - t1
print(times)