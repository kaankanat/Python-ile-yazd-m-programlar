import sqlite3

# Veritabanına bağlan
baglanti = sqlite3.connect('kisiler.db')

# Veritabanı yoksa oluştur
imlec = baglanti.cursor()
imlec.execute('''CREATE TABLE IF NOT EXISTS kisiler (isim TEXT, yas INTEGER, eposta TEXT)''')

# Ekleme işlemi için fonksiyon tanımla
def ekle(isim, yas, eposta):
    imlec.execute("INSERT INTO kisiler VALUES (?, ?, ?)", (isim, yas, eposta))
    baglanti.commit()

# Silme işlemi için fonksiyon tanımla
def sil(isim):
    imlec.execute("DELETE FROM kisiler WHERE isim=?", (isim,))
    baglanti.commit()

# Güncelleme işlemi için fonksiyon tanımla
def guncelle(isim, yas, eposta):
    imlec.execute("UPDATE kisiler SET yas=?, eposta=? WHERE isim=?", (yas, eposta, isim))
    baglanti.commit()

# Görüntüleme işlemi için fonksiyon tanımla
def goruntule():
    imlec.execute("SELECT * FROM kisiler")
    kisiler = imlec.fetchall()
    for kisi in kisiler:
        print("İsim: " + kisi[0] + ", Yaş: " + str(kisi[1]) + ", E-posta: " + kisi[2])

# Ana döngü
while True:
    print("\nYapmak istediğiniz işlemi seçin:")
    print("1- Kişi Ekle")
    print("2- Kişi Sil")
    print("3- Kişi Güncelle")
    print("4- Kişileri Görüntüle")
    print("q- Çıkış")

    secim = input("Seçiminiz: ")

    if secim == "1":
        isim = input("İsim: ")
        yas = int(input("Yaş: "))
        eposta = input("E-posta: ")
        ekle(isim, yas, eposta)
        print("-"*40)

    elif secim == "2":
        isim = input("Silmek istediğiniz kişinin adı: ")
        sil(isim)
        print("-"*40)

    elif secim == "3":
        isim = input("Güncellemek istediğiniz kişinin adı: ")
        yas = int(input("Yeni yaş: "))
        eposta = input("Yeni e-posta: ")
        guncelle(isim, yas, eposta)
        print("-"*40)

    elif secim == "4":
        goruntule()
        print("-"*40)

    elif secim == "q":
        break

    else:
        print("Geçersiz seçim. Lütfen devam edin.")
        print("-"*40)

# Bağlantıyı kapat
baglanti.close()
