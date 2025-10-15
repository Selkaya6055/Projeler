import random
sayi = random.randint(1,10)
while True:
    tahmin = int(input("Tahmin et:"))
    if tahmin==sayi:
        print("doğru")
        break
    elif tahmin<=sayi:
        print("tahminini yükselt")
    elif tahmin>=sayi:
        print("tahminini düşür")
