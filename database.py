import sqlite3

conn = sqlite3.connect('database.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS kullanicilar
            (id INTEGER PRIMARY KEY AUTOINCREMENT,
            isim TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            yas INTEGER NOT NULL)''')

while True:
    print("1. Ekleme\n2. Silme\n3. Güncelleme\n4. Görüntüleme\n5. Çıkış\n")
    secim = input("Yapmak istediğiniz işlemi seçiniz: ")

    if secim == "1":
        isim = input("İsim: ")
        email = input("Email: ")
        yas = int(input("Yaş: "))
        c.execute("INSERT INTO kullanicilar (isim, email, yas) VALUES (?, ?, ?)", (isim, email, yas))
        print("Kullanıcı eklendi.\n" + "-" * 50)

    elif secim == "2":
        isim = input("Silmek istediğiniz kullanıcının ismini giriniz: ")
        c.execute("SELECT * FROM kullanicilar WHERE isim=?", (isim,))
        result = c.fetchone()
        if result:
            c.execute("DELETE FROM kullanicilar WHERE isim=?", (isim,))
            print("Kullanıcı silindi.\n" + "-" * 50)
        else:
            print("Bu isim sistemde bulunamamıştır.\n" + "-" * 50)

    elif secim == "3":
        isim = input("Güncellemek istediğiniz kullanıcının ismini giriniz: ")
        c.execute("SELECT * FROM kullanicilar WHERE isim=?", (isim,))
        result = c.fetchone()
        if result:
            email = input("Yeni Email: ")
            yas = int(input("Yeni Yaş: "))
            c.execute("UPDATE kullanicilar SET email=?, yas=? WHERE isim=?", (email, yas, isim))
            print("Kullanıcı güncellendi.\n" + "-" * 50)
        else:
            print("Bu isim sistemde bulunamamıştır.\n" + "-" * 50)

    elif secim == "4":
        c.execute("SELECT * FROM kullanicilar")
        result = c.fetchall()
        if result:
            for row in result:
                print("ID:", row[0])
                print("İsim:", row[1])
                print("Email:", row[2])
                print("Yaş:", row[3])
                print("-" * 50)
        else:
            print("Veri tabanı şu anda boş.\n" + "-" * 50)

    elif secim == "5":
        print("Çıkış yapılıyor...")
        break

    else:
        print("Lütfen geçerli bir seçenek giriniz.\n" + "-" * 50)

conn.commit()
conn.close()
