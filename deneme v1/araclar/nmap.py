# araclar/nmap.py
import subprocess

def nmap_tarama(hedef):
    try:
        sonuc = subprocess.run(["nmap", hedef], capture_output=True, text=True, check=True)
        return sonuc.stdout
    except subprocess.CalledProcessError as e:
        return f"Nmap hatası: {e.stderr}"
    except FileNotFoundError:
        return "Nmap bulunamadı. Lütfen Nmap'in yüklü olduğundan emin olun."
    except Exception as e:
        return f"Beklenmeyen bir hata oluştu: {e}"