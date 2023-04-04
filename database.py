import sqlite3

conn = sqlite3.connect('database.db')
c = conn.cursor()

c.execute('''
          CREATE TABLE IF NOT EXISTS kullanici
          (isim TEXT, email TEXT, yas INTEGER)
          ''')

print("Kullanici veritabanina baglandi...")

while True:
    print(
        "\nLutfen yapmak istediginiz islemi secin:\n1. Kullanici ekleme\n2. Kullanici silme\n3. Kullanici guncelleme\n4. Kullanici goruntuleme\n5. Cikis")
    secim = input("Seciminiz: ")

    if secim == "1":
        isim = input("Isim: ").lower()
        email = input("Email: ").lower()
        yas = int(input("Yas: "))
        c.execute('INSERT INTO kullanici VALUES (?, ?, ?)', (isim, email, yas))
        conn.commit()
        print("\nKullanici basariyla eklendi.")

    elif secim == "2":
        isim = input("Silmek istediginiz kullanici ismi: ").lower()
        c.execute('SELECT * FROM kullanici WHERE isim = ?', (isim,))
        data = c.fetchall()
        if len(data) == 0:
            print("\nBu isim sistemde bulunamamistir.")
        else:
            c.execute('DELETE FROM kullanici WHERE isim = ?', (isim,))
            conn.commit()
            print("\nKullanici basariyla silindi.")

    elif secim == "3":
        isim = input("Guncellemek istediginiz kullanici ismi: ").lower()
        c.execute('SELECT * FROM kullanici WHERE isim = ?', (isim,))
        data = c.fetchall()
        if len(data) == 0:
            print("\nBu isim sistemde bulunamamistir.")
        else:
            print("\nMevcut bilgiler:")
            for row in data:
                print("Isim:", row[0])
                print("Email:", row[1])
                print("Yas:", row[2])
            yeni_isim = input("Yeni isim: ").lower()
            yeni_email = input("Yeni email: ").lower()
            yeni_yas = int(input("Yeni yas: "))
            c.execute('UPDATE kullanici SET isim = ?, email = ?, yas = ? WHERE isim = ?',
                      (yeni_isim, yeni_email, yeni_yas, isim))
            conn.commit()
            print("\nKullanici basariyla guncellendi.")

    elif secim == "4":
        c.execute('SELECT * FROM kullanici')
        data = c.fetchall()
        if len(data) == 0:
            print("\nVeri tabani su anda bos.")
        else:
            print("\nKullanici bilgileri:")
            for row in data:
                print("Isim:", row[0])
                print("Email:", row[1])
                print("Yas:", row[2])

    elif secim == "5":
        print("Program kapatiliyor...")
        break

    else:
        print("Gecersiz secim. Lutfen tekrar deneyin.")

conn.close
