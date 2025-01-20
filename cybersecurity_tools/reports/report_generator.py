import datetime
import os

def generate_report(data):
    """Verilen verileri kullanarak biçimlendirilmiş bir rapor oluşturur.

    Args:
        data (dict): Rapor verilerini içeren bir sözlük. Şunları içermelidir:
            'stage': Aşama adı (Örn: "1. Adım").
            'stage_name': Aşama Açıklaması (Örn: "KEŞİF").
            'tool': Kullanılan araç (Örn: "Nmap").
            'target': Hedef (Örn: "scanme.nmap.org").
            'arguments': Kullanılan argümanlar (Örn: "-sn -vv -sV").
            'result': Aracın çıktısı.

    Returns:
        str: Biçimlendirilmiş rapor metni.
    """
    now = datetime.datetime.now()
    tarih_saat = now.strftime("%Y-%m-%d %H:%M:%S")

    report = "==================================================\n"
    report += f"Tarih/Saat: {tarih_saat}\n\n"
    report += ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n"
    report += f"**{data['stage']}: {data.get('stage_name', '')}**\n"
    report += f"**Araç: {data['tool']}**\n"
    report += f"Hedef: {data['target']}**\n"
    report += f"Kullanılan Parametreler: {data['arguments']}\n"
    report += "<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n\n"
    report += "Nmap Çıktısı:\n"  # "Sonuç:" yerine "Nmap Çıktısı:"
    report += "<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n"
    report += data['result'] + "\n"
    report += "==================================================\n"
    return report

def save_report_to_file(report, filename="report.txt", reports_dir="reports"):
    """Oluşturulan raporu belirtilen dizine kaydeder.

    Args:
        report (str): Kaydedilecek rapor metni.
        filename (str, optional): Rapor dosyasının adı. Varsayılan: "report.txt".
        reports_dir (str, optional): Raporların kaydedileceği dizin. Varsayılan: "reports".
    """
    try:
        if not os.path.exists(reports_dir):
            os.makedirs(reports_dir)  # Klasör yoksa oluştur
        filepath = os.path.join(reports_dir, filename)
        with open(filepath, "w", encoding="utf-8") as file:
            file.write(report)
        print(f"Rapor {filepath} dosyasına kaydedildi.")
    except Exception as e:
        print(f"Rapor kaydedilirken bir hata oluştu: {e}")