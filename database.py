# --------------------------------------------
# Kullanıcıdan isim, yaş, e-posta bilgileri alınıyor
# --------------------------------------------
def bilgi_gir():
    isim = input("İsim: ")
    yas = input("Yaş: ")
    email = input("E-posta: ")
    return isim, yas, email


# --------------------------------------------
# Database'e bilgi ekleme fonksiyonu
# --------------------------------------------
def ekle(isim, yas, email, db):
    db[isim] = {"Yaş": yas, "E-posta": email}
    print(f"{isim} bilgileri database'e eklendi.")


# --------------------------------------------
# Database'den bilgi silme fonksiyonu
# --------------------------------------------
def sil(isim, db):
    if isim in db:
        del db[isim]
        print(f"{isim} bilgileri database'den silindi.")
    else:
        print(f"{isim} database'de bulunamadı.")


# --------------------------------------------
# Database'deki bilgileri güncelleme fonksiyonu
# --------------------------------------------
def guncelle(isim, db):
    if isim in db:
        print(f"{isim} bilgileri güncelleniyor.")
        yeni_yas = input("Yeni Yaş: ")
        yeni_email = input("Yeni E-posta: ")
        db[isim]["Yaş"] = yeni_yas
        db[isim]["E-posta"] = yeni_email
        print(f"{isim} bilgileri güncellendi.")
    else:
        print(f"{isim} database'de bulunamadı.")


# --------------------------------------------
# Database'deki bilgileri görüntüleme fonksiyonu
# --------------------------------------------
def goruntule(db):
    if not db:
        print("Database boş.")
    else:
        for isim, bilgiler in db.items():
            print(f"İsim: {isim}")
            for bilgi_adi, bilgi_degeri in bilgiler.items():
                print(f"{bilgi_adi}: {bilgi_degeri}")
            print("\n")


# --------------------------------------------
# Ana kod bloğu
# --------------------------------------------
database = {}

while True:
    print("\nNe yapmak istersin?")
    print("Ekle: e")
    print("Sil: s")
    print("Güncelle: g")
    print("Görüntüle: v")
    print("Çıkış: q")

    secim = input("Seçiminiz: ")

    if secim == "e":
        isim, yas, email = bilgi_gir()
        ekle(isim, yas, email, database)
    elif secim == "s":
        isim = input("Silinecek kişinin ismi: ")
        sil(isim, database)
    elif secim == "g":
        isim = input("Güncellenecek kişinin ismi: ")
        guncelle(isim, database)
    elif secim == "v":
        goruntule(database)
    elif secim == "q":
        break
    else:
        print("Geçersiz seçim. Lütfen tekrar deneyin.")
