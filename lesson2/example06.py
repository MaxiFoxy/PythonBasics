#
# не работает, процессе делается
#
import os # для получения списка файлов
import json  # Doc: https://python-scripts.com/json

# Макет будушей базы
# dbName.json->[
#{tb:
#   {name : tb0}
#   {name : tb1}
#}
#   (tb)1[tb0
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
#   (tb)2[tb1,
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
dbName = None
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
        file = open(f"./db/{namedb}.json", "w").write(json.dumps(input))
    elif operation == "r":
        with open(f"./db/{namedb}.json", "r") as read_file:
            file = json.load(read_file)
    else:
        print("всего 2 операции w (write) и r (read)")

    return file

def CreateTable(namedb):
    while True:
        name = input("Введите название таблици: ")
        columns = explode(",", input("Введите название столбцов через запятую: "))
        tb = {"name" : name, "columns" : columns}
        db = W_R_Table(namedb, "r")
        db["table"].append(tb)
        w = W_R_Table(namedb, "w", db)
        return w, db
        break

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
        return None
    else:
        return files

def InteractionDB(dbName):
    while True:
        print("(1) Создать Таблицу\n(2) Удалить Таблицу\n(3) Открыть таблицу")
        run = input("Ведите число: ")
        if run == "1":
            p = CreateTable(dbName)
            print(p)
            continue
        elif run == "2":
            print("Удалить Таблицу")
            continue
        elif run == "3":
            print("Открыть таблицу")
            continue
        else:
            print("Введите номер пункта который надо сделать")
            continue

print("Добро пожаловать!")
#gb = {'table': [{'name':'test', 'columns':['id', 'price', 'kol', 'xr', 'name']}]}
#W_R_Table("db0", "w", gb)
while True:
    p = None
    if TestDB() != None:
        p = "\n(2) Использовать готовую JSON базу"
    print(f"(1) Создать JSON базу{p}")
    run = input("Ведите число: ")
    if run == "1":
        print("Введиет /q что вернуться назад")
        namedb = input("Введите имя Базы: ")
        if namedb == "/q": continue
        W_R_Table(namedb, "w", {"table": []})
        dbName = namedb
        InteractionDB(dbName)
        #print(W_R_Table(namedb,"w",{"table":[]}))
        #print(W_R_Table(namedb, "r"))
        break
    elif run == "2":
        list=[]
        for name in TestDB():
            list.append(name[:-5])
            print(name.index(name), name[:-5])
        while True:
            print("Введиет /q что вернуться назад")
            try:
                run = input("Выберете базу (Введите номер базы): ")
                if list[int(run)] != None:
                    break
            except IndexError:
                continue
            except ValueError:
                if run == "/q":
                    break
                else:
                    continue
        if run == "/q": continue
        dbName = list[int(run)]
        InteractionDB(dbName)
        break
    else:
        print("Введите номер пункта который надо сделать")
        continue

print(dbName)
#test = input("input: ")
#print(CreateLine(CreateTable()))
#print(CreateLine(CreateTable()))
#print(workdb("test", "w", explode(",", test)))
#print(list(workdb("test", "r")))
