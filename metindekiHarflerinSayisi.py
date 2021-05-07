metin=str(input("metin giriniz: "))
cikanlar=[]
sayi=[]
for i in metin:
    if not (i in cikanlar):
        cikanlar.append(i)
        sayi.append(1)
    else:
        sayi[cikanlar.index(i)]+=1

for j in range(len(cikanlar)):
	
    print (cikanlar[j], " ", sayi[j])

while True:
  if(input() == "x"):
    print(metin)
    break