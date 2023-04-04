import sqlite3

with sqlite3.connect('database.db') as conn:
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS kisiler (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            isim TEXT NOT NULL,
            yas INTEGER NOT NULL,
            eposta TEXT
        )
    ''')


def kisi_ekle(isim, yas, eposta):
    with sqlite3.connect('database.db') as conn:
        cursor = conn.cursor()

        # Aynı isimde kayıt varsa ekleme
        cursor.execute('SELECT * FROM kisiler WHERE isim = ?', (isim,))
        if cursor.fetchone():
            print(f"{isim} isimli kayıt zaten var, ekleme yapılamadı.")
        else:
            cursor.execute('INSERT INTO kisiler (isim, yas, eposta) VALUES (?, ?, ?)', (isim, yas, eposta))
            print(f"{isim} isimli kişi veritabanına eklendi.")


def kisi_sil():
    with sqlite3.connect('database.db') as conn:
        cursor = conn.cursor()
        isim = input('Silinecek kişinin adını girin: ')
        cursor.execute('SELECT COUNT(*) FROM kisiler WHERE isim = ?', (isim,))
        count = cursor.fetchone()[0]
        if count == 0:
            print(f'{isim} adlı kişi veri tabanında bulunamadı.')
        else:
            cursor.execute('DELETE FROM kisiler WHERE isim = ?', (isim,))
            conn.commit()
            print(f'{isim} adlı kişi veri tabanından silindi.')


def kisi_guncelle():
    with sqlite3.connect('database.db') as conn:
        cursor = conn.cursor()
        isim = input('Güncellenecek kişinin adını girin: ')
        cursor.execute('SELECT * FROM kisiler WHERE isim=?', (isim,))
        kisi = cursor.fetchone()
        if kisi is None:
            print("Kişi bulunamadı!")
            return
        print('Güncel bilgiler:')
        print('İsim:', kisi[1])
        print('Yaş:', kisi[2])
        print('Eposta:', kisi[3])
        yeni_yas = input('Yeni yaşınızı girin (mevcut: {}): '.format(kisi[2]))
        yeni_eposta = input('Yeni e-posta adresinizi girin (mevcut: {}): '.format(kisi[3]))
        cursor.execute('UPDATE kisiler SET yas=?, eposta=? WHERE isim=?', (yeni_yas, yeni_eposta, isim))
        print('Kişi başarıyla güncellendi!')
        conn.commit()

def veritabani_goruntule():
    with sqlite3.connect('database.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM kisiler')
        kisiler = cursor.fetchall()
        if not kisiler:
            print('Veri tabanında kayıt bulunmamaktadır.')
        else:
            print(f"{'İsim':<20} {'Yaş':<10} {'Eposta':<30}")
            print('-' * 60)
            for kisi in kisiler:
                print(f"{kisi[1]:<20} {kisi[2]:<10} {kisi[3]:<30}")
                print('-' * 60)

def cizgi_ciz():
    print('-' * 30)


def program():
    while True:
        cizgi_ciz()
        print('Kullanıcı Ekle: 1')
        print('Kullanıcı Sil: 2')
        print('Kullanıcı Güncelle: 3')
        print('Veritabanını Görüntüle: 4')
        print('Çıkış: q')
        cizgi_ciz()

        secim = input('Yapmak istediğiniz işlemi seçin: ')
        if secim == '1':
            isim = input('İsim: ')
            yas = input('Yaş: ')
            eposta = input('E-posta: ')
            kisi_ekle(isim, eposta, yas)
        elif secim == '2':
            kisi_sil()
        elif secim == '3':
            kisi_guncelle()
        elif secim == '4':
            veritabani_goruntule()
        elif secim == 'q':
            print('Program sonlandırılıyor.')
            break
        else:
            print('Geçersiz seçim. Lütfen tekrar deneyin.')
program()