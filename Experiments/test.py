import pandas as pd
import os

filename = r'C:/Users/user/Downloads/test.xlsx'
df = pd.read_excel(filename)
based = list(df['based'])
red = list(df['red'])
white = list(df['white'])
rezerv = list(df['based'])
i = 0
while True:
    #(based[i])
    if rezerv[i][0] == 'Б':
        rezerv[i] = 'Ц' + rezerv[i][1:]
        try:
            key = based.index(rezerv[i])

            ck = red[key]
            bk = red[i]
            cb = white[key]
            bb = white[i]
            print(i, based[i], ck, bk, cb, bb)
        except ValueError:
            continue
    elif rezerv[i][0] == 'Ц':
        rezerv[i] = 'Б' + rezerv[i][1:]
        try:
            key = based.index(rezerv[i])
            #print(i, based[i], red[key], white[key], red[i], white[i])
            ck = red[i]
            bk = red[key]
            cb = white[i]
            bb = white[key]
            print(i, based[i], ck, bk, cb, bb)
        except ValueError:
            continue
    else:
        print("не получилось(")

    text = f'<svg width="200px" height="300px" xmlns="http://www.w3.org/2000/svg"><line x1="0" y1="0" x2="200" y2="0" stroke-width="1" stroke="rgb(0,0,0)"/><line x1="200" y1="0" x2="200" y2="300" stroke-width="1" stroke="rgb(0,0,0)"/><line x1="0" y1="0" x2="0" y2="300" stroke-width="1" stroke="rgb(0,0,0)"/><line x1="0" y1="300" x2="200" y2="300" stroke-width="1" stroke="rgb(0,0,0)"/><text x="15" y="35">Образец не для продажи</text><text x="40" y="60">{based[i]}</text><line x1="0" y1="125" x2="200" y2="125" stroke-width="1" stroke="rgb(0,0,0)"/><text x="30" y="90">Артикула для заказа</text><text x="60" y="110">(Золото):</text><text x="10" y="150">ЦК: {ck}</text><text x="10" y="180">БК: {bk}</text><line x1="0" y1="200" x2="200" y2="200" stroke-width="1" stroke="rgb(0,0,0)"/><text x="10" y="230">ЦБ: {cb}</text><text x="10" y="260">ББ: {bb}</text></svg>'.encode('utf-8')
    file = open(f"C:/Users/user/Downloads/1/{based[i]}.svg", "wb").write(text)

    i += 1
    if i >= len(based):
        break

#directory = 'C:/Users/mlapin/Downloads/1/'
#files = os.listdir(directory)
#for i in based:
    #print(files.index(i+".svg"))


