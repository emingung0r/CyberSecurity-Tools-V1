from interface import clear_screen, print_header
from tools import nikto, owasp_zap

def scanning_menu():
    clear_screen()
    print_header("2. TARAMA AŞAMASI", "Tarama Aşaması Araçları")
    print("1. Nikto Taraması")
    print("2. OWASP ZAP Taraması")

    while True:
        try:
            tool_choice = int(input("Bir araç seçin: "))
            if 1 <= tool_choice <= 2:
                break
            else:
                print("Geçersiz seçim. Lütfen 1 veya 2 girin.")
        except ValueError:
            print("Lütfen bir sayı girin.")

    target = input("Taranacak hedefi girin: ")
    arguments = ""

    if tool_choice == 1:
        print(f"Nikto taraması başlatılıyor: {target}...\n")
        result = nikto.nikto_tarama(target)
        tool_name = "Nikto"
    elif tool_choice == 2:
        print(f"OWASP ZAP taraması başlatılıyor: {target}...\n")
        result = owasp_zap.owasp_zap_tarama(target)
        tool_name = "OWASP ZAP"
    else:
        result = "Geçersiz araç seçimi."
        tool_name = "Bilinmeyen Araç"
    
    return {
        "stage": "Scanning",
        "tool": tool_name,
        "target": target,
        "arguments": arguments,
        "result": result
    }