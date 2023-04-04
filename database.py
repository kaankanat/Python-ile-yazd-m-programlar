def ekle():
    isim = input("İsim: ")
    yas = input("Yaş: ")
    email = input("E-posta: ")
    kisi_listesi.append({"isim": isim, "yas": yas, "email": email})
    print("Kişi eklendi.")

def sil():
    isim = input("Silmek istediğiniz kişinin ismini girin: ")
    bulundu = False
    for kisi in kisi_listesi:
        if kisi["isim"] == isim:
            kisi_listesi.remove(kisi)
            bulundu = True
            print("Kişi silindi.")
            break
    if not bulundu:
        print("Kişi bulunamadı.")

def guncelle():
    isim = input("Güncellemek istediğiniz kişinin ismini girin: ")
    bulundu = False
    for kisi in kisi_listesi:
        if kisi["isim"] == isim:
            yeni_isim = input("Yeni isim: ")
            yeni_yas = input("Yeni yaş: ")
            yeni_email = input("Yeni e-posta: ")
            kisi["isim"] = yeni_isim
            kisi["yas"] = yeni_yas
            kisi["email"] = yeni_email
            bulundu = True
            print("Kişi güncellendi.")
            break
    if not bulundu:
        print("Kişi bulunamadı.")

def goruntule():
    if not kisi_listesi:
        print("Veri tabanı boş.")
    else:
        for kisi in kisi_listesi:
            print("İsim: " + kisi["isim"] + ", Yaş: " + kisi["yas"] + ", E-posta: " + kisi["email"])

while True:
    secim = input("Veri tabanına kişi eklemek: 1\nVeri tabandan kişi silmek: 2\nVeri tabanındaki kişiyi güncellemek: 3\nVeri tabanını görüntülemek: 4\nVeri tabanından çıkmak: q\nSeçiminiz: ")
    if secim == "1":
        ekle()
    elif secim == "2":
        sil()
    elif secim == "3":
        guncelle()
    elif secim == "4":
        goruntule()
    elif secim == "q":
        print("Program sonlandırıldı.")
        break
    else:
        print("Geçersiz seçim. Lütfen devam edin.")
