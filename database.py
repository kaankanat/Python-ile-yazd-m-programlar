import sqlite3

# veritabanı bağlantısı oluşturma
baglanti = sqlite3.connect('veritabani.db')

# tablo oluşturma (eğer daha önce oluşturulmadıysa)
baglanti.execute('''CREATE TABLE IF NOT EXISTS kullanicilar
             (ID INTEGER PRIMARY KEY AUTOINCREMENT,
             isim TEXT NOT NULL,
             email TEXT NOT NULL,
             yas INT NOT NULL);''')

# kullanıcı seçimi
while True:
    secim = input("Yapmak istediğiniz işlemi seçin (ekle, güncelle, sil): ")
    if secim.lower() not in ['ekle', 'güncelle', 'sil']:
        print("Geçersiz işlem, tekrar deneyin.")
    else:
        break

# kullanıcı bilgileri alma
isim = input("İsim: ")
email = input("E-posta: ")
yas = int(input("Yaş: "))

# işleme göre veritabanında değişiklik yapma
if secim.lower() == 'ekle':
    baglanti.execute("INSERT INTO kullanicilar (isim, email, yas) VALUES (?, ?, ?);", (isim, email, yas))
    print("Kullanıcı başarıyla eklendi.")
elif secim.lower() == 'güncelle':
    baglanti.execute("UPDATE kullanicilar SET email = ?, yas = ? WHERE isim = ?;", (email, yas, isim))
    print("Kullanıcı bilgileri başarıyla güncellendi.")
elif secim.lower() == 'sil':
    baglanti.execute("DELETE FROM kullanicilar WHERE isim = ?;", (isim,))
    print("Kullanıcı başarıyla silindi.")

# veritabanını kaydetme ve bağlantıyı kapama
baglanti.commit()
baglanti.close()
