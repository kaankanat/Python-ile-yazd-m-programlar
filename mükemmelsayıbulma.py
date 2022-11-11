print("""
*************************************************************************
Mükemmel Sayı Bulma Programı

Bir sayının kendi hariç bölenlerinin toplamı kendine eşitse bu sayıya "mükemmel sayı" denir. 
Örnek olarak, 6 mükemmel bir sayıdır. (1 + 2 + 3 = 6)

Programdan çıkmak için q'ya basın.

*************************************************************************""")
while True:
    try:
        i = 1
        toplam = 0
        sayi = input("Bir sayı giriniz: ")
        if (sayi == "q"):
            print("Programı Kullandığınız için teşekkürler, Programdan çıkılıyor....")
            break
        elif type(sayi) == str:
            sayi=int(sayi)
        while (i < sayi):
            if(sayi % i == 0):
                toplam += i
            i += 1
        if (toplam == sayi):
            print("Girdiğiniz Sayı {} Mükemmel Sayıdır.".format(sayi))
        else:
            print("Girdiğiniz Sayı {} Mükemmel Sayı Değildir.".format(sayi))
    except ValueError:
        print("Geçersiz Karakter Girdiniz.")