print("Beden Kitle İndeksi Hesaplama")

a=int(input("Lütfen Kilonuzu Yazınız: "))
b=float(input("Lütfen Boyunuzu Metre Cinsinden Yazınız(Örnek: 1.70): "))

bedenkitleindeksi = (a / (b*b))

if bedenkitleindeksi <= 18.5:
    print("Beden Kitle İndeksiniz: {}, Zayıfsınız.".format(bedenkitleindeksi))
elif 18.5 < bedenkitleindeksi < 25:
    print("Beden Kitle İndeksiniz: {}, Normal Kilodasınız.".format(bedenkitleindeksi))
elif 25 <= bedenkitleindeksi < 35:
    print("Beden Kitle İndeksiniz: {}, Normalin Üzerinde Kilolusunuz.".format(bedenkitleindeksi))
elif 35 <= bedenkitleindeksi:
    print("Beden Kitle İndeksiniz: {}, Obezsiniz.".format(bedenkitleindeksi))
else:
    print("Geçersiz bir değer girdiniz.")