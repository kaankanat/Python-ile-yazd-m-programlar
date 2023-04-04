import sqlite3

def create_connection():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    return conn, cursor

def create_table(cursor):
    cursor.execute("""CREATE TABLE IF NOT EXISTS kisiler (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      isim TEXT NOT NULL,
                      email TEXT NOT NULL,
                      yas INTEGER NOT NULL)""")
    print("Tablo oluşturuldu")

def insert_data(conn, cursor, isim, email, yas):
    cursor.execute("INSERT INTO kisiler (isim, email, yas) VALUES (?, ?, ?)", (isim, email, yas))
    conn.commit()
    print(f"{isim} veritabanına eklendi")

def update_data(conn, cursor, id, isim, email, yas):
    cursor.execute("UPDATE kisiler SET isim=?, email=?, yas=? WHERE id=?", (isim, email, yas, id))
    conn.commit()
    print(f"{isim} güncellendi")

def delete_data(conn, cursor, id):
    cursor.execute("DELETE FROM kisiler WHERE id=?", (id,))
    conn.commit()
    print(f"{id} numaralı kişi silindi")

def display_data(cursor):
    cursor.execute("SELECT * FROM kisiler")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

def main():
    conn, cursor = create_connection()
    create_table(cursor)
    while True:
        print("İşlem Seçin:")
        print("1 - Kişi Ekle")
        print("2 - Kişi Güncelle")
        print("3 - Kişi Sil")
        print("4 - Verileri Görüntüle")
        print("q - Çıkış")
        selection = input("Seçiminiz: ")

        if selection == "1":
            isim = input("İsim: ")
            email = input("Email: ")
            yas = input("Yaş: ")
            insert_data(conn, cursor, isim, email, yas)
        elif selection == "2":
            id = input("Güncellemek istediğiniz kişinin id'si: ")
            isim = input("Yeni isim: ")
            email = input("Yeni email: ")
            yas = input("Yeni yaş: ")
            update_data(conn, cursor, id, isim, email, yas)
        elif selection == "3":
            id = input("Silmek istediğiniz kişinin id'si: ")
            delete_data(conn, cursor, id)
        elif selection == "4":
            display_data(cursor)
        elif selection == "q":
            break
        else:
            print("Geçersiz seçim")


    conn.close()

if __name__ == "__main__":
    main()
