import os # для получения списка файлов
import json  # Doc: https://python-scripts.com/json

# Макет будушей базы
# namedb.json->[
#   (tb)1[{name : columns}
#       ,[
#           id = 0,
#           name = Name,
#           xr = xr,
#           kol = 1,
#           price = 10000
#       ],[
#           id = 0,
#           name = Name,
#           xr = xr,
#           kol = 1,
#           price = 10000
#       ],[
#           id = 0,
#           name = Name,
#           xr = xr,
#           kol = 1,
#           price = 10000
#       ]
#     ],
#   (tb)2[{name : columns},
#       [
#           id = 0,
#           name = Max,
#           age = 20,
#           password = ********
#        ],[
#           id = 1,
#           name = Den,
#           age = 21,
#           password = ********
#        ]
#      ]
# ]
def explode(separator, string, limit: int = None):
    run = []
    n = 0
    while True:
        if limit is None:
            if limit == n:
                break
        try:
            run.append(string[n:string.index(separator, n)].strip())
            n = string.index(separator, n) + 1
        except ValueError:
            run.append(string[n:].strip())
            break
    separator = None
    string = None
    limit = None
    return run

def W_R_Table(namedb, operation, input=None):
    file = None
    if operation == "w":
        file = open(f"./db/{namedb}.json", "w").write(json.dumps(input, sort_keys=True))
    elif operation == "r":
        with open(f"./db/{namedb}.json", "r") as read_file:
            file = json.load(read_file)
    else:
        print("всего 2 операции w (write) и r (read)")

    return file

def CreateTable(db):
    while True:
        name = input("Введите название таблици: ")
        columns = explode(",",input("Введите название столбцов через запятую: "))
        columns = set(columns)
        if db.index(name):#предалать проверку
          continue
        tb = [{name : columns}]
        print(type(db))
        db.append(tb)
    return db

def CreateLine(tb):
    #nametb = tb[0].keys(1)
    #paramtb = tb[0][nametb]
    #line = []
    #for i in paramtb[0]:
    #    line.append(input(f"Введите значение {i}: "))
    #tb.append(line)
    return tb

def TestDB():
    files = os.listdir("./db/")
    files = filter(lambda x: x.endswith('.json'), files)
    if files is None: #Доработать bool
        return bool(false)
    else:
        return bool(true)

print("Добро пожаловать!")
p = None
if TestDB:
    p = "\n(2) Использовать готовую JSON базу"
print(f"(1) Создать JSON базу{p}")
run = input("Ведите число: ")
if run == "1":
    namedb = input("Введите имя Базы: ")
    db = []
    db = CreateTable(db)
    print(W_R_Table(namedb,"w",db))
    print(W_R_Table(namedb, "r"))
else:
    print("WTF???")
#test = input("input: ")
#print(CreateLine(CreateTable()))
#print(CreateLine(CreateTable()))
#print(workdb("test", "w", explode(",", test)))
#print(list(workdb("test", "r")))
