import tkinter
canvas = tkinter.Canvas(width=300, height=700)
canvas.pack()

subor = open('slovenske_texty.txt', 'r')
subor1 = open('anglicke_texty.txt', 'r')
frekvencia = {}
for riadok in subor:
    riadok = riadok.lower()
    for znak in riadok:
        if 'a' <= znak <= 'z':
            frekvencia[znak] = frekvencia.get(znak, 0) + 1
            
frekvencia1 = {}
for riadok1 in subor1:
    riadok1 = riadok.lower()
    for znak1 in riadok1:
        if 'a' <= znak1 <= 'z':
            frekvencia1[znak1] = frekvencia1.get(znak1, 0) + 1
            
subor.close()
subor1.close()

zoradene = sorted(frekvencia, key=frekvencia.get, reverse=True)
zoradene1 = sorted(frekvencia1, key=frekvencia1.get, reverse=True)

for kluc in zoradene:
    print(kluc, frekvencia.get(kluc))

for kluc1 in zoradene1:
    print(kluc1, frekvencia1.get(kluc1))

def kresli_stlpec(x, y, dx, dy, znaky):
    fa, fb = 'yellow', 'lightblue'
    for znak in znaky:
        canvas.create_rectangle(x, y, x+dx, y+dy, fill=fa)
        canvas.create_text(x+dx/2, y+dy/2, text=znak)
        y += dy
        fb, fa = fa, fb

def kresli_stlpec2(x1, y1, dx, dy, znaky):
    fa, fb = 'yellow', 'lightblue'
    for znak in znaky:
        canvas.create_rectangle(x1, y1, x1+dx, y1+dy, fill=fa)
        canvas.create_text(x1+dx/2, y1+dy/2, text=znak)
        y += dy
        fb, fa = fa, fb
        
velkost = 300
pocet_casti = 2
pocet_casti1 = 2
x = 10
y = 10
x1 = 10
y1 = 350
dx = 50
spracovat = zoradene[:]
spracovat1 = zoradene1[:]

while len(spracovat) > 0:
    kresli_stlpec(x, y, dx, velkost/pocet_casti, spracovat[:pocet_casti])
    spracovat = spracovat[pocet_casti:]
    x += dx
    pocet_casti *= 2

while len(spracovat1) > 0:
    kresli_stlpec(x1, y1, dx, velkost/pocet_casti1, spracovat1[:pocet_casti1])
    spracovat1 = spracovat1[pocet_casti1:]
    x1 += dx
    pocet_casti1 *= 2
    
canvas.create_text(100,330,text='===SK===',font=('Arial',20))
canvas.create_text(100,670,text='===EN===',font=('Arial',20))