import tkinter
from random import *
canvas= tkinter.Canvas(width=800, height=600, bg='white')
canvas.pack()

subor=open('clanok.txt','r', encoding='utf-8')

pocetnost={}

for r in subor:
    r=r.replace(',','')
    slova=r.split()
    for slovo in slova:
        pocetnost[slovo]=pocetnost.get(slovo,0)+1
subor.close()

zoznam=[]
for ntica in pocetnost.items():
    zoznam.append((ntica[1],ntica[0]))

zoznam.sort(reverse=True)

kopia=[]
for prvok in zoznam:
    if len(prvok[1])>=3:
        kopia.append(prvok)

kopia=kopia[:40]

poradie=0
maxy=800

def rgb(r,g,b):
    return '#{:02x}{:02x}{:02x}'.format(r,g,b)

for pocet,slovo in kopia[::-1]:
    velkost=poradie+5
    x=randint(100,700)
    y=randrange(100,500)
    farba=rgb(randrange(256),randrange(256),randrange(256))
    uhol=randint(-90,90)
    canvas.create_text(x,y,text=slovo, font=('Arial',velkost),angle=uhol, fill=farba)
    poradie+=1
