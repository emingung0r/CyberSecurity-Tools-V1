# stages/reconnaissance.py
from interface import clear_screen, print_header
from tools import nmap

def reconnaissance_menu():
    """Handles the reconnaissance stage menu and Nmap scans.
    Keşif aşaması menüsünü ve Nmap taramalarını yönetir."""
    clear_screen()
    print_header("1. RECONNAISSANCE", "Reconnaissance Stage - Nmap Usage") #Başlıklar
    print("1. Nmap Scan") #Nmap Taraması
    try:
        tool_choice = int(input("Select a tool: ")) #Bir araç seçin
        if tool_choice == 1:
            target = input("Enter target to scan (e.g., 127.0.0.1 or example.com): ") #Taranacak hedefi girin
            arguments = input("Enter additional arguments (leave blank if none): ") #Ek argümanlar girin
            print(f"Starting Nmap scan: {target}...\n") #Nmap taraması başlatılıyor
            nmap_result = nmap.nmap_scan(target, arguments)
            print(nmap_result)
            print("\nNmap operation completed.\n") #Nmap işlemi tamamlandı
            input("Press Enter to continue...") #Devam etmek için Enter'a basın
        else:
            print("Invalid tool selection.") #Geçersiz araç seçimi
            input("Press Enter to continue...") #Devam etmek için Enter'a basın
    except ValueError:
        print("Invalid input. Please enter a number.") #Geçersiz giriş. Lütfen bir sayı girin.
        input("Press Enter to continue...") #Devam etmek için Enter'a basın