# sayi = int(input("sayiyi giriniz: "))
# if(sayi > 50 and sayi < 100):
#     print("sayi 50 ile 100 arasında.")
# else:
#     print("sayi 50 den küçük veya 100 den büyük")

# if(sayi >= 0 and sayi % 2 == 1):
#     print("sayi pozitif tek sayidir.")
# else:
#     print("pozitif veya tek sayi değildir.")

# username = input("username: ")
# password = input("password: ")
# if(username == "harunethm"):
#     if(password == "1234"):
#         print("doğru bilgiler")
#     else:
#         print("şifre yanlış")
# else:
#     print("kullanıcı adı yanlış")

# # ----------------------------------------------------------------------------------------------------

# isim = input("isminizi giriniz: ")
# yas = int(input("yaşınızı giriniz: "))
# mezuniyet = input("mezuniyet bilginizi giriniz: ")

# if(yas > 18 and (mezuniyet == "lise" or mezuniyet == "üniversite")):
#     print(f"Sn. {isim} ehliyet alabilirsiniz.")

# # ----------------------------------------------------------------------------------------------------

# yazili_1 = input("birinci yazılı notunuzu giriniz: ")
# yazili_2 = input("ikinci yazılı notunuzu giriniz: ") 
# sozlu = input("sözlü notunuzu giriniz: ") 

# ort = (yazili_1 + yazili_2 + sozlu) / 3

# if(24 >= ort >= 0):
#     print("0")
# if(44 >= ort >= 25):
#     print("1")
# if(54 >= ort >= 45):
#     print("2")
# if(69 >= ort >= 55):
#     print("3")
# if(84 >= ort >= 70):
#     print("4")
# if(100 >= ort >= 85):
#     print("5")

# # ----------------------------------------------------------------------------------------------------

# import datetime

# tarih = input("yola çıkış tarihini giriniz (30/12/2020): ").split("/") 
# # tarih[0] gün, tarih[1] ay, tarih[2] yıl

# trafigeCikis = datetime.datetime(int(tarih[2]), int(tarih[1]), int(tarih[0]))

# fark = datetime.datetime.now() - trafigeCikis

# print(f"{fark.days // 365}. servis bakımı gelmiş.")

# # ----------------------------------------------------------------------------------------------------

# for i in range(1, 10):
#     for j in range(1, 10):
#         print(f"{i} x {j} = {i * j}")
#     print("")

# # ----------------------------------------------------------------------------------------------------

# sayi = 0
# inpt = ''
# while(not inpt):
#     inpt = input("sayi: ")
#     if(inpt.isdigit):
#         sayi = int(inpt)
#     else:
#         print("Lütfen bir sayı giriniz.")
#         inpt = ''

# asal = False
# if(sayi < 2):
#     asal = True
# else:
#     for i in range (2, sayi // 2):
#         if(sayi % i == 0):
#             asal = True
#             break

# if(not asal):
#     print(f"{sayi} sayısı asaldır.")
# else:
#     print("sayı asal değildir.")

# # ----------------------------------------------------------------------------------------------------

# import random as rnd

# hak = int(input("kaç hak olsun: "))
# kalanCan = hak

# rndSayi = rnd.randint(0, 100)
# print(rndSayi)

# while(kalanCan > 0):
#     tahmin = int(input("tahmininiz: "))
    
#     if(tahmin == rndSayi):
#         print(f"{hak - kalanCan + 1}. denemede bildin.")
#         print(f"puanın: {(100 // hak) * kalanCan}")
#         break
#     elif(tahmin < rndSayi):
#         print("daha büyük bir sayı tahmin et.")
#     elif(tahmin > rndSayi):
#         print("daha küçük bir sayı tahmin et.")
    
#     kalanCan -= 1

# # ----------------------------------------------------------------------------------------------------

# # List Comprehension

# x = []
# y = []

# y = [a for a in x]
# # for a in x:
# #     y.append(a)
# # ----------------------------------------

# y = [a for a in x if a > 0]
# # for a in x:
# #     if (a > 0):
# #         y.append(a)
# # ----------------------------------------

# y = [a if a > 0 else '...' for a in x]
# # for a in x:
# #     if (a > 0):
# #         y.append(a)
# #     else:
# #         y.append('...')
# # ----------------------------------------

