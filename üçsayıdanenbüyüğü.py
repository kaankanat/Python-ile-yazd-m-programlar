print("Girdiğiniz üç sayıdan en büyüğünü bulma programı")

a=input("Birinci sayıyı giriniz: ")
b=input("İkinci sayıyı giriniz: ")
c=input("Üçüncü sayıyı giriniz: ")

if a>b and a>c:
    print("En büyük sayı {}".format(a))
elif b>a and b>c:
    print("En büyük sayı {}".format(b))
elif c>a and c>b:
    print("En büyük sayı {}".format(c))
else:
    print("Bir takım hatalar oldu yav.")