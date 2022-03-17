def ücgenAçi():
    sayi1 = int(input("Lütfen Bir Tam Sayı Giriniz "))
    sayi2 = int(input("Lütfen Bir Tam Sayı Giriniz "))
    sayi3 = int(input("Lütfen Bir Tam Sayı Giriniz "))
    
    if sayi1==90 or sayi2==90 or sayi3==90:
        print("Bu Üçgen Dik Açılıdır.")
    if sayi1>90 or sayi2>90 or sayi3>90:
        print("Bu Üçgen Geniş Açılıdır.")
    if sayi1<90 and sayi2<90 and sayi3<90:
        print("Bu Üçgen Dar Açılıdır.")

def uzayliOyunu():
    uzaylıRengi=""
    print("1-Kırmızı")
    print("2-Yeşil")
    print("3-Sarı")
    uzaylıRengi=input("Yukarda Değerlerden Birini Seçiniz.")

def switch(deger):
        if deger=="2":
            print("Tebrikler, yeşil uzaylıya ateş ettiğiniz için 5 puan kazandınız")
        if deger!="1" or deger!="2" or deger!="3":
            print("Tekrar Deneyiniz")
        else:
            print("Tebrikler, yeşil olmayan uzaylıya ateş ettiğiniz için 10 puan kazandınız")

def uzayliOyunu():
    uzaylıRengi=""
    print("1-Kırmızı")
    print("2-Yeşil")
    print("3-Sarı")
    while True:
        uzaylıRengi=input("Yukardaki Değerlerden Birini Seçiniz.")
        switch(uzaylıRengi)
        
def uzayliOyunu2():
    print("1-Kırmızı")
    print("2-Yeşil")
    print("3-Sarı")
    while True:
        uzaylıRengi=input("Yukardaki Değerlerden Birini Seçiniz.")
        if uzaylıRengi=="1":
            print("Tebrikler, yeşil uzaylıya ateş ettiğiniz için 5 puan kazandınız")
        elif uzaylıRengi=="2":
            print("Tebrikler, sarı uzaylıya ateş ettiğiniz için 10 puan kazandınız")
        elif uzaylıRengi=="3":
            print("Tebrikler, kırmızı uzaylıya ateş ettiğiniz için 15 puan kazandınız")
        else:
            print("Tekrar Deneyiniz")

def yasFonk():
    while True:
        yas=0
        yas=int(input("Yaşınızı Giriniz."))
        if yas < 2:
            print("Bu kişi bebektir")
        elif 2<= yas <4:
            print("Bu kişi yeni yürümeye başlayan çocuktur")
        elif 4<= yas <13:
            print("Bu kişi çocuktur")
        elif 13<= yas <20:
            print("Bu kişi ergendir")
        elif 20<= yas <65:
            print("Bu kişi yetişkindir")
        else:
            print("Bu kişi yaşlıdır")

def meyveler():
    favori_meyveler=["mandalina","çilek","portakal","kavun","kivi"]
    ornek_meyveler=["elma","armut","karpuz","kavun","muz","portakal","çilek","vişne","kiraz","mandalina"]
    
    for eleman in ornek_meyveler:
            if eleman in favori_meyveler:
                print(eleman)
                
# meyveler()
# yasFonk()
# uzayliOyunu()
# uzayliOyunu2()
# ücgenAçi()
        
        
    