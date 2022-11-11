print("Dik Üçgenin Hipotenüsünü Hesaplama Programı")
a = int(input("Dik Üçgenin Dik Olan İki Kenarından Birinin Uzunluğunu Giriniz: "))
b = int(input("Dik Üçgenin Dik Olan İki Kenarından İkincisinin Uzunluğunu Giriniz: "))

hipotenus=(a**2)+(b**2)

print("Dik iki kenarının birinin uzunluğu {}, diğerinin uzunluğu {} olan üçgenin hiptenüsünün uzunluğu {} dir.".format(a,b,hipotenus))