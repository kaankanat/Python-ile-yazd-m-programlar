import sqlite3

con = sqlite3.connect('veritabani.db')
cursor = con.cursor()

# kisiler tablosu oluşturuluyor 
cursor.execute('''CREATE TABLE IF NOT EXISTS kisiler
                    (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                    isim TEXT NOT NULL, 
                    yas INTEGER NOT NULL, 
                    email TEXT NOT NULL)''')
con.commit()

# yararlı fonksiyonlar tanımlanıyor
def kisi_ekle():
    print("-" * 50)
    isim = input("İsim: ")
    yas = int(input("Yaş: "))
    email = input("E-mail: ")
    cursor.execute(f"INSERT INTO kisiler (isim, yas, email) VALUES ('{isim}',{yas},'{email}')")
    con.commit()
    print(f"{isim} isimli kişi veri tabanına eklendi.")

def kisi_sil():
    print("-" * 50)
    isim = input("Silmek istediğiniz kişinin İsmi: ")
    cursor.execute(f"SELECT * FROM kisiler WHERE isim = '{isim}'")
    row = cursor.fetchone()
    if row:
        cursor.execute(f"DELETE FROM kisiler WHERE isim='{isim}'")
        con.commit()
        print(f"{isim} isimli kişi veri tabanından silindi.")
    else:
        print(f"{isim} isimli kişi veri tabanında bulunamadı.")

def kisi_guncelle():
    print("-" * 50)
    isim = input("Güncellemek istediğiniz kişinin İsmi: ")
    cursor.execute(f"SELECT * FROM kisiler WHERE isim = '{isim}'")
    row = cursor.fetchone()
    if row:
        yas = input("Yeni Yaş: ")
        email = input("Yeni E-mail: ")
        cursor.execute(f"UPDATE kisiler SET yas = '{yas}', email = '{email}' WHERE isim='{isim}'")
        con.commit()
        print(f"{isim} isimli kişi başarıyla güncellendi.")
    else:
        print(f"{isim} isimli kişi veri tabanında bulunamadı.")

def veritabani_goruntule():
    print("-" * 50)
    cursor.execute("SELECT isim, yas, email FROM kisiler")
    rows = cursor.fetchall()
    if rows:
        for row in rows:
            print(row[0], row[1], row[2])
    else:
        print("Veri tabanında kayıt bulunmamaktadır.")

while True:
    print("Veri Tabanı Programı")
    print("-" * 50)
    print("Kullanılabilir Fonksiyonlar:")
    print("1. Yeni Kişi Ekle")
    print("2. Kişi Sil")
    print("3. Kişi Bilgilerini Güncelle")
    print("4. Veri Tabanındaki Kayıtları Görüntüle")
    print("q. Çıkış Yap")

    secim = input("Lütfen bir seçenek seçiniz (1/2/3/4/q): ")

    if secim == "1":
        kisi_ekle()
    elif secim == "2":
        kisi_sil()
    elif secim == "3":
        kisi_guncelle()
    elif secim == "4":
        veritabani_goruntule()
    elif secim == "q":
        break
    else:
        print("Geçersiz Seçim!")
