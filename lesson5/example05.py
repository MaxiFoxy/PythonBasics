from random import randint
try:
    with open('random_sum.txt', 'r') as file:
        print(sum([int(i) for i in file.readline().split(" ")[:len(file.readline().split(" "))-2]]))
except FileNotFoundError:
    with open('random_sum.txt', 'w') as file:
        for i in range(randint(1, 99), randint(10, 99)):
            file.write(str(i)+" ")
    print(file)