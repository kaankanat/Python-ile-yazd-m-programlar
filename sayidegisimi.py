print("Müthiş Hizmet! İki sayı gireceksiniz ve biz bu iki sayıyı birbiriyle değiştireceğiz!")
a=int(input("İlk sayıyı giriniz: "))
b=int(input("İkinci sayıyı giriniz: "))

print("Değiştirilme İşlemi Gerçekleşiyor..... Değiştirilmeden önceki değerler, ilk sayı {}, ikinci sayı {}".format(a,b))

(a,b)=(b,a)

print("Değiştirilme İşlemi Gerçekleşti. Değişimden sonraki değerler: ilk sayı {}, ikinci sayı {}".format(a,b))