urun = [] # Ürün isimlerini tutmak için boş bir liste oluşturuldu
fiyat = [] # Ürün fiyatlarını tutmak için boş bir liste oluşturuldu

while True: # Sonsuz döngü, kullanıcı 'X' girene kadar ürün eklemeye devam edecek
    urunAdi = (input("Ürün adını giriniz:")) # Kullanıcıdan ürün adı alınır
    if urunAdi == "X": # Eğer kullanıcı 'X' girerse ürün ekleme işlemi biter
        break
    urunFiyati = float(input("Ürün fiyatını giriniz:")) # Ürünün fiyatı alınır ve ondalıklı sayıya çevrilir
    urun.append(urunAdi) # Ürün adı listeye eklenir
    fiyat.append(urunFiyati) # Fiyat listeye eklenir

toplam = sum(fiyat) # Sepetteki tüm ürünlerin fiyatı toplanır

bakiye = float(input("Bakiyenizi giriniz:")) # Kullanıcının bakiyesi alınır

for i in urun: # Listedeki her ürün için döngü başlatılır
    print("\n Sepetiniz: ",urun," == ",fiyat,"\n Sepet tutarınız: ",toplam,"TL") # Sepet bilgileri yazdırılır
    if bakiye >= toplam:  # Eğer bakiye yeterliyse    
        print("\n Siparişiniz onaylandı.")
        print("\n Para üstünüz:",bakiye-toplam,"TL") # Para üstü hesaplanır ve yazdırılır
        break # Döngüden çıkılır
    elif bakiye < toplam: # Eğer bakiye yetersizse
        print("\n Bakiyeniz:",bakiye,"TL")
        print("\n Yetersiz bakiye, lütfen ürün çıkarınız.")
        while True:  # Kullanıcı ürün çıkardıkça kontrol tekrarlanır
            urunAdi = input("Çıkarmak istediğiniz ürünü söyleyiniz:") # Kullanıcıdan çıkarılacak ürün adı alınır
            urun.remove(urunAdi) # Ürün adı listeden silinir
            fiyat.remove(urunFiyati) # Ürün fiyatı listeden silinir
            toplam = sum(fiyat) # Yeni toplam hesaplanır
            if bakiye >= toplam: # Artık bakiye yeterliyse
                print("\n Siparişiniz onaylandı.")
                print("\n Para üstünüz:",bakiye-toplam,"TL")
                break # Döngüden çıkılır