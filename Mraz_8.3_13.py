subor = open('osoby.txt', 'r')
mena=[]
vysky=[]
roknarodenia=[]
mesto=[]
riadok=subor.readline()    
while riadok != '':
    riadok = riadok.split(';')
    mena.append(riadok[0])
    vysky.append(int(riadok[1]))
    roknarodenia.append(int(riadok[2]))
    mesto.append(riadok[3].strip())
    riadok=subor.readline()


pom=-1
pom2=-1
hladat = input('Zadaj rok narodenia: ')
hladatm = input('Zadaj mesto v ktorom si sa narodil: ')

while hladat != '' or hladatm != '':
    for i in roknarodenia:
        if i==int(hladat):
            pom=pom+1
            print(str(mena[pom])+' sa narodil/a v roku '+str(hladat))
        else:
            pom=pom+1
    for j in mesto:
        if str(j)==hladatm:
            pom2=pom2+1
            print(str(mena[pom2])+' sa narodil/a v meste '+str(hladatm))
        else:
            pom2=pom2+1
    hladat = input('Zadaj rok narodenia: ')
    hladatm = input('Zadaj mesto v ktorom si sa narodil: ')
    pom=-1
    pom2=-1