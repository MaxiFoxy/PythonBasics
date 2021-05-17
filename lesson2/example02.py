str = input("Введите занчения: ")
i = 0
run = []
while True:
        if len(str) == i:
            break
        elif i % 2 == 0:
            try:
                run.append(str[i+1])
            except IndexError:
                run.append(str[i])
        elif i % 1 == 0:
            run.append(str[i-1])
        else:
            print("Упс! Что-то пошло не так!")
        i+=1
print(run)