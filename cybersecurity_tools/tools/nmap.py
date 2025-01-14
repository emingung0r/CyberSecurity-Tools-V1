# tools/nmap.py
import subprocess

def nmap_scan(target, arguments=""):
    """Performs an Nmap scan.
    Bir Nmap taraması gerçekleştirir."""
    try:
        command = ["nmap"]
        if arguments:
            command.extend(arguments.split())
        command.append(target)
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Nmap error: {e.stderr}" #Nmap hatası
    except FileNotFoundError:
        return "Nmap not found. Please ensure Nmap is installed." #Nmap bulunamadı. Lütfen Nmap'in yüklü olduğundan emin olun.
    except Exception as e:
        return f"An unexpected error occurred: {e}" #Beklenmeyen bir hata oluştu