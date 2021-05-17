import pandas as pd
import time
import os

t1 = time.time()
filename = r'C:/Users/mlapin/Downloads/test.xlsx'
df = pd.read_excel(filename)
based = list(df['based'])
red = list(df['red'])
white = list(df['white'])
po = list(df['po'])
ok = list(df['ok'])
pz = list(df['pz'])
rezerv = list(df['based'])
i = 0
while True:
    #(based[i])
    if rezerv[i][0] == 'Б':
        rezerv[i] = 'Ц' + rezerv[i][1:]
        try:
            key = based.index(rezerv[i])
            # можно сократить добовляя в именнованный массив
            ck = red[key]
            bk = red[i]
            cb = white[key]
            bb = white[i]
            cpo = po[key]
            bpo = po[i]
            cok = ok[key]
            bok = ok[i]
            cpz = pz[key]
            bpz = pz[i]
            print(i, based[i], ck, bk, cb, bb, cpo, bpo, cok, bok, cpz, bpz)
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
            cpo = po[i]
            bpo = po[key]
            cok = ok[i]
            bok = ok[key]
            cpz = pz[i]
            bpz = pz[key]
            print(i, based[i], ck, bk, cb, bb, cpo, bpo, cok, bok, cpz, bpz)
        except ValueError:
            continue
    else:
        print("не получилось(")

    text = f'<svg width="300px" height="500px" xmlns="http://www.w3.org/2000/svg"><line x1="0" y1="0" x2="300" y2="0" stroke-width="1" stroke="rgb(0,0,0)"/><line x1="300" y1="0" x2="300" y2="500" stroke-width="1" stroke="rgb(0,0,0)"/><line x1="0" y1="0" x2="0" y2="500" stroke-width="1" stroke="rgb(0,0,0)"/><line x1="0" y1="500" x2="300" y2="500" stroke-width="1" stroke="rgb(0,0,0)"/><text x="50" y="25">Образец не для продажи</text><text x="75" y="50">{based[i]}</text><text x="70" y="75">Артикула для заказа</text><line x1="0" y1="83" x2="500" y2="83" stroke-width="1" stroke="rgb(0,0,0)"/><text x="120" y="100">(Золото):</text><text x="120" y="120">Красное:</text><text x="10" y="140">Ц: {ck}</text><text x="10" y="165">Б: {bk}</text><text x="120" y="185">Белое:</text><text x="10" y="205">Ц: {cb}</text><text x="10" y="225">Б: {bb}</text><line x1="0" y1="235" x2="500" y2="235" stroke-width="1" stroke="rgb(0,0,0)"/><text x="120" y="255">(Серебро):</text><text x="90" y="280">РОДИРОВАНИЕ:</text><text x="10" y="300">Ц: {cpo}</text><text x="10" y="325">Б: {bpo}</text><line x1="0" y1="333" x2="500" y2="333" stroke-width="1" stroke="rgb(0,0,0)"/><text x="80" y="350">ОКСИДИРОВАНИЕ:</text><text x="10" y="370">Ц: {cok}</text><text x="10" y="395">Б: {bok}</text><line x1="0" y1="405" x2="500" y2="405" stroke-width="1" stroke="rgb(0,0,0)"/><text x="120" y="425">Золочение:</text><text x="10" y="445">Ц: {cpz}</text><text x="10" y="470">Б: {bpz}</text></svg>'.encode('utf-8')
    file = open(f"C:/Users/mlapin/Downloads/2/{based[i]}.svg", "wb").write(text)

    i += 1
    if i >= len(based):
        break

#directory = 'C:/Users/mlapin/Downloads/1/'
#files = os.listdir(directory)
#for i in based:
    #print(files.index(i+".svg"))
t2 = time.time()
times = t2 - t1
print(times)

