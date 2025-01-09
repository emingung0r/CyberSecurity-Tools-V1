import os
import sys
import tkinter as tk
from tkinter import messagebox

# Adımlar ve araçlar
steps = {
    1: {"name": "Keşif (Reconnaissance)", "tools": ["Nmap", "Shodan", "Maltego"]},
    2: {"name": "Tarama (Scanning)", "tools": ["Nmap", "Nikto", "OWASP ZAP"]},
    3: {"name": "Erişim Sağlama (Gaining Access)", "tools": ["Metasploit Framework", "Burp Suite"]},
    4: {"name": "Hak Yükseltme (Privilege Escalation)", "tools": ["Tool1", "Tool2"]},
    5: {"name": "İz Sürmeyi Engelleme (Covering Tracks)", "tools": ["Tool3", "Tool4"]},
    6: {"name": "Bilgi Çıkarma ve Kapatma", "tools": ["Tool5", "Tool6"]},
}

# Kullanıcı seçimlerini kaydetmek için bir liste
user_selections = []

current_step = "Anasayfa"
def display_current_step():
    print("\n" + "=" * 50)
    # Mevcut adım ekrana büyük harflerle yazdırılır
    print(f"Adım: {current_step.upper()}\n")
    if current_step != "Anasayfa":
        for step_id, step_info in steps.items():
            # Kullanıcının seçtiği adım ve araç bilgisi dinamik olarak gösterilir
            if step_info["name"].split(" (")[0] in current_step:
                print(f"*{step_info['name']}* (Araçlar: {', '.join(step_info['tools'])})")
                break
    print("=" * 50)


def display_menu():
    print("\nSiber Güvenlik Adımları:")
    for step_id, step_info in steps.items():
        print(f"{step_id}. {step_info['name']}")
    print("7. Raporu Görüntüle")
    print("0. Çıkış")

def select_step():
    while True:
        try:
            step_id = int(input("\nBir adım seçin (0 için çıkış, 7 için rapor): "))
            if step_id == 0 or step_id == 7 or step_id in steps:
                return step_id
            else:
                print("Geçersiz seçim. Tekrar deneyin.")
        except ValueError:
            print("Lütfen bir Adım Tercih Edin.")

def select_tool(step_id):
    # Kullanıcının seçtiği adım için kullanılabilecek araçlar listelenir
    tools = steps[step_id]["tools"]
    print(f"\n{steps[step_id]['name']} için araçlar:")
    for idx, tool in enumerate(tools, 1):
        print(f"{idx}. {tool}")
    while True:
        try:
            # Kullanıcıdan bir araç seçmesi istenir
            tool_idx = int(input("Bir araç seçin: "))
            if 1 <= tool_idx <= len(tools):
                return tools[tool_idx - 1]  # Seçilen araç döndürülür
            else:
                print("Geçersiz seçim. Tekrar deneyin.")
        except ValueError:
            print("Lütfen bir sayı girin.")


def save_report():
    report = "\nSiber Güvenlik Süreç Raporu:\n"
    for step in user_selections:
        report += f"{step['step_name']} - Seçilen Araç: {step['tool']}\n"
    with open("siber_guvenlik_raporu.txt", "w") as file:
        file.write(report)
    print("\nRapor kaydedildi: siber_guvenlik_raporu.txt")

def display_report():
    if not user_selections:
        print("\nHenüz bir rapor oluşturulmadı.")
    else:
        print("\nSiber Güvenlik Süreç Raporu:")
        for step in user_selections:
            print(f"{step['step_name']} - Seçilen Araç: {step['tool']}")

def handle_error():
    root = tk.Tk()
    root.withdraw()  # Ana penceresini gizle
    messagebox.showerror("Hata", "Uygulama çalıştırılamadı. Lütfen tekrar deneyiniz.")
    root.destroy()

def main():
    global current_step
    print("Siber Güvenlik Terminal Aracı\n")
    try:
        while True:
            display_current_step()
            display_menu()
            step_id = select_step()
            if step_id == 0:
                print("\nProgramdan çıkış yapılıyor...")
                break
            elif step_id == 7:
                display_report()
            else:
                step_name = steps[step_id]["name"]
                current_step = step_name.split(" (")[0]
                tool = select_tool(step_id)
                user_selections.append({"step_name": step_name, "tool": tool})
                print(f"\n{step_name} için {tool} aracı seçildi ve çalıştırılıyor...")
                # Örnek terminal komutu (gerçek araçları çalıştırmak için kullanılabilir)
                # os.system(f"{tool.lower()}")
                print(f"{tool} işlemi tamamlandı.")
        save_report()
    except Exception as e:
        print(f"Bir hata oluştu: {e}")
        handle_error()
        main()  # Programı tekrar başlat

if __name__ == "__main__":
    main()
