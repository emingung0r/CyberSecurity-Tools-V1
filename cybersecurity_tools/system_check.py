import subprocess
import platform
import importlib
import sys
import logging
import os
from interface import clear_screen, print_header

# Configure logging
logging.basicConfig(
    filename='reports/app.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    encoding="utf-8"
)

def setup_environment():
    """Uygulama için gerekli ortamı hazırlar."""
    try:
        # reports klasörünü oluştur
        os.makedirs("reports", exist_ok=True)
        logging.info("Çalışma ortamı başarıyla hazırlandı.")
        return True
    except Exception as e:
        logging.error(f"Ortam hazırlanırken hata oluştu: {e}")
        return False

def check_tool(tool_name, command):
    """Check if a specific tool is installed."""
    try:
        subprocess.run([command, "--version"], capture_output=True, text=True, check=True)
        return True, ""
    except FileNotFoundError:
        return False, f"{tool_name} bulunamadı. Lütfen {tool_name}'ı yükleyin."
    except Exception as e:
        logging.exception(f"{tool_name} kontrol edilirken hata oluştu: {e}")
        return False, f"{tool_name} kontrol edilirken hata oluştu: {e}"

def check_python_module(module_name, package_name):
    """Check if a Python module is installed."""
    try:
        importlib.import_module(module_name)
        return True, ""
    except ModuleNotFoundError:
        return False, f"{module_name} bulunamadı. Kurulum için: pip install {package_name}"
    except Exception as e:
        logging.exception(f"{module_name} modülü kontrol edilirken hata oluştu: {e}")
        return False, f"{module_name} modülü kontrol edilirken hata oluştu: {e}"

