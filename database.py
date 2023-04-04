import sqlite3

conn = sqlite3.connect('veritabani.db')
c = conn.cursor()

while True:
    print("="*50)
    print("VERİTABANI İŞLEMLERİ\n1- Ekleme\n2- Güncelleme\n3- Silme\n4- Görüntüleme\n5- Çıkış")
    islem = input("Hangi işlemi yapmak istersiniz? ")

    if islem == '1':
        print("="*50)
        ad = input("Adınız: ")
        email = input("E-posta adresiniz: ")
        yas = input("Yaşınız: ")

        c.execute("INSERT INTO kullanicilar VALUES (?, ?, ?)", (ad, email, yas))
        conn.commit()
        print("Kullanıcı eklendi.")

    elif islem == '2':
        print("="*50)
        ad = input("Güncellemek istediğiniz kullanıcının adı: ")
        email = input("E-posta adresiniz: ")
        yas = input("Yaşınız: ")

        c.execute("UPDATE kullanicilar SET email = ?, yas = ? WHERE ad = ?", (email, yas, ad))
        conn.commit()
        print("Kullanıcı güncellendi.")

    elif islem == '3':
        print("="*50)
        ad = input("Silmek istediğiniz kullanıcının adı: ")

        c.execute("DELETE FROM kullanicilar WHERE ad = ?", (ad,))
        conn.commit()
        print("Kullanıcı silindi.")

    elif islem == '4':
        print("="*50)
        c.execute("SELECT * FROM kullanicilar")
        kullanici_listesi = c.fetchall()

        for kullanici in kullanici_listesi:
            print(kullanici)

    elif islem == '5':
        break

    else:
        print("Geçersiz işlem. Lütfen tekrar deneyin.")

c.close()
conn.close()
