import urllib.request
import time

site = "https://dm-system.ru/"
t1 = time.time()
webpage = str(urllib.request.urlopen(site).read().decode("utf-8"))


def parse(start, end, webpage):
    try:
        start = webpage.index(start) + len(start)
        end = webpage[start:].index(end) + start
        return (webpage[start:end])
    except ValueError:
        return ""


if len(parse("<title>", "</title>", webpage)) <= 0:
    print("Заголовок:", parse("property=og:title content=", ">", webpage))
else:
    print("Заголовок:", parse("<title>", "</title>", webpage))
if len(parse('<meta name="description" content=', ">", webpage)) <= 0:
    print("Описание:", parse('<meta property=og:description content=', ">", webpage))
else:
    print("Описание:", parse('<meta name="description" content=', ">", webpage))

t2 = time.time()
times = t2 - t1
print("\nВремя работы скриптав секундах:", times)

#print(webpage)
