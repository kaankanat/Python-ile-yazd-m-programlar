import math
import time

print("""
**************************************
Gelişmiş Hesap Makinesi

İşlemler:

1 - Toplama
2 - Çıkarma
3 - Çarpma
4 - Bölme
5 - Faktoriyel
6 - Kök Alma
7 - Bir Sayının İstediğiniz Kuvvetini Bulma
8 - 10 Tabanında Logaritma Alma
9 - Sinüs, Kosinüs, Tanjant Hesaplama

0 - Programdan Çıkış
**************************************
""")
while True:
    işlem = int(input("İşlem Seçiniz: "))
    if işlem == 0:
        break
    elif işlem == 1:
        a = int(input("Toplamak İstediğiniz Birinci Sayıyı Giriniz:"))
        b = int(input("Toplamak İstediğiniz İkinci Sayıyı Giriniz:"))
        print("İşleminiz Hesaplanıyor....")
        time.sleep(1)
        print(a+b)
    elif işlem == 2:
        a = int(input("Çıkarmak İstediğiniz Birinci Sayıyı Giriniz:"))
        b = int(input("Çıkarmak İstediğiniz İkinci Sayıyı Giriniz:"))
        print("İşleminiz Hesaplanıyor....")
        time.sleep(1)
        print(a - b)
    elif işlem == 3:
        a = int(input("Çarpmak İstediğiniz Birinci Sayıyı Giriniz:"))
        b = int(input("Çarpmak İstediğiniz İkinci Sayıyı Giriniz:"))
        print("İşleminiz Hesaplanıyor....")
        time.sleep(1)
        print(a * b)
    elif işlem == 4:
        a = int(input("Bölmek İstediğiniz Birinci Sayıyı Giriniz:"))
        b = int(input("Bölmek İstediğiniz İkinci Sayıyı Giriniz:"))
        print("İşleminiz Hesaplanıyor....")
        time.sleep(1)
        print(a / b)
    elif işlem == 5:
        a = int(input("Faktoriyelini Almak İstediğiniz Sayıyı Giriniz:"))
        print("İşleminiz Hesaplanıyor....")
        time.sleep(1)
        print(math.factorial(a))
    elif işlem == 6:
        a = int(input("Kökünü Almak İstediğiniz Sayıyı Giriniz:"))
        print("İşleminiz Hesaplanıyor....")
        time.sleep(1)
        print(math.pow(a,1/2))
    elif işlem == 7:
        a = int(input("Kuvvetini Almak İstediğiniz Sayıyı Giriniz:"))
        b = int(input("Sayının Kaçıncı Kuvvetini Almak İstediğinizi Giriniz:"))
        print("İşleminiz Hesaplanıyor....")
        time.sleep(1)
        print(math.pow(a,b))
    elif işlem == 8:
        a = int(input("10 Tabanında Logaritmasını Almak İstediğiniz Sayıyı Giriniz:"))
        print("İşleminiz Hesaplanıyor....")
        time.sleep(1)
        print(math.log10(a))
    elif işlem == 9:
        print("""
        *************************
        Sinüs Hesaplamak için 1
        Kosinüs Hesaplamak için 2
        Tanjant Hesaplamak için 3
        
        Programın Başına Geri Dönmek İçin 0
        *************************
        """)
        a = int(input("Tuşlayınız:"))
        if a == 0:
            continue
        elif a == 1:
            a = int(input("Sinüs Almak İstediğiniz Sayıyı Giriniz:"))
            print(math.sin(a))
        elif a == 2:
            a = int(input("Kosinüs Almak İstediğiniz Sayıyı Giriniz:"))
            print(math.cos(a))
        elif a == 3:
            a = int(input("Tanjant Almak İstediğiniz Sayıyı Giriniz:"))
            print(math.tan(a))
