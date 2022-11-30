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

ktory=0
for i in vysky:
    if ktory<i:
        ktory=i
        

ktory1=0
for j in roknarodenia:
    if ktory1<j:
        ktory1=j

pom=-1
pom2=-1
hladat = ktory1
hladatn = ktory

while hladat != '' or hladatn != '':
    for i in roknarodenia:
        if i==int(hladat):
            pom=pom+1
            print(str(mena[pom])+' je majmladší.')
        else:
            pom=pom+1
    for j in vysky:
        if j==int(hladatn):
            pom2=pom2+1
            print(str(mena[pom2])+' je najvyšší.')
        else:
            pom2=pom2+1
    hladat = ''
    hladatn = ''
        
        
    
    
   
   
 
