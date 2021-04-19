import urllib.request

site = ""
webpage = str(urllib.request.urlopen(site).read().decode("utf-8"))


def parse(start, end):
    try:
        return (webpage[webpage.index(start) + len(start):webpage.index(end)])
    except ValueError:
        return "Ошибка получания данных"


divided = '<div class="catalog-item-body">'
n = webpage.index(divided)
while True:
    try:
        print(webpage[n:webpage.index(divided, n)])

        n = webpage.index(divided) + 1
    except ValueError:
        print(webpage[n:])
        break
