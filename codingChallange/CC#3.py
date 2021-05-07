#girdi = input("string'i giriniz : ")
girdi = "The quick brown fox jumps over the lazy dog".replace(" ", "")
#sıralıHal = ",".join(girdi).split(",")
sıralıHal = list(girdi)

for i in range(len(girdi)):
    for j in range(len(girdi)):
        if(ord(sıralıHal[i].lower()) < ord(sıralıHal[j].lower())):
            sıralıHal[i], sıralıHal[j] = sıralıHal[j], sıralıHal[i]

print(sıralıHal)