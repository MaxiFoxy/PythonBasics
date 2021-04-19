import urllib.request
import time

site = "https://google.com/"
t1 = time.time()
webpage = str(urllib.request.urlopen(site).read().decode("utf-8"))

def parse(start, end):
    try:
        return (webpage[webpage.index(start) + len(start):webpage.index(end)])
    except ValueError:
        return "Ошибка получания данных"
start = "<"
end = ">"
n = webpage.index(start)
while True:
    #print(parse("<", ">"))
    try:
        print (webpage[n:webpage.index(end, n)])
        n = webpage.index(end, n) + 1
    except ValueError:
        break
t2 = time.time()
times = t2 - t1
print("Время работы скриптав секундах:", times)
