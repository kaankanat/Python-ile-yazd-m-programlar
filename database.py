import sqlite3

# Veritabanı bağlantısı oluşturma
conn = sqlite3.connect('veritabani.db')

# Veritabanındaki tablo oluşturma
conn.execute('''CREATE TABLE IF NOT EXISTS kisiler
             (ID INTEGER PRIMARY KEY AUTOINCREMENT,
             ISIM TEXT NOT NULL,
             YAS INT NOT NULL,
             EMAIL TEXT NOT NULL);''')

while True:
    # Kullanıcıdan işlem seçimini alınması
    print("Veri Tabanı Programı")
    print("Kişi eklemek: 1")
    print("Kişi silmek: 2")
    print("Kişi güncellemek: 3")
    print("Veri tabanını görüntülemek: 4")
    print("Programdan çıkmak: q")
    secim = input("Yapmak istediğiniz işlemi seçin: ")

    # Veritabanına kişi eklemek
    if secim == "1":
        isim = input("Kişinin adını girin: ")
        yas = int(input("Kişinin yaşını girin: "))
        email = input("Kişinin e-posta adresini girin: ")
        conn.execute("INSERT INTO kisiler (ISIM, YAS, EMAIL) VALUES (?, ?, ?)", (isim, yas, email))
        conn.commit()
        print("Kişi başarıyla eklendi.")

    # Veritabanından kişi silmek
    elif secim == '2':
        if len(kisiler) == 0:
            print("Veri tabanı boş.")
        else:
            silinecek_isim = input("Silinecek kişinin ismi: ")
            bulundu = False
            for i in range(len(kisiler)):
                if kisiler[i]["isim"] == silinecek_isim:
                    bulundu = True
                    kisiler.pop(i)
                    print(f"{silinecek_isim} isimli kişi başarıyla silindi.")
                    break
            if not bulundu:
                print(f"{silinecek_isim} isimli kişi veri tabanında bulunamadı.")

    elif secim == '3':
        if len(kisiler) == 0:
            print("Veri tabanı boş.")
        else:
            guncellenecek_isim = input("Güncellenecek kişinin ismi: ")
            bulundu = False
            for i in range(len(kisiler)):
                if kisiler[i]["isim"] == guncellenecek_isim:
                    bulundu = True
                    yeni_isim = input("Yeni isim: ")
                    yeni_email = input("Yeni email: ")
                    yeni_yas = input("Yeni yaş: ")
                    kisiler[i] = {"isim": yeni_isim, "email": yeni_email, "yas": yeni_yas}
                    print("Kişi başarıyla güncellendi.")
                    break
            if not bulundu:
                print(f"{guncellenecek_isim} isimli kişi veri tabanında bulunamadı.")

    elif secim == '4':
        if len(kisiler) == 0:
            print("Veri tabanı boş.")
        else:
            print("Veri tabanındaki kişiler:")
            for kisi in kisiler:
                print(f"İsim: {kisi['isim']}, Email: {kisi['email']}, Yaş: {kisi['yas']}")

    elif secim == 'q':
        print("Programdan çıkılıyor...")
        break

    else:
        print("Geçersiz seçim. Lütfen tekrar deneyin.")

