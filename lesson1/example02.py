print("Преобразование секунд в время")
TimeEntry = int(input("Введите секунды: "))
mm, ss = divmod(TimeEntry, 60)
hh, mm = divmod(mm, 60)
print("{}:{}:{}".format(hh, mm, ss))