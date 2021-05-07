girdi = input("sayiyi giriniz : ")
toplam = 0
carpim = 1
for i in range(len(girdi)):
    toplam += int(girdi[i])
    carpim *= int(girdi[i])
if(toplam == carpim):
    print("spy number")
else:
    print("not")