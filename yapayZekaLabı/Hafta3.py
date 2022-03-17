

def carpimTablosu():
    deger = int(input("Lütfen Bir Tam Sayı Giriniz "))
    yeniDeger=0
    for i in range(10):
        yeniDeger=yeniDeger+deger
        print(yeniDeger)
        
def kacBasamakli():
    sayi = int(input("Lütfen Bir Tam Sayı Giriniz "))
    sayac=0
    kontrol= True
    kalan=0
    while sayi>0:
        kalan=sayi%10
        sayi=(sayi - kalan)/10
        sayac+=1
        if sayi==0:
            kontrol=False
            print("Girilen Sayı" , sayac, "Basamaklıdır")

def modAlma():
    sayısalDeğerler = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]
    for i in range(len(sayısalDeğerler)):
        if sayısalDeğerler[i]%5==0 and sayısalDeğerler[i]<=150:
            print(sayısalDeğerler[i])
            
def sayiSırala():
    sayi1=0
    sayi2=100
    for i in range(99):
        sayi1+=1
        sayi2-=1
        print(sayi1,"-",sayi2)
        
def ipAddress():
    ip = input("Lütfen Ip Adresinizi Giriniz ").split(".")
    ip2=[]
    
    for t in range(len(ip)):
        ip2.append(int(ip[t]))
    
    for i in range(5):
        ip2[3]+=1
        if ip2[3] > 255:
            ip2[3]=0
            ip2[2]+=1
            if ip2[2] > 255:
                ip2[2]=0
                ip2[1]+=1
        print(ip2)
    print(ip2[0])
    
def bölünebilme():
    a = int(input("Lütfen Bir Tam Sayı Giriniz "))
    b = int(input("Lütfen Bir Tam Sayı Giriniz "))
    c = int(input("Lütfen Bir Tam Sayı Giriniz "))
    sonuc=0
    if a<b:
        for i in range(a,b+1):
            if a%c==0:
                sonuc+=1
            a+=1
        print(sonuc)
    else:
        for i in range(b,a+1):
            if b%c==0:
                sonuc+=1
            b+=1
        print(sonuc)
        
        

# carpimTablosu()
# kacBasamakli()
# modAlma()
# sayiSırala()
# ipAddress()
# bölünebilme()
