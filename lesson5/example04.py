with open('transfer.txt', 'r+') as file:
    us = ('One', 'Two', 'Three', 'Four')
    rus = ('Один', 'Два', 'Три', 'Четыре')
    files = file.read().splitlines()
    texts = []
    for i, text in enumerate(files):
        if text == "":
            break
        texts.append(text.replace(us[i], rus[i])+"\n")
with open('transfer_ru.txt', 'w') as file: file.writelines(texts)