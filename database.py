# Veri Tabanı Programı

database = []

while True:
    print("--------------------")
    print("Veri tabanına kişi eklemek: 1")
    print("Veri tabandan kişi silmek: 2")
    print("Veri tabanındaki kişiyi güncellemek: 3")
    print("Veri tabanını görüntülemek: 4")
    print("Veri tabanından çıkmak: q")
    print("--------------------")

    # Kullanıcıdan seçim yapmasını istiyoruz
    secim = input("Yapmak istediğiniz işlemin numarasını girin: ")

    # Seçime göre ilgili işlem yapılıyor
    if secim == "1":
        # Yeni kişi ekleme
        print("Yeni kişi ekleyin:")
        isim = input("İsim: ")
        yas = input("Yaş: ")
        email = input("E-posta: ")
        database.append({"isim": isim, "yas": yas, "email": email})
        print("Kişi veri tabanına eklendi.")

    elif secim == "2":
        # Kişi silme
        if len(database) == 0:
            print("Veri tabanı boş.")
            continue
        isim = input("Silmek istediğiniz kişinin adını girin: ")
        bulundu = False
        for kisi in database:
            if kisi["isim"] == isim:
                database.remove(kisi)
                bulundu = True
                print("Kişi veri tabanından silindi.")
                break
        if not bulundu:
            print("Bu isimde bir kişi veri tabanında yok.")

    elif secim == "3":
        # Kişi güncelleme
        if len(database) == 0:
            print("Veri tabanı boş.")
            continue
        isim = input("Güncellemek istediğiniz kişinin adını girin: ")
        bulundu = False
        for kisi in database:
            if kisi["isim"] == isim:
                yeni_isim = input("Yeni isim: ")
                yeni_yas = input("Yeni yaş: ")
                yeni_email = input("Yeni e-posta: ")
                kisi["isim"] = yeni_isim
                kisi["yas"] = yeni_yas
                kisi["email"] = yeni_email
                bulundu = True
                print("Kişi veri tabanında güncellendi.")
                break
        if not bulundu:
            print("Bu isimde bir kişi veri tabanında yok.")

    elif secim == "4":
        # Veri tabanını görüntüleme
        if len(database) == 0:
            print("Veri tabanı boş.")
            continue
        for kisi in database:
            print(f"İsim: {kisi['isim']}, Yaş: {kisi['yas']}, E-posta: {kisi['email']}")

    elif secim == "q":
        # Çıkış
        print("Program sonlandırılıyor.")
        break

    else:
        print("Geçersiz seçim.")
