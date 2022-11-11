print("""
*************************************************
Armstrong Sayısı Bulma Programı
Örnek olarak; 
Bir sayı eğer 4 basamaklı ise ve oluşturan rakamlardan 
herbirinin 4. kuvvetinin toplamı( 3 basamaklı sayılar için 3.kuvveti )
o sayıya eşitse bu sayıya "Armstrong" sayısı denir.

Programı kapatmak için q tuşuna basınız.
*************************************************
""")

while True:
    try:
        sayı = input("Sayınızı Giriniz: ")
        basamaksayısı = len(sayı)
        basamak = 0
        toplam = 0
        if sayı == "q":
            print("Yine Bekleriz. Programdan çıkılıyor...")
            break
        sayı=int(sayı)
        geçicisayı = sayı
        while (geçicisayı > 0):
            basamak = geçicisayı % 10
            toplam += basamak ** basamaksayısı
            geçicisayı //= 10
        if (toplam == sayı):
            print("Girdiniz Sayı {} bir Armstrong Sayısıdır.".format(sayı))
        else:
            print("Girdiniz Sayı {} bir Armstrong Sayısı Değildir.".format(sayı))
    except ValueError:
        print("Geçersiz Bir Değer Girdiniz.")

