import sqlite3


def kisi_ekle(isim, yas, eposta):
    with sqlite3.connect('database.db') as conn:
        cursor = conn.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS kisiler (isim TEXT, yas INT)')
        cursor.execute('INSERT INTO kisiler (isim, yas) VALUES (?, ?)', (isim, yas))
        conn.commit()
        print(f'{isim} adlı kişi veri tabanına eklendi.')


def kisi_sil(isim):
    with sqlite3.connect('database.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT COUNT(*) FROM kisiler WHERE isim = ?', (isim,))
        count = cursor.fetchone()[0]
        if count == 0:
            print(f'{isim} adlı kişi veri tabanında bulunamadı.')
        else:
            cursor.execute('DELETE FROM kisiler WHERE isim = ?', (isim,))
            conn.commit()
            print(f'{isim} adlı kişi veri tabanından silindi.')


def kisi_guncelle(isim, yas):
    with sqlite3.connect('database.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT COUNT(*) FROM kisiler WHERE isim = ?', (isim,))
        count = cursor.fetchone()[0]
        if count == 0:
            print(f'{isim} adlı kişi veri tabanında bulunamadı.')
        else:
            cursor.execute('UPDATE kisiler SET yas = ? WHERE isim = ?', (yas, isim))
            conn.commit()
            print(f'{isim} adlı kişinin yaşı {yas} olarak güncellendi.')


def veritabani_goruntule():
    with sqlite3.connect('database.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM kisiler')
        kisiler = cursor.fetchall()
        if not kisiler:
            print('Veri tabanında kayıt bulunmamaktadır.')
        else:
            for kisi in kisiler:
                print(f'{kisi[0]:<20} {kisi[1]:<10}')
                print('-' * 30)


def cizgi_ciz():
    print('-' * 30)


def program():
    while True:
        cizgi_ciz()
        print('Kullanıcı Ekle: 1')
        print('Kullanıcı Sil: 2')
        print('Kullanıcı Güncelle: 3')
        print('Veritabanını Görüntüle: 4')
        print('Çıkış: 5')
        cizgi_ciz()

        secim = input('Yapmak istediğiniz işlemi seçin (1-5): ')

        if secim == '1':
            isim = input('İsim: ')
            yas = int(input('Yaş: '))
            eposta = input('E-posta: ')
            kisi_ekle(isim, yas, eposta)
        elif secim == '2':
            isim = input('Silmek istediğiniz kişinin adını girin: ')
            kisi_sil(isim)
        elif secim == '3':
            isim = input('Güncellemek istediğiniz kişinin adı: ')
            yas = input('Yeni yaş: ')
            eposta = input('Yeni eposta: ')
            kisi_guncelle(isim, yas, eposta)
        elif secim == '4':
            veritabani_goruntule()
        elif secim == '5':
            break
        else:
            print('Geçersiz seçim.')
program()