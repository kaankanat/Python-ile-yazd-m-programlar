# veritabanı listesi
database = []

while True:
    print("\n" + "-" * 30)
    print("Veritabanı İşlemleri".center(30))
    print("-" * 30)
    print("1. Ekle")
    print("2. Güncelle")
    print("3. Sil")
    print("4. Görüntüle")
    print("5. Çıkış")

    choice = input("Yapmak istediğiniz işlemi seçin: ")

    if choice == "1":
        name = input("İsim girin: ")
        email = input("Email girin: ")
        age = input("Yaş girin: ")

        # yeni veri
        new_data = {"isim": name, "email": email, "yaş": age}
        database.append(new_data)
        print("\nİşlem başarılı: Veritabanına yeni veri eklendi.")

    elif choice == "2":
        name = input("Güncellemek istediğiniz kişinin adını girin: ")
        for data in database:
            if data["isim"] == name:
                email = input("Yeni email girin: ")
                age = input("Yeni yaş girin: ")
                data["email"] = email
                data["yaş"] = age
                print("\nİşlem başarılı: Veritabanındaki veri güncellendi.")
                break
        else:
            print("\nHata: Girilen isim veritabanında bulunamadı.")

    elif choice == "3":
        name = input("Silmek istediğiniz kişinin adını girin: ")
        for data in database:
            if data["isim"] == name:
                database.remove(data)
                print("\nİşlem başarılı: Veritabanından veri silindi.")
                break
        else:
            print("\nHata: Girilen isim veritabanında bulunamadı.")

    elif choice == "4":
        print("\nVeritabanı Listesi:")
        print("-" * 30)
        for data in database:
            print("İsim: {}\nEmail: {}\nYaş: {}\n".format(data["isim"], data["email"], data["yaş"]))

    elif choice == "5":
        print("\nProgram kapatılıyor...")
        break

    else:
        print("\nHatalı seçim! Lütfen geçerli bir seçenek girin.")
