# ana.py
from cybersecurity_tools.interface import ekran_temizle, baslik_yazdir
from tools import nmap

def kesif_menu():
    ekran_temizle()
    baslik_yazdir("1. Adım: KEŞİF (RECONNAISSANCE)", "Keşif Aşaması - Nmap Kullanımı")
    hedef = input("Taranacak hedefi girin (Örn: 127.0.0.1 veya example.com): ")
    print(f"Nmap taraması başlatılıyor: {hedef}...\n")
    nmap_sonucu = nmap.nmap_tarama(hedef)
    print(nmap_sonucu)
    print("\nNmap işlemi tamamlandı.\n")
    input("Devam etmek için Enter'a basın...")

def ana_menu():
    ekran_temizle()
    baslik_yazdir("SİBER GÜVENLİK TERMİNAL ARACI")
    print("1. Keşif (Reconnaissance)")
    print("0. Çıkış\n")
    try:
        secim = int(input("Bir adım seçin (0 için çıkış): "))
        return secim
    except ValueError:
        print("Geçersiz giriş. Lütfen bir sayı girin.")
        input("Devam etmek için Enter'a basın...")
        return -1

while True:
    secim = ana_menu()
    if secim == 0:
        print("Programdan çıkış yapılıyor.")
        break
    elif secim == 1:
        kesif_menu()
    elif secim == -1:
        continue
    else:
        print("Geçersiz seçim.")
        input("Devam etmek için Enter'a basın...")