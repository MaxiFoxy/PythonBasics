money:int = 1
day = 1
month = 1
while True:
    print(month, money)
    money+=1
    day+=1
    if month >= 12:
        break

print(day, money)