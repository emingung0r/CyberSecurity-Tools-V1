import datetime
import os
import subprocess
import platform
from interface import clear_screen, print_header
from stages import reconnaissance, scanning, gaining_access, privilege_escalation, covering_tracks, information_gathering
from tools import nmap, shodan, maltego, nikto, owasp_zap, metasploit, burp_suite # Tüm araçlar import edildi
from reports import report_generator

def check_tool(tool_name, command):
    """Belirli bir aracın kurulu olup olmadığını kontrol eder."""
    try:
        subprocess.run([command, "--version"], capture_output=True, text=True, check=True)
        return True, ""
    except FileNotFoundError:
        return False, f"{tool_name} bulunamadı. Lütfen {tool_name}'ı yükleyin."
    except Exception as e:
        return False, f"{tool_name} kontrol edilirken hata oluştu: {e}"

def check_system():
    """Sistemi kontrol eder ve kurulu araçları listeler."""
    clear_screen()
    print_header("Sistem Kontrolü")
    print("================")

    tools_to_check = { # Kontrol edilecek araçlar
        "Nmap": "nmap",
        "Shodan": "shodan", # Shodan eklendi (Shodan CLI kurulu olmalı)
        # Diğer araçlar buraya eklenebilir
    }

    for tool_name, command in tools_to_check.items():
        is_installed, message = check_tool(tool_name, command)
        if is_installed:
            print(f"✅ {tool_name}: Kurulu")
        else:
            print(f"❌ {tool_name}: {message}")
            if tool_name == "Nmap":
                if platform.system() == "Linux":
                    print("Kurulum için: sudo apt-get install nmap")
                elif platform.system() == "Darwin":
                    print("Kurulum için: brew install nmap")
                elif platform.system() == "Windows":
                    print("Kurulum için: https://nmap.org/download.html adresinden indirin ve PATH'e ekleyin.")
            elif tool_name == "Shodan":
                print("Shodan CLI kurulumu için: pip install shodan") # Shodan kurulum bilgisi
            else:
                print("Bilinmeyen işletim sistemi veya araç. Lütfen kurulum talimatlarını internetten araştırın.")

    input("Devam etmek için Enter'a basın...")

def report_menu(results):
    """Rapor oluşturma menüsünü gösterir."""
    clear_screen()
    print_header("Rapor Oluşturma")

    if not results:
        print("Oluşturulacak bir rapor bulunmamaktadır.")
        input("Devam etmek için Enter'a basın...")
        return

    print("Hangi formatta rapor oluşturmak istersiniz?")
    print("1. Metin (.txt)")
    print("2. PDF (.pdf)")
    print("3. Word (.docx)")

    while True:
        try:
            format_choice = int(input("Seçiminizi girin: "))
            if format_choice in (1, 2, 3):
                break
            else:
                print("Geçersiz seçim. Lütfen geçerli bir seçenek girin.")
        except ValueError:
            print("Lütfen bir sayı girin.")

    format_list = ["txt", "pdf", "docx"]
    format = format_list[format_choice - 1]

    for result in results:
        report_path, report_content = report_generator.generate_report(result, format)

        # Hata kontrolü
        if isinstance(report_path, str) and (report_path.startswith("1001:") or report_path.startswith("1002:") or report_path.startswith("2001:") or report_path.startswith("2002:")) :
            print(report_path) # Hata mesajını yazdır
            input("Devam etmek için Enter'a basın...")
            continue # Bir sonraki rapora geç

        report_generator.save_report_to_file((report_path, report_content))

    print(f"Rapor 'reports' klasörüne kaydedildi.")
    input("Devam etmek için Enter'a basın...")

def main_menu():
    """Ana menüyü gösterir."""
    clear_screen()
    print_header("Siber Güvenlik Değerlendirme Aracı")
    print("1. Keşif Aşaması")
    print("2. Tarama Aşaması")
    print("3. Erişim Kazanma Aşaması")
    print("4. Hak Yükseltme Aşaması")
    print("5. İz Sürmeyi Engelleme Aşaması")
    print("6. Bilgi Toplama Aşaması")
    print("7. Sistem Kontrolü")
    print("8. Rapor Oluştur")
    print("0. Çıkış")
    while True:
        try:
            choice = int(input("Seçiminizi girin: "))
            if 0 <= choice <= 8: # Geçerli seçenekler 0-8
                return choice
            else:
                print("Geçersiz seçim. Lütfen 0-8 arasında bir sayı girin.")
        except ValueError:
            print("Lütfen bir sayı girin.")

if __name__ == "__main__":
    results = []
    check_system() # Başlangıçta sistem kontrolü yapılır

    while True:
        choice = main_menu()
        if choice == 0:
            print("Programdan çıkılıyor.")
            break
        elif choice == 1:
            result = reconnaissance.reconnaissance_menu()
            if result:
                results.append(result)
        elif choice == 2:
            result = scanning.scanning_menu()
            if result:
                results.append(result)
        elif choice == 3:
            result = gaining_access.gaining_access_menu()
            if result:
                results.append(result)
        elif choice == 4:
            result = privilege_escalation.privilege_escalation_menu()
            if result:
                results.append(result)
        elif choice == 5:
            result = covering_tracks.covering_tracks_menu()
            if result:
                results.append(result)
        elif choice == 6:
            result = information_gathering.information_gathering_menu()
            if result:
                results.append(result)
        elif choice == 7:
            check_system()
        elif choice == 8:
            report_menu(results)
        else:
            print("Geçersiz seçim.")