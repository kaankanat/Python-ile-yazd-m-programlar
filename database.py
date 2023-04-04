import sqlite3

# Veritabanı bağlantısını oluşturalım
conn = sqlite3.connect('veriler.db')
c = conn.cursor()

# Veritabanı tablosunu oluşturalım
c.execute('''CREATE TABLE IF NOT EXISTS kisiler
             (isim TEXT, yas INT, email TEXT)''')

# Komutları sürekli olarak isteyelim
while True:
    print('-' * 30)
    print('Veri Tabanı Programı')
    print('-' * 30)
    print('1. Kişi Eklemek')
    print('2. Kişi Silmek')
    print('3. Kişiyi Güncellemek')
    print('4. Veri tabanını görüntülemek')
    print('q. Çıkış')

    # Kullanıcıdan komut alalım
    komut = input('Komut girin: ')

    # Çıkış işlemi
    if komut == 'q':
        print('Program sonlandırıldı.')
        break

    # Kişi ekleme işlemi
    elif komut == '1':
        isim = input('İsim: ')
        yas = int(input('Yaş: '))
        email = input('Email: ')
        # Eklenmek istenen kişi daha önceden veritabanında var mı kontrol ediyoruz
        c.execute("SELECT * FROM kisiler WHERE isim=?", (isim,))
        if c.fetchone() is not None:
            print('Bu isimde bir kişi zaten var.')
        else:
            c.execute("INSERT INTO kisiler VALUES (?, ?, ?)", (isim, yas, email))
            conn.commit()
            print('Kişi eklendi.')


    # Kişi silme işlemi
    elif komut == '2':
        isim = input('Silinecek kişinin ismi: ')
        c.execute("SELECT * FROM kisiler WHERE isim=?", (isim,))
        if c.fetchone() is None:
            print('Kişi bulunamadı.')
        else:
            c.execute("DELETE FROM kisiler WHERE isim=?", (isim,))
            conn.commit()
            print('Kişi silindi.')

    # Kişi güncelleme işlemi
    elif komut == '3':
        isim = input('Güncellenecek kişinin ismi: ')
        c.execute("SELECT * FROM kisiler WHERE isim=?", (isim,))
        if c.fetchone() is None:
            print('Kişi bulunamadı.')
        else:
            yeni_yas = int(input('Yeni yaş: '))
            yeni_email = input('Yeni email: ')
            c.execute("UPDATE kisiler SET yas=?, email=? WHERE isim=?",
                      (yeni_yas, yeni_email, isim))
            conn.commit()
            print('Kişi güncellendi.')


    # Veritabanını görüntüleme işlemi
    elif komut == '4':
        c.execute("SELECT * FROM kisiler")
        veriler = c.fetchall()
        if len(veriler) == 0:
            print('Veritabanı boş.')
        else:
            for veri in veriler:
                print(veri)

    # Geçersiz komut
    else:
        print('Geçersiz komut. Tekrar deneyin.')
