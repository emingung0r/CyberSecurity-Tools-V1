import os

def clear_screen():
    """Ekranı temizler."""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header(title, subtitle=None):
    """Başlık ve alt başlık yazdırır."""
    clear_screen()
    width = 80  # Sabit genişlik
    print("=" * width)
    print(f"{title:^{width}}")  # Başlığı ortalar
    if subtitle:
        print(f"{subtitle:^{width}}")  # Alt başlığı ortalar
    print("=" * width)
    print()  # Ekstra boşluk ekler

def print_section_header(title):
    """Alt başlık yazdırır."""
    width = 80
    print("\n" + "=" * width)
    print(f"{title:^{width}}")
    print("=" * width)

def print_menu(menu_items):
    """Menü öğelerini yazdırır."""
    for key, value in menu_items.items():
        print(f"{key}. {value}")

def print_installation_menu(items, item_type="Araçlar"):
    """Kurulum menüsünü yazdırır."""
    print_section_header(f"Kurulacak {item_type}")
    print()
    for i, item in enumerate(items, 1):
        print(f"{i}. {item}")
    print("\nSeçenekler:")
    print("- Belirli öğeler için: Numaraları virgülle ayırarak girin (örn: 1,2,3)")
    print("- Tüm öğeler için: 't' girin")
    print("- İptal etmek için: 'q' girin")
    
    return input("\nSeçiminiz > ").strip().lower()

def print_status(message, success=True):
    """Durum mesajı yazdırır."""
    icon = "✅" if success else "❌"
    print(f"{icon} {message}")

def print_tool_status(tool_name, description, is_installed, message=""):
    """Araç durumunu yazdırır."""
    status = "kurulu" if is_installed else message
    icon = "✅" if is_installed else "❌"
    print(f"{icon} {tool_name} ({description}) - {status}")

def print_module_status(module_name, is_installed, message=""):
    """Modül durumunu yazdırır."""
    status = "Kurulu" if is_installed else message
    icon = "✅" if is_installed else "❌"
    print(f"{icon} {module_name}: {status}")

def wait_for_user():
    """Kullanıcıdan devam etmek için giriş bekler."""
    print("\n" + "-" * 80)
    input("Devam etmek için Enter'a basın...")