# y = [(a,b) for a in x for b in x] 
# # # for c in x for d in x şeklinde devam ettirilebilir
# # # [(a,b,c,d) for a in x for b in x for c in x for d in x]
# # for a in x:
# #     for b in x:
# #         y.append((a,b))

# # ----------------------------------------------------------------------------------------------------

# import datetime as dt
# isimler = ["Ahmet", "ali", "Çınar", "DeNiz"]
# string = "Merhaba 12345 Dünya"
# yillar = [1983, 1999, 2008, 1956, 1986, 1969, 1977, 2000, 2003, 2007]
# dereceler = [20, 5, 15, -2, 0, -6]
# sonuc = []

# # soru 1 - 1-100 arasındaki sayılardan 12 ye tam bölünenleri listeleyiniz
# sonuc = [sayi for sayi in range(1, 100) if (sayi % 12 == 0)]

# # soru 2 - isimler listesindeki her ismi küçük harfe çevirip tersten yazdırınız
# sonuc = [isim.lower()[::-1] for isim in isimler]

# # soru 3 - verilen string içindeki rakamları içeren bir liste oluşturunuz
# sonuc = [letter for letter in string if (letter.isdigit())]

# # soru 4 - yillar listesindeki her doğum yılı için yaş bilgisini içeren bir liste oluşturunuz
# sonuc = [dt.datetime.now().year - yil for yil in yillar]

# # soru 5 - dereceler listesindeki eksi dereceler için buzlanma tehlikesi uyarı mesajı yazdırın
# sonuc = ['Buzlanma Tehlikesi' if derece <= 0 else derece for derece in dereceler]

# print(sonuc)

# # ----------------------------------------------------------------------------------------------------

# fonksiyon tanımlama
# def fonksiyon_ismi(parametre, parametre2):
#     sonuc = parametre + parametre2 # işlemler
#     return sonuc # sonuç döndürme

# # ----------------------------------------------------------------------------------------------------

# # soru 1 - kendisine gönderilen kelimeyi belirtilen kez ekrana yazan fonksiyon
# def fonk_1(kelime, tekrar):
#     print((kelime + "\n") * tekrar) # no need for for :D

# # soru 2 - dikdörtgenin alan ve çevresini hesaplayan fonksiyonu yazınız
# def fonk_2(kısaKenar, uzunKenar):
#     # dikdortgen = {"alan":0 , "cevre":0}
#     # dikdortgen["alan"] = kısaKenar * uzunKenar
#     # dikdortgen["cevre"] = kısaKenar * 2 + uzunKenar * 2
#     # return dikdortgen
#     return {"alan":kısaKenar * uzunKenar , "cevre":kısaKenar * 2 + uzunKenar * 2}

# # soru 3 - yazı tura uygulamasını fonksiyon kullanarak yapınız
# def fonk_3():
#     import random as rnd
#     return "Yazı" if rnd.randint(0, 10) % 2 == 0 else "Tura"

# # soru 4 - kendisine gönderilen sayının tam bölenlerini bir liste şeklinde döndüren fonksiyon
# def fonk_4(sayi):
#     # for i in range(1, sayi):
#     #     if(sayi % i == 0):
#     #         result.append(i)
#     result = [i for i in range(1, sayi) if (sayi % i == 0)]
#     return result

# # soru 5 - kendisine gönderilen iki sayı arasındaki tüm asal sayıları bulan fonksiyon
# def fonk_5(s1, s2):
#     sonuc = []
#     for s in range(s1, s2 + 1):
#         asallık = True
#         for i in range(2, s//2 + 1):
#             if s % i == 0:
#                 asallık = False
#                 break
#         if asallık:
#             sonuc.append(s)
#     return sonuc

# fonk_1("harun", 5)
# print(fonk_2(7 , 21))
# print(fonk_3())
# print(fonk_4(99))
# print(fonk_5(0, 30))

# # ----------------------------------------------------------------------------------------------------

# # default parametre verme

# def deneysel_1(taban, us):
#     return taban ** us

# # def deneysel_2(taban = 1, us): # parametrelerde default değer vermeye sondan başlanır
# #     return taban ** us

# def deneysel_3(taban, us = 1):
#     return taban ** us

# def deneysel_4(taban = 1, us = 1):
#     return taban ** us

# print(deneysel_1(2, 5)) # 2 nin 5 inci kuvvetini alır

# # print(deneysel_2(2, 5)) deneysel_2 hata verir

