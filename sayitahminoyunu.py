import time
import random
print("""
*******************************
Sayı Tahmin Oyunu

* Sayı 1 İle 100 Arasındadır.
* 7 Hakkınız Var.

* Programdan Çıkmak İçin 0 Tuşuna Basınız.
*******************************
""")
tahminhakkı = 7
b = random.randint(1, 101)
while True:
    a = int(input("1-100 Arasında Bir Sayı Giriniz:"))
    if a == 0:
        break
    elif a<b:
        print("Hesaplanıyor...")
        time.sleep(1)
        tahminhakkı -= 1
        print("Girdiğiniz Sayı Küçük. Lütfen {}'den Büyük Bir Sayı Giriniz. Kalan Tahmin Hakkınız: {}".format(a,tahminhakkı))

    elif a>b:
        print("Hesaplanıyor...")
        time.sleep(1)
        tahminhakkı -= 1
        print("Girdiğiniz Sayı Büyük. Lütfen {}'den Küçük Bir Sayı Giriniz. Kalan Tahmin Hakkınız: {}".format(a,tahminhakkı))
    else:
        print("Hesaplanıyor...")
        time.sleep(1)
        print("Tebrikler Sayıyı Doğru Bildiniz. Oyunu Kazandınız.")
        b = random.randint(1, 101)
        tahminhakkı = 7
        time.sleep(1)
        c = int(input("Tekrar Oynamak İçin 1'e, Oyundan Çıkmak İçin 0'a Basın: "))
        if c == 1:
            continue
        elif c == 0:
            break
        else:
            print("Geçersiz Bir Değer Girdiniz. Programın Başına Dönülüyor...")
            continue

    if tahminhakkı == 0:
        tahminhakkı = 7
        print("Tahmin Hakkınız Bitti. Oyunu Kaybettiniz. Doğru Sayı {} idi.".format(b))
        b = random.randint(1, 101)
        time.sleep(1)
        c = int(input("Tekrar Oynamak İçin 1'e, Oyundan Çıkmak İçin 0'a Basın: "))
        if c == 1:
            continue
        elif c == 0:
            break
        else:
            print("Geçersiz Bir Değer Girdiniz. Programın Başına Dönülüyor...")
            continue
