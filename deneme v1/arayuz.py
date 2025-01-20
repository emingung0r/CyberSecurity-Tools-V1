# arayuz.py
import os

def ekran_temizle():
    os.system('cls' if os.name == 'nt' else 'clear')

def baslik_yazdir(baslik, alt_baslik=None):
    try:
        ekran_genisligi = os.get_terminal_size().columns
    except OSError:
        ekran_genisligi = 80
    cizgi = "=" * ekran_genisligi

    baslik_bosluk = (ekran_genisligi - len(baslik)) // 2
    baslik_ortali = ' ' * baslik_bosluk + baslik + ' ' * baslik_bosluk

    cerceveli_baslik = f"{cizgi}\n{baslik_ortali}\n"

    if alt_baslik:
        ayrac = "-" * ekran_genisligi
        alt_baslik_bosluk = (ekran_genisligi - len(alt_baslik)) // 2
        alt_baslik_ortali = ' ' * alt_baslik_bosluk + alt_baslik + ' ' * alt_baslik_bosluk
        cerceveli_baslik += f"{ayrac}\n{alt_baslik_ortali}\n"
    cerceveli_baslik += f"{cizgi}\n"
    print(cerceveli_baslik)