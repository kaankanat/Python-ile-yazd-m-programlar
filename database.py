import sqlite3

# Veritabanı bağlantısını oluşturalım veya var olanı açalım
conn = sqlite3.connect('adres_defteri.db')

# Veritabanı tablosunu oluşturalım
conn.execute('''CREATE TABLE IF NOT EXISTS kisiler
            (ID INTEGER PRIMARY KEY AUTOINCREMENT,
            AD TEXT NOT NULL,
            SOYAD TEXT NOT NULL,
            EMAIL TEXT NOT NULL,
            TELEFON TEXT NOT NULL);''')

# Veritabanındaki kayıtları listeleme fonksiyonu
def kisileri_goruntule():
    cursor = conn.execute("SELECT * from kisiler")
    kisiler = cursor.fetchall()
    if len(kisiler) == 0:
        print("Veritabanı şu anda boş.")
    else:
        print("{:<5} {:<15} {:<15} {:<25} {:<15}".format("ID", "Ad", "Soyad", "E-mail", "Telefon"))
        print("------------------------------------------------------------")
        for row in kisiler:
            print("{:<5} {:<15} {:<15} {:<25} {:<15}".format(row[0], row[1], row[2], row[3], row[4]))
        print("------------------------------------------------------------")

# Veritabanına yeni kişi ekleme fonksiyonu
def kisi_ekle():
    ad = input("Ad giriniz: ")
    soyad = input("Soyad giriniz: ")
    email = input("E-mail giriniz: ")
    telefon = input("Telefon giriniz: ")
    conn.execute("INSERT INTO kisiler (AD, SOYAD, EMAIL, TELEFON) VALUES (?, ?, ?, ?)", (ad, soyad, email, telefon))
    conn.commit()
    print("Kişi başarıyla eklendi.")

# Veritabanındaki bir kişiyi güncelleme fonksiyonu
def kisi_guncelle():
    kisi_id = input("Güncellenecek kişinin ID numarasını girin: ")
    cursor = conn.execute("SELECT * from kisiler WHERE ID=?", (kisi_id,))
    kisi = cursor.fetchone()
    if kisi is None:
        print("Bu ID numarasına sahip bir kişi bulunamadı.")
    else:
        print("Güncellenecek kişi: ", kisi[1], kisi[2])
        yeni_ad = input("Yeni ad: ")
        yeni_soyad = input("Yeni soyad: ")
        yeni_email = input("Yeni e-mail: ")
        yeni_telefon = input("Yeni telefon: ")
        conn.execute("UPDATE kisiler SET AD=?, SOYAD=?, EMAIL=?, TELEFON=? WHERE ID=?", (yeni_ad, yeni_soyad, yeni_email, yeni_telefon, kisi_id))
        conn.commit()
        print("Kişi başarıyla güncellendi.")

# Veritabanından bir kişiyi silme fonksiyonu
def kisi_sil():
    kisi_id = input("Silinecek kişinin ID numarasını girin: ")
    cursor = conn.execute("SELECT * from kisiler WHERE ID=?", (kisi_id,))
    kisi = cursor.fetchone()
    if kisi is None:
        print("Bu ID numarasına sahip bir kişi bulunamadı.")
if secim == 1:
    ad = input("İsim: ").capitalize()
    email = input("Email: ").lower()
    yas = input("Yaş: ")
    cur.execute("INSERT INTO kisiler (isim, email, yas) VALUES (?, ?, ?)", (ad, email, yas))
    conn.commit()
    print("\nBaşarıyla eklendi.\n" + "-"*30)
elif secim == 2:
    silinecek_id = input("Silinecek kişinin ID numarasını girin: ")
    cur.execute("SELECT * FROM kisiler WHERE id=?", (silinecek_id,))
    if cur.fetchone() is None:
        print("Bu ID numarasına sahip bir kişi bulunamadı. Lütfen devam edin.\n" + "-"*30)
        continue
    else:
        cur.execute("DELETE FROM kisiler WHERE id=?", (silinecek_id,))
        conn.commit()
        print("\nBaşarıyla silindi.\n" + "-"*30)
elif secim == 3:
    guncellenecek_id = input("Güncellenecek kişinin ID numarasını girin: ")
    cur.execute("SELECT * FROM kisiler WHERE id=?", (guncellenecek_id,))
    if cur.fetchone() is None:
        print("Bu ID numarasına sahip bir kişi bulunamadı. Lütfen devam edin.\n" + "-"*30)
        continue
    else:
        yeni_ad = input("Yeni isim: ").capitalize()
        yeni_email = input("Yeni email: ").lower()
        yeni_yas = input("Yeni yaş: ")
        cur.execute("UPDATE kisiler SET isim=?, email=?, yas=? WHERE id=?", (yeni_ad, yeni_email, yeni_yas, guncellenecek_id))
        conn.commit()
        print("\nBaşarıyla güncellendi.\n" + "-"*30)
elif secim == 4:
    cur.execute("SELECT * FROM kisiler")
    rows = cur.fetchall()
    if not rows:
        print("Veri tabanı şu anda boş.\n" + "-"*30)
    else:
        print("ID  İsim           Email                 Yaş")
        print("-"*45)
        for row in rows:
            print("{}   {}   {}   {}".format(row[0], row[1].capitalize(), row[2], row[3]))
        print("-"*45)
else:
    print("Geçersiz seçim. Lütfen tekrar deneyin.\n" + "-"*30)

