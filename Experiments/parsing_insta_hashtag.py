import urllib.request
import time
#
#  Не работает
#
hashtag = input("Введите  хештег: ")
site = "https://www.instagram.com/explore/tags/lol/?__a=1"
t1 = time.time()
webpage = str(urllib.request.urlopen("https://www.instagram.com/explore/tags/lol/?__a=1").read())
print(site)
print(webpage)
t2 = time.time()
times = t2 - t1
print("\nВремя работы скриптав секундах:", times)