# print(deneysel_3(3)) # 3 ün 1 inci kuvvetini alır
# print(deneysel_3(3, 4)) # 3 ün 4 üncü kuvvetini alır

# print(deneysel_4()) # 1 in 1 inci kuvvetini alır
# print(deneysel_4(6)) # 6 nın 1 inci kuvvetini alır
# print(deneysel_4(2, 5)) # 2 nin 5 inci kuvvetini alır

# # ----------------------------------------

# # parametre olarak fonksiyon verme

# def toplama(a, b):
#     return a + b

# def cikarma(a, b):
#     return a - b
    
# def carpma(a, b):
#     return a * b

# def bolme(a, b):
#     return a // b

# def islem(a, b, fonk = toplama): # parametre olarak verilen fonksiyon da default değer alabilir
#     return fonk(a, b)

# a, b = 5, 2

# print(islem(a, b, toplama))
# print(islem(a, b, cikarma))
# print(islem(a, b, carpma))
# print(islem(a, b, bolme))
# print(islem(a, b)) # toplama yapar

# # ----------------------------------------

# parametreleri isimleri ile gönderme

# def alan(kısaKenar, uzunKenar):
#     return kısaKenar * uzunKenar

# print(alan(kısaKenar= 5, uzunKenar= 7))
# print(alan(uzunKenar= 5, kısaKenar= 7)) # bu sayede parametreleri istediğimiz sırayla verebiliriz

# # ----------------------------------------------------------------------------------------------------

# # değişken sayıda parametre ile fonksiyon oluşturma args *args (tuple tipinde)
# def toplama(*sayilar):
#     toplam = 0
#     for i in sayilar:
#         toplam += i
#     return toplam

# print(toplama())
# print(toplama(10))
# print(toplama(10, 20))
# print(toplama(10, 20, 30))
# print(toplama(10, 20, 30, 40)) # ...

# # ----------------------------------------

# # değişken sayıda parametre ile fonksiyon oluşturma keyword args *kwargs {dictionary türünde}

# def kullanici(**kullanici):
#     for key, value in kullanici.items():
#         print(f"{key.capitalize()}: {value}")
#     print("\n")

# kullanici(kullaniciAdi= "canha")
# kullanici(kullaniciAdi= "canha", sifre="1234")
# kullanici(kullaniciAdi= "canha", sifre="1234", eMail="canha@gmail.com")
# kullanici(kullaniciAdi= "canha", sifre="1234", eMail="canha@gmail.com", ulke="Türkiye")

# # ----------------------------------------

# # anlatım

# def fonk(a, b, c, *args, **kwargs):
#     print(a)
#     print(b)
#     print(c)
#     print(args)
#     print(kwargs)

# fonk(10, 20, 30, 40, 50, 60, key1= "val1", key2="val2", key3="val3")

# # -----------------------------------------------------------------------------------------------------

# x = 50

# def change():
#     global x # fonksiyon içerisinde global değişkenle oynamak için global anaghtarını kullan
#     x = 100
# def nChange():
#     x = 75

# change()
# print(x)
# x = 75
# nChange()
# print(x)

# change()
# print(x)

# # -----------------------------------------------------------------------------------------------------

# def fonk(a):
#     return a ** 2

# mFonk = lambda a: a ** 2

# print(fonk(2)) # 2 nin karesi alınır
# print(mFonk(3)) # 3 ün karesi alınır

# def fonk_2(a):
#     return lambda n: n ** a

# mFonk_2 = fonk_2(4) # mFonk_2 gönderilen değerin 4. kuvvetini geri döndürür
# mFonk_2 = fonk_2(5) # mFonk_2 gönderilen değerin 5. kuvvetini geri döndürür

# print(mFonk_2(5)) # 5 in 5. kuvveti alınır

# # -----------------------------------------------------------------------------------------------------


# # sayıların karesini alma yöntem 1 düz for döngüsü
# sayilar = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# s_kare = []
# for s in sayilar:
#     s_kare.append(s ** 2)
# print(s_kare)

# # ----------------------------------------

# # sayıların karesini alma yöntem 2 map methodu
# sayilar = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# def kareAl(s):
#     return s ** 2
# s_kare = list(map(kareAl, sayilar)) # list çevirisi yapılmaz ise object olarak kalır
# print(s_kare)

# # ----------------------------------------

# # sayıların karesini alma yöntem 2.1 map methodu lambda ile
# sayilar = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# s_kare = list(map(lambda s: s ** 2, sayilar))
# print(s_kare)

