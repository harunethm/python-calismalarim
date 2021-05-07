def artik_yillar(yil):
  if (yil % 400 == 0 or (yil % 4 == 0 and yil % 100 != 0)):
    return True
  
yil = int(input("Hangi yila kadar öğrenmek istersiniz: "))
print("\n")

fark = 0
onceki_artikyil = 0
aralik_toplam = 0
yil_ortalama = 0
sayi = 0

for i in range(1,yil+1):
  if artik_yillar(i):
    sayi += 1
    print(i)
    if (onceki_artikyil == 0):   
      onceki_artikyil = i
    elif (onceki_artikyil != 0):
      fark =  (i - onceki_artikyil)
      onceki_artikyil = i
      aralik_toplam += fark
  
yil_ortalama = aralik_toplam/sayi
print("Kaç adet yil var:",sayi)
print("Fark Toplami:",aralik_toplam)
print("Ortalama Artik Yil araligi:", yil_ortalama)