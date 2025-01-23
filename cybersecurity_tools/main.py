import datetime
import os
import logging

from interface import clear_screen, print_header, print_menu
from stages import reconnaissance, scanning, gaining_access, privilege_escalation, covering_tracks, information_gathering
from tools import nmap, shodan, maltego, nikto, owasp_zap, metasploit, burp_suite
from reports import report_generator
from system_check import check_system, install_tool, setup_environment

# Log yapılandırması
logging.basicConfig(filename='reports/app.log', level=logging.INFO,
                    format='%(asctime)s - %(asctime)s - %(message)s', encoding="utf-8")

def report_menu(filename):
    clear_screen()
    print_header("Rapor Görüntüle")
    reports_dir = "reports"
    filepath = os.path.join(reports_dir, filename)
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            print(file.read())
    except FileNotFoundError:
        print("Rapor dosyası bulunamadı.")
    input("Devam etmek için Enter'a basın...")

def main_menu():
    clear_screen()
    print_header("Siber Güvenlik Değerlendirme Aracı")
    print_menu({
        1: "Keşif Aşaması",
        2: "Tarama Aşaması",
        3: "Erişim Kazanma Aşaması",
        4: "Hak Yükseltme Aşaması",
        5: "İz Sürmeyi Engelleme Aşaması",
        6: "Bilgi Toplama Aşaması",
        7: "Sistem Kontrolü",
        8: "Rapor Görüntüle",
        0: "Çıkış"
    })
    while True:
        try:
            choice = int(input("Seçiminizi girin: "))
            if 0 <= choice <= 8:
                return choice
            else:
                print("Geçersiz seçim. Lütfen 0-8 arasında bir sayı girin.")
        except ValueError:
            print("Lütfen bir sayı girin.")

def main():
    # Ortamı hazırla
    if not setup_environment():
        print("Ortam hazırlanamadı. Program sonlandırılıyor.")
        return

    # Başlangıçta sistem kontrolü yap
    print("Sistem kontrolü yapılıyor...")
    check_system()
    
    print("\nSistem kontrolü tamamlandı. Ana menüye devam etmek için Enter'a basın...")
    input()

    report_filename = f"cybersecurity_report_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    logging.info("Uygulama başlatıldı.")

    stages = {
        1: {"module": reconnaissance, "menu_function": reconnaissance.reconnaissance_menu, "name": "Keşif Aşaması"},
        2: {"module": scanning, "menu_function": scanning.scanning_menu, "name": "Tarama Aşaması"},
        3: {"module": gaining_access, "menu_function": gaining_access.gaining_access_menu, "name": "Erişim Kazanma Aşaması"},
        4: {"module": privilege_escalation, "menu_function": privilege_escalation.privilege_escalation_menu, "name": "Hak Yükseltme Aşaması"},
        5: {"module": covering_tracks, "menu_function": covering_tracks.covering_tracks_menu, "name": "İz Sürmeyi Engelleme Aşaması"},
        6: {"module": information_gathering, "menu_function": information_gathering.information_gathering_menu, "name": "Bilgi Toplama Aşaması"},
    }

    while True:
        choice = main_menu()
        logging.info(f"Kullanıcı seçimi: {choice}")
        if choice == 0:
            print("Programdan çıkılıyor.")
            logging.info("Uygulama kapatılıyor.")
            break
        elif choice in stages:
            stage = stages[choice]
            try:
                result = stage["menu_function"]()
                if result:
                    result["stage"] = stage["name"]
                    report_content = report_generator.generate_report_content(result)
                    report_generator.save_report_to_file(report_content, filename=report_filename)
            except Exception as e:
                print(f"{stage['name']} aşamasında bir hata oluştu: {e}")
                logging.exception(f"{stage['name']} aşamasında hata oluştu")
        elif choice == 7:
            check_system()
        elif choice == 8:
            report_menu(report_filename)
        else:
            print("Geçersiz seçim.")

if __name__ == "__main__":
    main()