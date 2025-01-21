from interface import clear_screen, print_header
from tools import nmap, shodan, maltego # İlgili araçlar import edildi

def reconnaissance_menu():
    clear_screen()
    print_header("1. RECONNAISSANCE", "Keşif Aşaması Araçları")
    print("1. Nmap Taraması")
    print("2. Shodan Taraması")
    print("3. Maltego Taraması") # Maltego eklendi
    # Diğer keşif araçları buraya eklenebilir

    while True:
        try:
            tool_choice = int(input("Bir araç seçin: "))
            if 1 <= tool_choice <= 3: # Geçerli seçenekler güncellendi
                break
            else:
                print("Geçersiz seçim. Lütfen 1-3 arasında bir sayı girin.")
        except ValueError:
            print("Lütfen bir sayı girin.")
    
    target = input("Taranacak hedefi girin: ")
    arguments = "" # Başlangıçta boş

    if tool_choice == 1:
        secilen_parametreler = nmap.nmap_parametre_secimi()
        arguments = " ".join(secilen_parametreler)
        print(f"Nmap taraması başlatılıyor: {target} {arguments}...\n")
        result = nmap.nmap_tarama(target, secilen_parametreler)
        tool_name = "Nmap"
    elif tool_choice == 2:
        print(f"Shodan taraması başlatılıyor: {target}...\n")
        result = shodan.shodan_tarama(target)
        tool_name = "Shodan"
    elif tool_choice == 3:
        print(f"Maltego taraması başlatılıyor: {target}...\n")
        result = maltego.maltego_tarama(target)
        tool_name = "Maltego"
    else: # Bu kısım gereksiz ama kalabilir
        result = "Geçersiz araç seçimi."
        tool_name = "Bilinmeyen Araç"

    return {
        "stage": "Reconnaissance",
        "tool": tool_name,
        "target": target,
        "arguments": arguments,
        "result": result
    }