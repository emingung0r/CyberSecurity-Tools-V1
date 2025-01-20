import subprocess
import re

def nmap_tarama(hedef, parametreler=None):
    """Nmap taramasını gerçekleştirir ve Nmap uyarılarını yakalar."""
    command = ["nmap"]
    if parametreler:
        command.extend(parametreler)
    command.append(hedef)
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=False)
        if result.returncode != 0:
            uyarilar = re.findall(r"Warning: (.+)", result.stderr)
            hatalar = re.findall(r"ERROR: (.+)", result.stderr)
            mesaj = f"Nmap komutu başarısız oldu. Çıkış Kodu: {result.returncode}\n"
            if hatalar:
                mesaj += "Hatalar:\n" + "\n".join(hatalar)
            if uyarilar:
                mesaj += "Uyarilar:\n" + "\n".join(uyarilar)
            else:
                mesaj += "Hata çıktısı yok"
            return mesaj
        return result.stdout
    except FileNotFoundError:
        return "Nmap bulunamadı. Lütfen Nmap'in yüklü olduğundan emin olun."
    except Exception as e:
        return f"Beklenmeyen bir hata oluştu: {e}"

def nmap_parametre_secimi():
    """Nmap parametrelerini seçmek için menü gösterir ve çakışmaları önler."""
    print("\nNmap Parameter Selection (Optimized) / Nmap Parametre Seçimi (Optimize Edilmiş):")
    print("-----------------------------------")
    print("{:<5} {:<15} {:<60}".format("#", "Parameters", "Description"))
    print("{:<5} {:<15} {:<60}".format("--", "--------", "-----------"))

    parametreler = {
        1: ("-sn", "Host discovery - Ping scan. Determines if the target is online.", "Host tespiti - Ping taraması. Hedefin çevrimiçi olup olmadığını belirler."),
        2: ("-F", "Fast scan - Scans fewer ports than the default scan.", "Hızlı tarama - Varsayılan taramadan daha az port tarar."),
        3: ("-sV", "Service/version detection - Determines service and version information on open ports.", "Servis/sürüm tespiti - Açık portlardaki servis ve sürüm bilgilerini belirler."),
        4: ("-O", "OS detection - Attempts to guess the target operating system.", "İşletim sistemi tespiti - Hedef işletim sistemini tahmin etmeye çalışır."),
        5: ("-p-", "Scan all ports - Scans all 65535 ports (Can be very time-consuming!).", "Tüm portları tara - 65535 portun tamamını tarar (Çok zaman alabilir!)."),
        6: ("-p <ports>", "Scan specific ports - Example: -p22,80,443", "Belirli portları tara - Örnek: -p22,80,443"),
        7: ("-sC", "Script scan - Runs default Nmap scripts (Works well with -sV).", "Script taraması - Varsayılan Nmap scriptlerini çalıştırır (sV ile iyi çalışır)."),
        8: ("-sS", "SYN Scan", "SYN Taraması"),
        9: ("-sU", "UDP Scan", "UDP Taraması"),
        10: ("-sA", "ACK Scan", "ACK Taraması"),
        11: ("-sW", "Window Scan", "Pencere Taraması"),
        12: ("-sM", "Maimon Scan", "Maimon Taraması"),
        0: ("Custom", "Enter custom Nmap parameters.", "Özel Nmap parametreleri girin.")
    }

    for key, (param, desc_en, desc_tr) in parametreler.items():
        print("{:<5} {:<15} {:<60}".format(key, param, desc_en))
        print("{:<5} {:<15} {:<60}".format("", "", desc_tr))
        print()

    print("-----------------------------------")

    tarama_turleri = {"-sS", "-sT", "-sU", "-sA", "-sW", "-sM", "-sn"}
    servis_tespiti = {"-sV"}
    isletim_sistemi_tespiti = {"-O"}
    script_taramasi = {"-sC"}
    zamanlama = {"-T0", "-T1", "-T2", "-T3", "-T4", "-T5"}

    uyumsuzluklar = [
        (tarama_turleri, tarama_turleri),
        (set(["-sn"]), servis_tespiti),
        (set(["-sn"]), isletim_sistemi_tespiti),
        (set(["-sn"]), script_taramasi),
        (set(["-sU"]), set(["-sS", "-sT", "-sA", "-sW", "-sM"])),
        (zamanlama, zamanlama)
    ]

    secilen_parametreler = []
    secilen_gruplar = set()

    while True:
        try:
            secim = input("Select a scan type (Enter to finish): ")
            if secim == "":
                break
            elif secim == "0":
                arguments = input("Enter your custom Nmap parameters (e.g., -sU -A -T4): ")
                secilen_parametreler.extend(arguments.split())
                for arg in secilen_parametreler:
                    for grup in (tarama_turleri, servis_tespiti, isletim_sistemi_tespiti, script_taramasi, zamanlama):
                        if arg in grup:
                            secilen_gruplar.add(frozenset(grup))
                            break

                break

            elif secim.isdigit():
                secim = int(secim)
                if secim in parametreler:
                    parametre = parametreler[secim][0]
                    uyumsuzluk_var = False
                    for grup, uyumsuz_grup in uyumsuzluklar:
                        if parametre in grup and not grup.isdisjoint(secilen_gruplar):
                            print(f"Uyarı: {parametre} parametresi seçilen diğer parametrelerle uyumlu değil.")
                            uyumsuzluk_var = True
                            break
                    if not uyumsuzluk_var:
                        for grup in (tarama_turleri, servis_tespiti, isletim_sistemi_tespiti, script_taramasi, zamanlama):
                            if parametre in grup:
                                secilen_gruplar.add(frozenset(grup))
                                break
                        if parametre == "-p":
                            while True:
                                portlar = input("Enter ports to scan (e.g., 22,80,443): ")
                                try:
                                    for port in portlar.split(','):
                                        int(port)
                                        if not 0 <= int(port) <= 65535:
                                            raise ValueError
                                    break
                                except ValueError:
                                    print("Invalid port entry. Please enter comma-separated numbers between 0-65535.")
                            secilen_parametreler.append(f"-p{portlar}")
                        else:
                            secilen_parametreler.append(parametre)
                else:
                    print("Invalid selection. Please choose from the list.")
            else:
                print("Invalid input. Please enter a number or 'Custom'.")
        except ValueError:
            print("Invalid input.")

    return secilen_parametreler