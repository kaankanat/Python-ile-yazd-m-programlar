def main():
    while True:
        print("Veri Tabanı Programı")
        print("Veri tabanına kişi eklemek: 1")
        print("Veri tabandan kişi silmek: 2")
        print("Veri tabanındaki kişiyi güncellemek: 3")
        print("Veri tabanını görüntülemek: 4")
        print("Veri tabanından çıkmak: q")

        secim = input("Yapmak istediğiniz işlemi seçin: ")

        if secim == "1":
            isim = input("Kişinin adını girin: ")
            yas = input("Kişinin yaşını girin: ")
            email = input("Kişinin e-posta adresini girin: ")
            ekle(isim, yas, email)

        elif secim == "2":
            isim = input("Silinecek kişinin adını girin: ")
            sil(isim)

        elif secim == "3":
            isim = input("Güncellenecek kişinin adını girin: ")
            yeni_isim = input("Yeni adı girin (boş bırakmak için enter'a basın): ")
            yeni_yas = input("Yeni yaşını girin (boş bırakmak için enter'a basın): ")
            yeni_email = input("Yeni e-posta adresini girin (boş bırakmak için enter'a basın): ")
            guncelle(isim, yeni_isim, yeni_yas, yeni_email)

        elif secim == "4":
            goruntule()

        elif secim.lower() == "q":
            break

        else:
            print("Geçersiz seçim. Lütfen tekrar deneyin.")
