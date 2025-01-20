from interface import clear_screen, print_header
from tools import nmap

def reconnaissance_menu():
    """Handles the reconnaissance stage menu and Nmap scans."""
    clear_screen()
    print_header("1. RECONNAISSANCE", "Reconnaissance Stage - Optimized Nmap Usage")
    print("1. Nmap Scan")

    try:
        tool_choice = int(input("Select a tool: "))
        if tool_choice == 1:
            target = input("Taranacak hedefi girin (URL, IP adresi, IP aralığı veya alt ağ; Örn: scanme.nmap.org, 192.168.1.1, 192.168.1.0/24, 192.168.1.1-10): ")
            secilen_parametreler = nmap.nmap_parametre_secimi()
            arguments = " ".join(secilen_parametreler)
            print(f"Starting Nmap scan: {target} {arguments}...\n")
            nmap_result = nmap.nmap_tarama(target, secilen_parametreler)
            print(nmap_result)
            print("\nNmap operation completed.\n")
            input("Press Enter to continue...")
            return {
                "stage": "Reconnaissance",
                "tool": "Nmap",
                "target": target,
                "arguments": arguments,
                "result": nmap_result
            }
        else:
            print("Invalid tool selection.")
            input("Press Enter to continue...")
            return None
    except ValueError:
        print("Invalid input. Please enter a number.")
        input("Press Enter to continue...")
        return None