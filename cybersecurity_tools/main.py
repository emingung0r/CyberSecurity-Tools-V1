# main.py
from interface import clear_screen, print_header
from stages import reconnaissance

def main_menu():
    """Displays the main menu.
    Ana menüyü görüntüler."""
    clear_screen()
    print_header("CYBERSECURITY TERMINAL TOOL")
    print("1. Reconnaissance") #Keşif
    print("0. Exit\n") #Çıkış
    try:
        choice = int(input("Select a stage (0 to exit): ")) #Bir aşama seçin
        return choice
    except ValueError:
        print("Invalid input. Please enter a number.") #Geçersiz giriş. Lütfen bir sayı girin.
        input("Press Enter to continue...") #Devam etmek için Enter'a basın
        return -1

while True:
    choice = main_menu()
    if choice == 0:
        print("Exiting the program.") #Programdan çıkılıyor
        break
    elif choice == 1:
        reconnaissance.reconnaissance_menu() #Keşif menüsünü çağır
    elif choice == -1:
        continue
    else:
        print("Invalid selection.") #Geçersiz seçim
        input("Press Enter to continue...") #Devam etmek için Enter'a basın