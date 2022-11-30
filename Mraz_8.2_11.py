import random
vstup = input('Zadaj text:') #do premennej vstup si uložím zadaný vstup
sifra = '' #premennú sifra nastavím ako string
for znak in vstup: #for cyklus na šifrovanie
    a=random.randint(97,122)
    novyznak = chr(a) #do premennej novyznak uložím znak
    sifra = sifra+novyznak #do premennej sifra uložím novyznak
print(sifra) #vypíšem šifru

subor=open('sifra.txt','w')
subor.write(vstup)
subor.write(',')
subor.write(sifra)
subor.write('\n')
subor.close()
