x = int(input("Bir sayı giriniz: "))
if -1 < x < 3:
    print("Sayınız üçten küçük. Lütfen üçten büyük bir sayı giriniz.")

elif x == 3:
    print("Sayınız zaten üç. Üçün üçe bölenildiğini biliyorsundur bence :D")

elif x % 3 == 0:
    print("Evet! Sayınız üçe tam bölünebiliyor.")

else:
    print("OLAMAZ! Sayınız üçe tam bölünemiyor.")

while x > -999999999999999999999999999999999999:
    x = int(input("Bir sayı giriniz: "))
    if -1 < x < 3:
        print("Sayınız üçten küçük. Lütfen üçten büyük bir sayı giriniz.")

    elif x == 3:
        print("Sayınız zaten üç. Üçün üçe bölenildiğini biliyorsundur bence :D")

    elif x % 3 == 0:
        print("Evet! Sayınız üçe tam bölünebiliyor.")

    else:
        print("OLAMAZ! Sayınız üçe tam bölünemiyor.")