def install_package(package_name, verbose=False):
    """Install a Python package."""
    try:
        if verbose:
            subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])
        else:
            subprocess.check_call([sys.executable, "-m", "pip", "install", package_name],
                                stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
        print(f"✅ {package_name} başarıyla kuruldu.")
        logging.info(f"{package_name} başarıyla kuruldu.")
        return True
    except subprocess.CalledProcessError as e:
        logging.error(f"{package_name} kurulurken hata oluştu: {e}")
        print(f"❌ {package_name} kurulurken hata oluştu: {e}")
        return False
    except Exception as e:
        logging.exception(f"{package_name} kurulumu sırasında beklenmeyen bir hata oluştu: {e}")
        print(f"❌ {package_name} kurulumu sırasında beklenmeyen bir hata oluştu: {e}")
        return False

def install_tool(tool_name, verbose=False):
    """Install a specific tool."""
    try:
        if tool_name == "Shodan":
            return install_package("shodan", verbose)
        elif tool_name == "Nikto":
            if platform.system() == "Linux":
                subprocess.check_call(["sudo", "apt-get", "install", "-y", "nikto"])
            elif platform.system() == "Darwin":
                subprocess.check_call(["brew", "install", "nikto"])
            else:
                print("Nikto kurulumu için: https://cirt.net/Nikto2/ adresinden indirin ve PATH'e ekleyin.")
                return False
            print(f"✅ Nikto başarıyla kuruldu.")
            logging.info("Nikto başarıyla kuruldu.")
            return True
        elif tool_name == "OWASP ZAP":
            print("OWASP ZAP kurulumu için: https://owasp.org/www-project-zap/ adresinden indirin.")
            return False
        elif tool_name == "Metasploit":
            if platform.system() == "Linux":
                subprocess.check_call([
                    "curl",
                    "https://raw.githubusercontent.com/rapid7/metasploit-framework/master/metasploit-framework.sh",
                    "-o", "msfinstall.sh"
                ])
                subprocess.check_call(["chmod", "+x", "msfinstall.sh"])
                subprocess.check_call(["./msfinstall.sh"])
            elif platform.system() == "Darwin":
                subprocess.check_call(["brew", "install", "metasploit"])
            else:
                print("Metasploit kurulumu için: https://windows.metasploit.com/ adresinden indirin.")
                return False
            print(f"✅ Metasploit başarıyla kuruldu.")
            logging.info("Metasploit başarıyla kuruldu.")
            return True
        elif tool_name == "Burp Suite":
            print("Burp Suite kurulumu için: https://portswigger.net/burp/freedownload adresinden indirin.")
            return False
        elif tool_name == "Nmap":
            if platform.system() == "Linux":
                subprocess.check_call(["sudo", "apt-get", "install", "-y", "nmap"])
            elif platform.system() == "Darwin":
                subprocess.check_call(["brew", "install", "nmap"])
            else:
                print("Nmap kurulumu için: https://nmap.org/download.html adresinden indirin ve PATH'e ekleyin.")
                return False
            print(f"✅ Nmap başarıyla kuruldu.")
            logging.info("Nmap başarıyla kuruldu.")
            return True
        else:
            print(f"{tool_name} için otomatik kurulum desteklenmiyor.")
            return False
    except subprocess.CalledProcessError as e:
        logging.error(f"{tool_name} kurulurken bir hata oluştu: {e}")
        print(f"❌ {tool_name} kurulurken bir hata oluştu: {e}")
        return False
    except Exception as e:
        logging.exception(f"{tool_name} kurulumu sırasında beklenmeyen bir hata oluştu: {e}")
        print(f"❌ {tool_name} kurulumu sırasında beklenmeyen bir hata oluştu: {e}")
        return False

def check_system():
    """Check if required tools and Python modules are installed on the system."""
    clear_screen()
    print_header("Sistem ve Modül Kontrolü")
    print("=" * 19)
    print("Sistem Araçları Kontrolü:")
    print("=" * 19)

    tools_info = {
        "Nmap": {"command": "nmap", "description": "Ağ tarayıcısı"},
        "Shodan": {"command": "shodan", "description": "İnternet cihaz arama motoru"},
        "Nikto": {"command": "nikto", "description": "Web sunucu tarayıcısı"},
        "OWASP ZAP": {"command": "zap-cli", "description": "Web uygulama güvenlik tarayıcısı"},
        "Metasploit": {"command": "msfconsole", "description": "Sızma testi çerçevesi"},
        "Burp Suite": {"command": "burpsuite", "description": "Web uygulama güvenlik test platformu"}
    }
    missing_tools = []

    for tool_name, info in tools_info.items():
        is_installed, message = check_tool(tool_name, info["command"])
        if not is_installed:
            print(f"❌ {tool_name} ({info['description']}) - {message}")
            missing_tools.append(tool_name)
        else:
            print(f"✅ {tool_name} ({info['description']}) kurulu.")

    print("\n" + "=" * 19)
    print("Python Modülleri Kontrolü:")
    print("=" * 19)

    modules_info = {
        "PyPDF2": {"package_name": "PyPDF2"},
        "reportlab": {"package_name": "reportlab"},
        "python-docx": {"package_name": "python-docx"},
        "pypdf2": {"package_name": "pypdf2"}
    }
    missing_modules = []

    for module_name, info in modules_info.items():
        is_installed, message = check_python_module(module_name, info["package_name"])
        if not is_installed:
            print(f"❌ {module_name}: {message}")
            missing_modules.append(module_name)
        else:
            print(f"✅ {module_name}: Kurulu")

    if missing_tools or missing_modules:
        print("\nEksik araçlar/modüller bulundu. Kurulum yapmak ister misiniz? (e/h)")
        install_choice = input("> ").lower()
        if install_choice == "e":
            if missing_tools:
                print("\nKurulacak Araçlar:")
                for i, tool in enumerate(missing_tools, 1):
                    print(f"{i}. {tool}")
                tool_choices = input("Kurmak istediğiniz araçların numaralarını virgülle ayırarak girin (örn: 1,2,3) veya tümünü kurmak için 't': ")
                
                if tool_choices.lower() == 't':
                    tools_to_install = missing_tools
                else:
                    try:
                        tool_indices = [int(x.strip()) - 1 for x in tool_choices.split(',')]
                        tools_to_install = [missing_tools[i] for i in tool_indices if 0 <= i < len(missing_tools)]
                    except (ValueError, IndexError):
                        print("Geçersiz giriş.")
                        return

                for tool in tools_to_install:
                    print(f"\n{tool} kuruluyor...")
                    install_tool(tool, verbose=True)

            if missing_modules:
                print("\nKurulacak Modüller:")
                for i, module in enumerate(missing_modules, 1):
                    print(f"{i}. {module}")
                module_choices = input("Kurmak istediğiniz modüllerin numaralarını virgülle ayırarak girin (örn: 1,2) veya tümünü kurmak için 't': ")
                
                if module_choices.lower() == 't':
                    modules_to_install = missing_modules
                else:
                    try:
                        module_indices = [int(x.strip()) - 1 for x in module_choices.split(',')]
                        modules_to_install = [missing_modules[i] for i in module_indices if 0 <= i < len(missing_modules)]
                    except (ValueError, IndexError):
                        print("Geçersiz giriş.")
                        return

                for module in modules_to_install:
                    print(f"\n{module} kuruluyor...")
                    install_package(modules_info[module]["package_name"], verbose=True)
        else:
            print("Kurulum yapılmadı.")
    
    input("\nDevam etmek için Enter'a basın...")

if __name__ == "__main__":
    # Create reports directory if it doesn't exist
    os.makedirs("reports", exist_ok=True)
    check_system()