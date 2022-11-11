birler=["","Bir","İki","Üç","Dört","Beş","Altı","Yedi","Sekiz","Dokuz"]
onlar=["","On","Yirmi","Otuz","Kırk","Elli","Altmış","Yetmiş","Seksen","Doksan"]

def okuma(sayı):
    a = sayı // 10
    b = sayı % 10
    return onlar[a] + " " + birler[b]

sayı = int(input("İki Basamaklı Bir Sayı Giriniz: "))
print(okuma(sayı))