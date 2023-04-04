import sqlite3

def veri_ekle():
    isim = input("İsim: ")
    email = input("E-posta: ")
    yas = input("Yaş: ")
    cursor.execute("INSERT INTO kisiler (isim, email, yas) VALUES (?, ?, ?)", (isim, email, yas))
    conn.commit()
    print("Kişi başarıyla eklendi.")

def veri_sil():
    isim = input("Silmek istediğiniz kişinin ismini girin: ")
    cursor.execute("SELECT * FROM kisiler WHERE isim=?", (isim,))
    row = cursor.fetchone()
    if row is None:
        print("Böyle bir kişi bulunamadı.")
    else:
        cursor.execute("DELETE FROM kisiler WHERE isim=?", (isim,))
        conn.commit()
        print("Kişi başarıyla silindi.")

def veri_guncelle():
    isim = input("Güncellemek istediğiniz kişinin ismini girin: ")
    cursor.execute("SELECT * FROM kisiler WHERE isim=?", (isim,))
    row = cursor.fetchone()
    if row is None:
        print("Böyle bir kişi bulunamadı.")
    else:
        email = input("Yeni e-posta adresi: ")
        yas = input("Yeni yaş: ")
        cursor.execute("UPDATE kisiler SET email=?, yas=? WHERE isim=?", (email, yas, isim))
        conn.commit()
        print("Kişi başarıyla güncellendi.")

def veri_goruntule():
    cursor.execute("SELECT * FROM kisiler")
    rows = cursor.fetchall()
    if len(rows) == 0:
        print("Veri tabanı boş.")
    else:
        for row in rows:
            print(f"{row[0]} - {row[1]} - {row[2]}")

# Veri tabanı bağlantısı oluştur
conn = sqlite3.connect("kisiler.db")

# Cursor oluştur
cursor = conn.cursor()

# Tablo oluştur
cursor.execute("""
    CREATE TABLE IF NOT EXISTS kisiler (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        isim TEXT NOT NULL,
        email TEXT NOT NULL,
        yas INT NOT NULL
    )
""")

# Menüyü göster
while True:
    print("Veri Tabanı Programı")
    print("1 - Veri tabanına kişi eklemek")
    print("2 - Veri tabanından kişi silmek")
    print("3 - Veri tabanındaki kişiyi güncellemek")
    print("4 - Veri tabanını görüntülemek")
    print("q - Veri tabanından çıkmak")
    secim = input("Seçiminiz: ")

    if secim == "1":
        veri_ekle()
    elif secim == "2":
        veri_sil()
    elif secim == "3":
        veri_guncelle()
    elif secim == "4":
        veri_goruntule()
    elif secim == "q":
        break
    else:
        print("Geçersiz seçim. Lütfen tekrar deneyin.")

# Veri tabanı bağlantısını kapat
conn.close()
