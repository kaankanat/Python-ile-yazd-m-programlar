print("Sınav Notları Hesaplama Programı")

print("""****************************
Birinci Vize toplam notun yüzde 30'una etki edecek.

İkinci Vize toplam notun yüzde 30'una etki edecek.

Final Sınavı toplam notun yüzde 40'ına etki edecek.
****************************""")

a=int(input("Birinci Vize Sonucunuzu Giriniz: "))
b=int(input("İkinci Vize Sonucunuzu Giriniz: "))
c=int(input("Final Sınavı Sonucunuzu Giriniz: "))

ortalama=(a/100*30)+(b/100*30)+(c/100*40)

if ortalama >= 90:
    print("AA")
elif ortalama >= 85:
    print("BA")
elif ortalama >= 80:
    print("BA")
elif ortalama >= 75:
    print("BA")
elif ortalama >= 70:
    print("BA")
elif ortalama >= 65:
    print("BA")
elif ortalama >= 60:
    print("BA")
elif ortalama >= 55:
    print("BA")
elif ortalama < 55:
    print("Kaldınız.")
else:
    print("Gerçesiz İşlem.")