def ebobbulma(sayı1,sayı2):
    i = 1
    ebob = 1
    while(i <= sayı1 and i <= sayı2):
        if(not(sayı1 % i) and not (sayı2 % i)):
            ebob = i
        i += 1
    return ebob
sayı1 = int(input("Birinci Sayıyı Giriniz: "))
sayı2 = int(input("İkinci Sayıyı Giriniz: "))

print("EBOB:",ebobbulma(sayı1,sayı2))