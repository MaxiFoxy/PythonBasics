def int_func0(text): #такой себе вариант так как при большой букве он будет менять на другой символ
    letter = chr(ord(text[0]) - 32)
    print(letter)
    text = letter + text[1:]
    return text


def int_func(text):
    if text[0] != text[0].upper():
        text = text[0].upper()+text[1:]
        return text
    else:
        return text

run = input("Введител текст: ").split(' ')
str=""
for i in run:
    str+=int_func(i)+" "

print(str)

#print(run.title())