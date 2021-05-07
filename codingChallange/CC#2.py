girdi = int(input("sayıyı giriniz : "))
toplam = 0
for i in range(1, int(girdi / 2) + 1):
    if(girdi % i == 0):
        toplam += i
if(toplam == girdi):
    print("perfect number")
else:
    print("not")