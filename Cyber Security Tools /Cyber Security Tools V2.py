import os
import datetime
import subprocess  # Alt süreçleri çalıştırmak için

# ... (Önceki fonksiyonlar: ekran_temizle, baslik_yazdir, asama_yazdir, ana_menu, rapor_yaz)

def kesif_menu():
    ekran_temizle()
    baslik_yazdir("1. Adım: KEŞİF")
    asama_yazdir("Keşif (Reconnaissance) Aşaması")
    print("Araçlar:")
    print("1. Nmap")
    print("2. Shodan (Henüz Tam Entegrasyon Yok)") # henüz tam entegre değil
    print("3. Maltego (Henüz Tam Entegrasyon Yok)\n")# henüz tam entegre değil
    try:
      arac_secim = int(input("Bir araç seçin: "))
      return arac_secim
    except ValueError:
        print("Geçersiz giriş. Lütfen bir sayı girin.")
        input("Devam etmek için Enter'a basın...")
        return -1

def nmap_tarama(hedef):
    try:
        # Nmap komutunu çalıştırma
        sonuc = subprocess.run(["nmap", hedef], capture_output=True, text=True, check=True)
        return sonuc.stdout # çıktıyı döndür
    except subprocess.CalledProcessError as e:
        return f"Nmap hatası: {e.stderr}"
    except FileNotFoundError:
        return "Nmap bulunamadı. Lütfen Nmap'in yüklü olduğundan emin olun."
    except Exception as e:
      return f"Beklenmeyen bir hata oluştu {e}"

rapor = ""

while True:
    secim = ana_menu()
    if secim == 0:
        rapor_yaz(rapor)
        break
    elif secim == 1:
        arac_secim = kesif_menu()
        if arac_secim == 1:
            hedef = input("Taranacak hedefi girin (Örn: 127.0.0.1 veya example.com): ")
            ekran_temizle()
            baslik_yazdir("1. Adım: KEŞİF")
            asama_yazdir("Keşif (Reconnaissance) Aşaması - Nmap Kullanımı")
            rapor += f"Keşif Aşaması - Nmap Kullanımı Başlatıldı - Hedef: {hedef}\n"
            print(f"Nmap taraması başlatılıyor: {hedef}...\n")
            nmap_sonucu = nmap_tarama(hedef) # nmap taramasını çalıştır ve sonucu al
            print(nmap_sonucu) # nmap sonucunu ekrana yazdır
            rapor += nmap_sonucu + "\n" # nmap sonucunu rapora ekle
            print("\nNmap işlemi tamamlandı.\n")
            input("Devam etmek için Enter'a basın...")
        # Shodan ve Maltego entegrasyonu için benzer kodlar buraya eklenecek
        elif arac_secim == -1:
          continue
        else:
          print("Geçersiz araç seçimi")
          input("Devam etmek için Enter'a basın...")
    elif secim == -1:
      continue
    else:
        print("Geçersiz seçim.")
        input("Devam etmek için Enter'a basın...")