while True:
    try:
        x = int(input("Bir sayı giriniz: "))
        if -1 < x < 3:
            print("Sayınız üçten küçük. Lütfen üçten büyük bir sayı giriniz.")
        elif x == 3:
            print("Sayınız zaten üç. Üçün üçe bölenildiğini biliyorsundur bence :D")
        elif x == 31:
            print(":D")
        elif x % 3 == 0:
            print("Evet! Sayınız üçe tam bölünebiliyor.")
        elif x % 3 == 1:
            print("OLAMAZ! Sayınız üçe tam bölünemiyor. Bölümün kalanı 1.")
        elif x % 3 == 2:
            print("OLAMAZ! Sayınız üçe tam bölünemiyor. Bölümün kalanı 2.")
        else:
            print("Bir takım hatalar oldu. Ne oldu ben de bilmiyom")
    except ValueError:
        print("Sayı girmediniz. Lütfen Sayı Giriniz.")