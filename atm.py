bakiye = 10000

print("1. Bakiye Görüntüle\n 2. Para Yatırma\n 3. Para Çekme\n")
islem = int(input("Hangi işlemi yapacaksınız?"))

if islem == 1:
    print("Bakiye:", bakiye)
elif islem ==2:
    miktar = int(input("Yatırmak istediğiniz tutarı giriniz:"))
    bakiye += miktar
    print("güncel bakiyeniz:", bakiye)
elif islem ==3:
    cekme = int(input("Çekmek istediğiniz miktarı giriniz:"))
    if cekme<bakiye:
        bakiye -=cekme
        print("güncel bakiyeniz:", bakiye)
    else:
        print("yetersiz bakiye") 
else:
    print("hatalı tuşlama")   