import sqlite3

def veritabani_olustur():
    conn = sqlite3.connect('kisiler.db')
    cursor = conn.cursor()

    cursor.execute(
        'CREATE TABLE IF NOT EXISTS kisiler (id INTEGER PRIMARY KEY AUTOINCREMENT, isim TEXT, yas INTEGER, eposta TEXT)')

    conn.commit()
    conn.close()


def kisi_ekle(isim, yas, eposta):
    conn = sqlite3.connect('kisiler.db')
    cursor = conn.cursor()

    cursor.execute('INSERT INTO kisiler (isim, yas, eposta) VALUES (?, ?, ?)', (isim, yas, eposta))

    conn.commit()
    conn.close()


def kisi_sil(isim):
    conn = sqlite3.connect('kisiler.db')
    cursor = conn.cursor()

    cursor.execute('DELETE FROM kisiler WHERE isim = ?', (isim,))

    conn.commit()
    conn.close()


def kisi_guncelle(eski_isim, yeni_isim, yeni_yas, yeni_eposta):
    conn = sqlite3.connect('kisiler.db')
    cursor = conn.cursor()

    cursor.execute('UPDATE kisiler SET isim = ?, yas = ?, eposta = ? WHERE isim = ?',
                   (yeni_isim, yeni_yas, yeni_eposta, eski_isim))

    conn.commit()
    conn.close()


def veritabani_goruntule():
    conn = sqlite3.connect('kisiler.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM kisiler')

    for row in cursor.fetchall():
        print(row)

    conn.close()


def program():
    veritabani_olustur()

    while True:
        print("Lütfen seçiminizi yapın:")
        print("1. Veri tabanına kişi ekle")
        print("2. Veri tabanından kişi sil")
        print("3. Veri tabanındaki kişiyi güncelle")
        print("4. Veri tabanını görüntüle")
        print("q. Çıkış yap")
        print("--------------------------")
        secim = input("Seçiminiz: ")

        if secim == "1":
            isim = input("İsim: ")
            yas = int(input("Yaş: "))
            eposta = input("Eposta: ")
            kisi_ekle(isim, yas, eposta)
            print("Kişi başarıyla eklendi.")
            print("--------------------------")
        elif secim == "2":
            isim = input("Silinecek kişinin ismi: ")
            kisi_sil(isim)
            print("Kişi başarıyla silindi.")
            print("--------------------------")
        elif secim == "3":
            eski_isim = input("Güncellenecek kişinin eski ismi: ")
            yeni_isim = input("Yeni isim: ")
            yeni_yas = int(input("Yeni yaş: "))
            yeni_eposta = input("Yeni eposta: ")
            kisi_guncelle(eski_isim, yeni_isim, yeni_yas, yeni_eposta)
            print("Kişi başarıyla güncellendi.")
            print("--------------------------")
        elif secim == "4":
            veritabani_goruntule()
            print("--------------------------")
        elif secim == "q":
            print("Program sonlandırılıyor...")
            return  # burada fonksiyondan çıkıyoruz, bu sayede program sonlanacak
        else:
            print("Geçersiz seçim, lütfen tekrar deneyin.")
            print("--------------------------")
def main():
    veritabani_olustur()
    program()

if __name__ == "__main__":
    main()