# # ----------------------------------------

# # string girilen sayıları int e çevirme (casting)
# str_sayilar = ["1", "2", "3", "4", "5"]
# int_sayilar = list(map(int, str_sayilar)) # int_sayilar = [int(s) for s in str_sayilar]
# print(int_sayilar)

# # ----------------------------------------

# kullanicilar = [
#     {"ad": "ahmet", "soyad" : "çalış"},
#     {"ad": "mehmet", "soyad": "yiğit"},
#     {"ad": "ali", "soyad": "karakaya"}
# ]

# isimler = list(map(lambda x: x["ad"], kullanicilar))
# print(isimler)

# # -----------------------------------------------------------------------------------------------------

# def ciftMi(s):
#     return s % 2 == 0

# def kareAl(s):
#     return s ** 2

# def retNull(s):
#     return None if s < 3 else s

# nums = [1, 2, 3, 4, 5, 6, 7]
# x = list(map(kareAl, nums)) # map fonksiyondan dönen değeri direk yazar
# y = list(map(ciftMi, nums))

# k = list(filter(kareAl, nums)) # filter None veya False döndürmeyen değerler için değerin kendisini yazar
# l = list(filter(ciftMi, nums)) # None veya False olursa hiçbir şey yazmaz

# print(f"map, kareAl: {x}")
# print(f"map, ciftMi: {y}")

# print(f"filter, kareAl: {k}")
# print(f"filter, ciftMi: {l}")

# # -----------------------------------------------------------------------------------------------------

# # all => eğer listedeki bütün değerler True ise True döndürür
# #        listede en az bir adet False var ise False döndürür (and operatörü gibi)
# # any => listede en az bir adet True var ise True döndürür
# #        eğer listedeki bütün elemanlar False ise False döndürür (or operatörü gibi) 

# # 0, '', ' ', None, False => False
# # > 0, "herhangiBosluksuzYazilar", 'herhangiHarfler', True => True

# liste = [True, True, True]
# sonuc = all(liste) # sonuc = True
# print(sonuc)
# sonuc = any(liste) # sonuc = True
# print(sonuc)

# liste = [True, True, False]
# sonuc = all(liste) # sonuc = False
# print(sonuc)
# sonuc = any(liste) # sonuc = True
# print(sonuc)

# liste = [True, False, False]
# sonuc = all(liste) # sonuc = False
# print(sonuc)
# sonuc = any(liste) # sonuc = True
# print(sonuc)

# liste = [False, False, False]
# sonuc = all(liste) # sonuc = False
# print(sonuc)
# sonuc = any(liste) # sonuc = False
# print(sonuc)

# # -----------------------------------------------------------------------------------------------------

# sayilar = [10, 20, 17, 14, 29, 22, 44, 32, 42]
# kullanicilar = [
#     {"kullaniciAdi": "harun", "tweetler": ["tw 1", "tw 2"], "mail": "google@gmail.com", "mahlas": "saykala"},
#     {"kullaniciAdi": "ethem", "tweetler": []},
#     {"kullaniciAdi": "calis", "tweetler": ["tw 3", "tw 4", "tw 5"], "mahlas": "scylla"}
# ]

# # sayilar.sort() # orijinal sayilar dizisini de değiştirir
# siraliSayilar = sorted(sayilar) # orijinal listeye dokunmadan yeni sıralamayı siraliSayilar'a atar
# tersSiraliSayilar = sorted(sayilar, reverse=True) # sıralamayı tersten yapar (büyükten küçüğe)
# siraliKullanicilar = sorted(kullanicilar, key=len)
# ismeGoreSiraliKullanicilar = sorted(kullanicilar, key=lambda k: k["kullaniciAdi"])
# tersSiraliKullanicilar = sorted(kullanicilar, key=len, reverse=True)

# print(sayilar)
# print(siraliSayilar)
# print(tersSiraliSayilar)
# print(siraliKullanicilar)
# print(ismeGoreSiraliKullanicilar)
# print(tersSiraliKullanicilar)

# # -----------------------------------------------------------------------------------------------------

# # try => kodun yazıldığı bölüm
# # except => bir hata çıkarsa yakalandığı bölüm
# # else => hatasız şekilde try sona ulaşırsa çalışacak kısım
# # finally => hata olsun yada olmasın en sonda çalışacak kısım

