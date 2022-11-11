print("Geometrik Şekil Hesaplama")
a=int(input("Üçgenin tipini bulmak istiyorsanız 1'e, Dörtgenin tipini bulmak istiyorsanız 2'ye basın: "))

if a == 1:
    print("Lütfen kenarları sırasıyla giriniz.")
    b = int(input("Birinci Kenar: "))
    c = int(input("İkinci Kenar: "))
    d = int(input("Üçüncü Kenar: "))
    if (abs(a+b) > c and abs(a+c) > b and abs(b+c) > a):
        if((b == c and b != d) or (b == d and b != c) or (c == d and b != c)):
            print("İkizkenar Üçgen")
        elif(b==c and b==d and c==d):
            print("Eşkenar Üçgen")
        else:
            print("Çeşitkenar Üçgen")
    else:
        print("Girdiğiniz Değerler Üçgen Belirtmiyor.")
elif a == 2:
    print("Lütfen kenarları sırasıyla giriniz.")
    x = int(input("Birinci Kenar: "))
    y = int(input("İkinci Kenar: "))
    z = int(input("Üçüncü Kenar: "))
    t = int(input("Dördüncü Kenar: "))
    if x==y and x==z and x==t:
        print("Kare")
    elif (x==z and y==t) or (x==y and z==t) or (x==t and z==y):
        print("Dikdörtgen")
    else:
        print("Dörtgen")
else:
    print("Girdiğiniz Şekil Geçersiz.")

