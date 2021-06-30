import re
with open('thing.txt', 'r') as file:
    files = file.read().splitlines()
    info = {}
    for i in files:
        i=i.split(" ")
        kol = i[1:]
        sums = 0
        for k in kol:
            k = re.sub("[^0-9]","",k)
            if k is None or k == "":
                continue
            else:
                sums += int(k)
        #l = {i[0]:sums}
        #info.update(l)
        info[i[0]]=sums
        print(i[0],sums)
    print(info)
