texts = []
while True:
    texts.append(input("Введите текст: ")+"\n")
    if texts[len(texts)-1] is None or texts[len(texts)-1] == "\n":
        with open('file.txt', 'a') as file: file.writelines(texts)
        exit("Тест записан в файл file.txt")