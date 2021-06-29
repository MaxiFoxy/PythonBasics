with open('salary.txt', 'r') as file:
    file = file.read().splitlines()
    for i in file:
        if sum(map(float, i.split(" ")[1:])) <= 20000: print(i.split(" ")[0],sum(map(float,i.split(" ")[1:])))
    #print(sum(map(int, i.split(" ")[1:])) / len(i.split(" ")[1:]))