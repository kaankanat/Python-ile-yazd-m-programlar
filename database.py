import sqlite3

conn = sqlite3.connect("example.db")
c = conn.cursor()

# tablo oluşturma
c.execute('''CREATE TABLE IF NOT EXISTS users
             (name TEXT, email TEXT, age INT)''')

while True:
    # işlem seçimi
    islem = input("Hangi işlemi yapmak istersiniz? (Ekle/Çıkar/Güncelle/Görüntüle/Kapat): ")

    if islem.lower() == "ekle":
        # kullanıcı bilgileri alma
        name = input("İsim: ")
        email = input("E-mail: ")
        age = int(input("Yaş: "))

        # kullanıcı ekleme
        c.execute("INSERT INTO users VALUES (?, ?, ?)", (name, email, age))
        conn.commit()

        print("-"*30)

    elif islem.lower() == "çıkar":
        # kullanıcı bilgileri alma
        name = input("Silmek istediğiniz kullanıcının ismini girin: ")

        # kullanıcı silme
        c.execute("DELETE FROM users WHERE name=?", (name,))
        conn.commit()

        print("-"*30)

    elif islem.lower() == "güncelle":
        # kullanıcı bilgileri alma
        name = input("Güncellemek istediğiniz kullanıcının ismini girin: ")
        new_email = input("Yeni e-mail: ")
        new_age = int(input("Yeni yaş: "))

        # kullanıcı güncelleme
        c.execute("UPDATE users SET email=?, age=? WHERE name=?", (new_email, new_age, name))
        conn.commit()

        print("-"*30)

    elif islem.lower() == "görüntüle":
        # veri tabanındaki tüm kullanıcıları görüntüleme
        c.execute("SELECT * FROM users")
        rows = c.fetchall()

        if rows:
            for row in rows:
                print(row)
        else:
            print("Veri tabanı şu anda boş.")

        print("-"*30)

    elif islem.lower() == "kapat":
        # veri tabanı bağlantısını kapatma
        conn.close()
        break

    else:
        print("Geçersiz işlem, tekrar deneyin.")

        print("-"*30)