# try:
#     x = int(input("x: "))
#     y = int(input("y: "))
#     print(x / y)
# except:
#     print("hatalı değer girişi.")

# # ----------------------------------------

# try:
#     x = int(input("x: "))
#     y = int(input("y: "))
#     print(x / y)
# except Exception as hata:
#     print("bilinmeyen hata oluşumu.")
#     print(hata)

# # ----------------------------------------

# try:
#     x = int(input("x: "))
#     y = int(input("y: "))
#     print(x / y)
# except ValueError:
#     print("hatalı değer girişi.")
# except ZeroDivisionError:
#     print("sıfıra bölüm tanımsızdır.")

# # ----------------------------------------

# try:
#     x = int(input("x: "))
#     y = int(input("y: "))
#     print(x / y)
# except (ValueError, ZeroDivisionError):
#     print("hatalı değer girişi.")

# # ----------------------------------------

# try:
#     x = int(input("x: "))
#     y = int(input("y: "))
#     print(x / y)
# except (ValueError, ZeroDivisionError) as e:
#     print("hatalı değer girişi.")
#     print(e)

# # ----------------------------------------

# try:
#     x = int(input("x: "))
#     y = int(input("y: "))
#     print(x / y)
# except (ValueError, ZeroDivisionError):
#     print("hatalı değer girişi.")
# else:
#     print("kod hatasız olarak çalıştırıldı.")

# # -----------------------------------------------------------------------------------------------------

# liste = ["1", "2", "5a", "10b", "abc", "10", "50"]
# soru 1 - liste elemanları içindeki sayısal değerleri bulunuz.

# for i in liste:
#     try:
#         print(int(i))
#     except:
#         pass

# soru 2 - kullanıcı 'q' değeri girmedikçe alınan her input değerinin sayı olduğundan emin ol,
# sayı değilse hata mesajı göster.

# liste = []
# while True:
#     inp = input("sayılar: ")
#     if(inp == "q"):
#         break
#     else:
#         try:
#             liste.append(int(inp))
#         except:
#             print("hatalı değer girişi. çıkış için 'q' giriniz.")

# soru 3 - dict ve key bilgilerini parametre olarak alan get(d, key) fonksiyonunu hazırla.
# d = {"urunAdi": "samsung s10"}
# d["price"] => KeyError
# get(d, price) => None
# get(d, urunAdi) => samsung s10

# def get(dict, key):
#     try:
#         return dict[key]
#     except:
#         return None

# d = {"urunAdi": "samsung s10"}
        
# while True:
#     key = input("aramak istediğinğiz değerin key bilgisini giriniz: ")
#     if(key == "q"):
#         break
#     print(get(d, key))

# # -----------------------------------------------------------------------------------------------------

# x, y = 10, 0
# # z = x / y => y değeri sıfır olduğu için DivideByZero hatası fırlatır

# y = 2
# z = x / y # normal şartta bir hata fırlatmaz ancak =>
# if( y == 2 ): # kafamıza göre bir koşul
#     raise ValueError('2 ye bölme hatası') # istenen her hata raise anahtar kelimesi ile fırlatılabilir

# # örnek

# def renklendir(text, color):
#     colors = ("red", "green", "blue")
#     if(type(text) is not str):
#         raise TypeError("text bilgisi str tipinde olmalı.")
#     if(type(color) is not str):
#         raise TypeError("renk bilgisi str tipinde olmalı.")
#     if(color not in colors):
#         raise ValueError("geçersiz renk ismi.")
#     print(f"{text}, {color}")

# try:
#     renklendir("yeşil yazı", "green")
#     renklendir("kırmızı yazı", "red")
#     renklendir("mavi yazı", "white")
#     renklendir("mavi yazı", 3)
# except Exception as ex:
#     print(ex)

# # -----------------------------------------------------------------------------------------------------

# # soru 1 - faktoriyel fonksiyonu oluşturup fonksiyona gelen değer için hata mesajı oluştur.

# def faktoriyel(sayi):
#     sonuc = 1
#     if(type(sayi) is str):
#         raise TypeError("harflerin / kelimelerin faktöriyeli alınamaz :D")
#     elif( sayi < 0 ):
#         raise ValueError("negatif sayı olamaz")
#     elif(sayi == 0):
#         return 1

#     for i in range(1, sayi + 1):
#         sonuc *= i
#     return sonuc



