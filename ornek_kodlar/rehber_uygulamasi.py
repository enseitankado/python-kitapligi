"""
    ~Bismillahirrahmanirrahim~

    Ummeti cihana notlarim
    ~~~~~~~~~~~~~~~~~~~~~~

    1) Programalama da yazim sekli olarak 2 tercih var.
    camelStyle ve snake_style
    Gordugum kadariyla Python'da camelStyle sadece sinif isimlerinde kullaniliyor,
    onun disinda programci tanimli hersey snake_style olmali.

    2) Dedigin is herbir kisiye tekil id vermekle cozulebilir ancak.
    Tabi ayni kayitlari listeletip, aynilar icinden kacinci siradakini
    guncellemek ya da silmek istiyorsun diye de sorulabilir. Ama bu kotu
    bir yaklasim olur. Kodlamayi da karisiklastirir.
    Vatandas, onunde sonunda kayitlarin ayir edilebilmesini saglayan
    tekil id mantigini ogrenecek. Belki yeri burasi olmayabilir.
    Ben bu yolu tercih ettim.

    3) rehber.txt'ye bir sutun daha ekledim (id sutunu)
    Yeni kayit eklerken son id'yi almak icin get_max_id adinda bir tanimlama yaptim.

    4) Sadece bir kayit guncellenecekse guncelliyor, birden fazla kayitla uyusuyorsa
    id'leri listeletip hangisini guncelleyecen diye soruyor.

    

    
    
"""

import os

def get_max_id(dosya_adi):
    # Dosya yoksa kayit sayisi 0
    if (os.path.exists(dosya_adi) == False):
        return 0;
    # Rehberdeki tum id numaralarini oku
    with open(dosya_adi, 'r', encoding='utf8') as dosya:
        rehber = dosya.readlines()
        tum_idler = []
        for kisi in rehber:
            kisi = kisi.split(',')
            tum_idler.append(kisi[0])
    # En buyuk id numarasini geri dondur
    return int(max(tum_idler))


def Rehbere_Kisi_Ekle(kisi_id, isim, soyisim, telefon, email):
    with open('rehber.txt', 'a',encoding='utf8') as dosya:        
        dosya.write(str(kisi_id)+','+isim+','+ soyisim +','+ telefon +','+ email+'\n')


def Telefon_Numarasi_Bul(isim):
    with open('rehber.txt', 'r',encoding='utf8') as dosya:
        rehber = dosya.readlines()
        for kisi in rehber:
            if isim in kisi.split(','):
                print("Aradığınız Kişinin Numarası : ",kisi.split(',')[3])


def Telefon_Numarasi_Guncelle(isim, telefon):    
    with open('rehber.txt', 'r+') as dosya:        
        rehber = dosya.readlines()

        # Ayni isimde baska kisi var mi
        ayni_isimli_kayit_sayisi = 0
        for kisi in rehber:
            if isim in kisi.split(','):
                ayni_isimli_kayit_sayisi += 1

        # Guncellenecek isim bulunamadi
        if (0 == ayni_isimli_kayit_sayisi):
            print("\nRehberde ", isim, " isimli bir kayit yok.")
            return

        # Aranan isimden sadece 1 tane varsa degistir
        if (1 == ayni_isimli_kayit_sayisi):
            for kisi in rehber:
                if isim in kisi.split(','): 
                    rehber.remove(kisi)
                    rehber.append(str(kisi.replace(kisi.split(',')[3],telefon)))
                    dosya.seek(0)
                    dosya.writelines(rehber)
                    break

        # Aranan isimden birden fazla varsa id'lerini listele
        if (ayni_isimli_kayit_sayisi > 1):
            print("\n Rehberde ayni isimde birden fazla kayit var.")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            for kisi in rehber:
                if isim in kisi.split(','):
                    print(kisi, end="")

            # Secilen id'ye sahip kaydi guncelle
            kisi_id = input("Telefon numarasini degistirmek istediginiz kisini id numarasini girin:")
            for kisi in rehber:
                if kisi_id == kisi.split(',')[0]:
                    rehber.remove(kisi)
                    rehber.append(str(kisi.replace(kisi.split(',')[3],telefon)))
                    dosya.seek(0)
                    dosya.writelines(rehber)
                    break
        

def Tum_Rehber_Goster():
    with open('rehber.txt', 'r',encoding='utf8') as dosya:
        rehber = dosya.readlines()
        print("\nRehber listeleniyor...")
        print("~~~~~~~~~~~~~~~~~~~~~~")
        for kisi in rehber:
            print(kisi, end="")


while True:
    print('''
    1.) Kisi Ekle
    2.) Kisinin Telefon no Bul
    3.) Kisinin Telefon no Guncelle
    4.) Tum Kisileri Goster
    Cikmak icin q
    ''')

    select = input('Bir tercih yapin :')

    if select == '1':
        isim = input('Isim Girin :')
        soyisim = input('Soyisim Girin :')
        telefon = input('Telefon No Gir :')
        email = input('Email Gir  :')
        kisi_id = get_max_id('rehber.txt') + 1
        Rehbere_Kisi_Ekle(kisi_id, isim, soyisim, telefon, email)

    elif select == '2':
        isim = input('Isim Girin :')
        Telefon_Numarasi_Bul(isim)

    elif select == '3':
        isim = input('Isim Girin :')
        telefon = input('Telefon No Gir :')
        Telefon_Numarasi_Guncelle(isim, telefon)

    elif select == '4':
        Tum_Rehber_Goster()

    elif select=='q':
        exit()

