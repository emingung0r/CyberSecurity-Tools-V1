import datetime
import os
import subprocess
import platform

# interface.py dosyasından fonksiyonları import et
from interface import clear_screen, print_header

def check_tool(tool_name, command):
    """Belirli bir aracın kurulu olup olmadığını kontrol eder."""
    try:
        subprocess.run([command, "--version"], capture_output=True, text=True, check=True)
        return True, ""
    except FileNotFoundError:
        return False, f"{tool_name} bulunamadı. Lütfen yükleyin."
    except Exception as e:
        return False, f"{tool_name} kontrol edilirken hata oluştu: {e}"

def check_system():
    """Sistemi kontrol eder ve kurulu araçları listeler."""
    print_header("Sistem Kontrolü")
    print("================")

    tools_to_check = {
        "Nmap": "nmap",
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
                elif platform.system() == "Darwin":  # macOS için Darwin
                    print("Kurulum için: brew install nmap")
                elif platform.system() == "Windows":
                    print("Kurulum için: https://nmap.org/download.html adresinden indirin ve PATH'e ekleyin.")
                else:
                    print("Bilinmeyen işletim sistemi. Lütfen kurulum talimatlarını internetten araştırın.")

    input("Devam etmek için Enter'a basın...")


def write_report(results):
    """Raporu bir dosyaya yazar."""
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"cybersecurity_report_{timestamp}.txt"
    try:
        with open(filename, "w", encoding="utf-8") as file:
            file.write("CYBERSECURITY ASSESSMENT REPORT\n")
            file.write("===============================\n")
            if not results:
                file.write("Hiçbir işlem gerçekleştirilmedi.\n")
            else:
                for result in results:
                    file.write(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n")
                    file.write(f"Aşama: {result['stage']}\n")
                    file.write(f"Araç: {result['tool']}\n")
                    file.write(f"Hedef: {result['target']}\n")
                    if result.get("arguments"):
                        file.write(f"Argümanlar: {result['arguments']}\n")
                    file.write("Sonuç:\n")
                    file.write(result['result'])
                    file.write("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n\n")

        print(f"Rapor {filename} dosyasına kaydedildi.")
    except Exception as e:
        print(f"Rapor yazma hatası: {e}")

from stages import reconnaissance

def main_menu():
    """Ana menüyü gösterir."""
    print_header("Siber Güvenlik Değerlendirme Aracı")
    print("1. Keşif Aşaması")
    print("7. Sistem Kontrolü")
    print("0. Çıkış ve Rapor Oluştur")
    while True:
        try:
            choice = int(input("Seçiminizi girin: "))
            if choice in (0, 1, 7): # 7 eklendi
                return choice
            else:
                print("Geçersiz seçim. Lütfen 0, 1 veya 7 girin.")
        except ValueError:
            print("Lütfen bir sayı girin.")

if __name__ == "__main__":
    results = []
    check_system() # Başlangıçta sistem kontrolü

    while True:
        choice = main_menu()
        if choice == 0:
            write_report(results)
            print("Programdan çıkılıyor.")
            break
        elif choice == 1:
            result = reconnaissance.reconnaissance_menu()
            if result:
                results.append(result)
        elif choice == 7: # Sistem kontrolü
            check_system()
        else:
            print("Geçersiz seçim.")
            input("Devam etmek için Enter'a basın...")