# for i in [2, 5, 6, -4, '3a', 8, 9, 1, 0]:
#     try:
#         x = faktoriyel(i)
#     except Exception as ex:
#         x = ex
#         continue
#     finally:
#         print(f"{i}! = {x}")

# # soru 2 - girilen parola içerisinde tr karakter var ise hata veren kodu yaz.

# def parolaKontrol(parola):
#     trKarakterler = ('ğ', 'ü', 'ı', 'ş', 'ç', 'ö', 'İ', 'Ğ', 'Ü', 'Ş', 'Ö', 'Ç')
#     for i in parola:
#         if (i in trKarakterler):
#             raise ValueError("parola tr karakter içermemelidir.")
#     return True

# try:
#     print(parolaKontrol("harunEthem"))
#     print(parolaKontrol("harunEthemÇalış"))
# except Exception as ex:
#     print(ex)

# # -----------------------------------------------------------------------------------------------------

# # pdb ile debugging
# # set_trace() => breakPoint
# # l => list => bulunulan durumdaki kodları gösterir
# # n => next line => bulunduğu satırdaki kodu işletir ve sonraki satıra geçer
# # c => continue => bir sonraki breakPointe kadar durmadan kodları işler 
# # degisken_ismi => değişkenin o andaki durumunu gösterir
# # p degisken_ismi=> print => bi farkı yok sadece p eklenmiş :D 

# import pdb

# one = "one"
# two = "two"
# liste = [2, 5, 6, -4, '3a', 8, 9, 1, 0]

# pdb.set_trace()

# sonuc = one + two
# three = "three"
# sonuc += three
# print(sonuc)

# # -----------------------------------------------------------------------------------------------------

# import module # module.py dosyasını import eder

# print(module.sayilar)

# # ----------------------------------------

# import module as m # module.py dosyasını modul.sayilar değil de m.sayilar şeklinde kullanabilmek için

# print (m.ogrenci)

# # ----------------------------------------

# from module import sayi # module.py içerisinden belli bir değişken import u için

# # print(module.topla(2,4)) sadece sayi import edildiği için hatalı kullanımdır
# print (module.sayi)

# # ----------------------------------------

# from module import sayilar, topla # birden fazla değişken/fonksiyon import edilebilir

# from module import sayilar as s, topla as t # import edilenler ayrı ayrı isimlendirilebilir

# # ----------------------------------------

# from module import * # değişkenleri module.degisken_ismi olarak kullanmak yerine direk olarak kullanmak için

# print(sayilar)

# # ----------------------------------------

# # eğer import edilen fonksiyonla aynı isimli fonksiyonu biz yazarsak
# # importtan önce tanımlarsak import geçerli olur, importtan sonra tanımlarsak bizim tanımladığımız geçerli olur

# def factorial(x):
#     print(f"kullanıcı tanımlı factorial methodu.{x}!")

# from math import factorial

# print(factorial(5)) # import kullanıcı tanımından sonra olduğu için import geçerli olur

# def factorial(x):
#     print(f"kullanıcı tanımlı factorial methodu. {x}!")
    
# print(factorial(5)) # kullanıcı tanımı importtan sonra olduğu için kullanıcı tanımı geçerli olur

# # -----------------------------------------------------------------------------------------------------

# import re # regular expression

# str = "python kursu: python öğrenme klavuzu, 10, 20, 30"

# yazdir = re.findall("python", str) # str içerisindeki "python" kelimelerini arar ve hepsini bir liste olarak döndürür
# print(yazdir)
# print(len(yazdir))

# # ----------------------------------------

# yazdir = re.split(" ", str) # str stringini boşluk karakterlerinden böler ve liste oluşturur
# print(yazdir)

# # ----------------------------------------

# yazdir = re.sub(" ", "-", str) # str içerisindeki bütün boşluk karakterlerini tire ile değiştirir
# print(yazdir)

# yazdir = re.sub("\s", "-", str) # str içerisindeki bütün boşluk karakterlerini(\s) tire ile değiştirir
# print(yazdir)

# # ----------------------------------------

# yazdir = re.search("python", str)
# print(yazdir)
# print(yazdir.span())
# print(yazdir.start())
# print(yazdir.end())
# print(yazdir.group())
# print(yazdir.string)

# # -----------------------------------------------------------------------------------------------------

# import termcolor # pip install termcolor

# yazi = termcolor.colored("merhaba", color="red", on_color="on_grey")
# print(yazi)

# # -----------------------------------------------------------------------------------------------------