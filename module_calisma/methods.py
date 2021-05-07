import dataBase as db

def urunEkle(urunAdi, fiyat):
    try:
        db.urunler.append({
            "id":len(db.urunler) + 1,
            "urunAdi": urunAdi,
            "fiyat": fiyat
        })
    except Exception as e:
        print(e)
        

def urunGuncelle(id, guncelAd, guncelFiyat):
    try:
        for urun in db.urunler:
            if(urun["id"] == id):
                urun["urunAdi"] = guncelAd
                urun["fiyat"] = guncelFiyat
                break
        else:
            print("Sütun ürün bilgilerinde yok.")
    except Exception as e:
        print(e)
            
def urunleriGetir():
    for urun in db.urunler:
        print(f"ID:{urun['id']}\nÜrün Adı : {urun['urunAdi']}\nFiyat : {urun['fiyat']}\n")

