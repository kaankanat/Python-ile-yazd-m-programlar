import sqlite3

conn = sqlite3.connect('database.db')
c = conn.cursor()

def tablo_olustur():
    c.execute('''CREATE TABLE IF NOT EXISTS kisiler
                 (isim TEXT, yas INT, email TEXT)''')

def ekle():
    isim = input("İsim: ")
    yas = input("Yaş: ")
    email = input("E-posta: ")
    c.execute("INSERT INTO kisiler (isim, yas, email) VALUES (?, ?, ?)", (isim, yas, email))
    conn.commit()
    print("Kişi başarıyla eklendi.")

def sil():
    isim = input("Silmek istediğiniz kişinin adını giriniz: ")
    c.execute("SELECT * FROM kisiler WHERE isim=?", (isim,))
    if not c.fetchall():
        print("Bu isimde bir kişi bulunamadı.")
        return
    c.execute("DELETE FROM kisiler WHERE isim=?", (isim,))
    conn.commit()
    print("Kişi başarıyla silindi.")

def guncelle():
    isim = input("Güncellemek istediğiniz kişinin adını giriniz: ")
    c.execute("SELECT * FROM kisiler WHERE isim=?", (isim,))
    if not c.fetchall():
        print("Bu isimde bir kişi bulunamadı.")
        return
    yas = input("Yeni yaş: ")
    email = input("Yeni e-posta: ")
    c.execute("UPDATE kisiler SET yas=?, email=? WHERE isim=?", (yas, email, isim))
    conn.commit()
    print("Kişi başarıyla güncellendi.")

def goruntule():
    c.execute("SELECT * FROM kisiler")
    rows = c.fetchall()
    if not rows:
        print("Veri tabanı boş.")
        return
    for row in rows:
        print("İsim: {}, Yaş: {}, E-posta: {}".format(row[0], row[1], row[2]))

def cikis():
    conn.close()
    print("Program sonlandırıldı.")
    exit()

tablo_olustur()

while True:
    print("\nVeri Tabanı Programı")
    print("1- Kişi Ekle")
    print("2- Kişi Sil")
    print("3- Kişi Güncelle")
    print("4- Kişileri Görüntüle")
    print("q- Çıkış")
    secim = input("Seçiminiz: ")
    if secim == "1":
        ekle()
    elif secim == "2":
        sil()
    elif secim == "3":
        guncelle()
    elif secim == "4":
        goruntule()
    elif secim == "q":
        cikis()
    else:
        print("Geçersiz seçim. Lütfen devam edin.")
