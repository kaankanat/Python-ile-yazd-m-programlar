print("""************************************
Programa eklemek istediğiniz sayıyı giriniz.
Programı sona erdirmek için q tuşuna basınız.
************************************""")
toplam = 0
while True:
    try:
        a = input("Bir Sayı Giriniz: ")
        if a == "q":
            print("Program Sonlandırılıyor...")
            break
        else:
            a = int(a)
            toplam+=a
            print("Girdiğiniz Sayıların toplamı {}".format(toplam))
    except ValueError:
        print("Hatalı bir karakter girdiniz.")
