# stages/reconnaissance.py
from interface import clear_screen, print_header
from tools import nmap

def reconnaissance_menu():
    """Handles the reconnaissance stage menu and Nmap scans.
    Keşif aşaması menüsünü ve Nmap taramalarını yönetir."""
    clear_screen()
    print_header("1. RECONNAISSANCE", "Reconnaissance Stage - Nmap Usage")
    print("1. Nmap Scan")
    try:
        tool_choice = int(input("Select a tool: "))
        if tool_choice == 1:
            target = input("Enter target to scan: ")
            arguments = input("Enter additional arguments (leave blank if none): ")
            print(f"Starting Nmap scan: {target}...\n")
            nmap_result = nmap.nmap_scan(target, arguments)
            print(nmap_result)
            print("\nNmap operation completed.\n")
            input("Press Enter to continue...")
            return { # Sonuçları dictionary olarak döndür
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