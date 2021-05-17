value = ['Имя','Фамилия','Год рождения','Город проживания','email','Телефон']
def reg(*value):
    str=""
    for i in value:
        data=input(f"{i}: ")
        str = f"{i}:{data}\n"+str
    return str

print(reg(*value))