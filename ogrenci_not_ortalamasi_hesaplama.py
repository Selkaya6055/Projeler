ogrencisayisi = int(input("Öğrenci sayısını giriniz: "))
print(ogrencisayisi)

ogrenciler = []

for i in range(ogrencisayisi):
    print(f"\n{i + 1} Öğrenci bilgilerini giriniz: ")
    ad = input("Ad: ")
    soyad = input("Soyad: ")
    yas = int(input("Yaş: "))

    not1 = float(input("1. Sınav Notu: "))
    not2 = float(input("2. Sınav Notu: "))
    not3 = float(input("3. Sınav Notu: "))

    ortalama = ((not1 + not2 + not3) / 3)
    if ortalama >= 50:
        print("Geçti")
        durum = "Geçti"
    else:
        print("Kaldı")
        durum = "Kaldı"

    ogrenci = {
        "Ad" : ad,
        "Soyad" : soyad,
        "Yaş" : yas,
        "Notlar" : [not1, not2, not3],
        "Ortalama" : ortalama,
        "Durum" : durum
    }
    ogrenciler.append(ogrenci)

ortalamalistesi = [ogr["Ortalama"] for ogr in ogrenciler]
enyuksek = max(ortalamalistesi)
endusuk = min(ortalamalistesi)

sinifortalama = sum(ortalamalistesi) / len(ortalamalistesi)

print("\n Öğrenci Bilgileri ")
for ogr in ogrenciler:
    print(f"{ogr['Ad']} {ogr['Soyad']} | Yaş {ogr['Yaş']} {ogr['Notlar']} | Ortalama: {ogr['Ortalama']:.2f} | Durum: {ogr['Durum']}")

print(f"\n En Yüksek Ortalama: {enyuksek:.2f}")
print(f"En Düşük Ortalama: {endusuk:.2f}")
print(f"Sınıf Ortalaması: {sinifortalama:.2f}")
