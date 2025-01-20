import datetime
import os
import importlib
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from docx import Document

def check_library(library_name, import_name):
    try:
        importlib.import_module(import_name)
        return True
    except ModuleNotFoundError:
        return False

def generate_report(data, format="txt"):
    if format == "pdf" and not check_library("reportlab", "reportlab.pdfgen"):
        return "1001: PDF raporları oluşturmak için 'reportlab' kütüphanesi kurulu değil. pip install reportlab komutunu kullanın.",None
    elif format == "docx" and not check_library("python-docx", "docx"):
        return "1002: Word raporları oluşturmak için 'python-docx' kütüphanesi kurulu değil. pip install python-docx komutunu kullanın.",None
    now = datetime.datetime.now()
    tarih_saat = now.strftime("%Y-%m-%d %H:%M:%S")
    filename = f"cybersecurity_report_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.{format}"
    reports_dir = "reports"
    filepath = os.path.join(reports_dir, filename)

    if format == "txt":
        report = f"==================================================\n"
        report += f"Tarih/Saat: {tarih_saat}\n\n"
        report += f">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n"
        report += f"**{data['stage']}: {data.get('stage_name', '')}**\n"
        report += f"**Araç: {data['tool']}**\n"
        report += f"Hedef: {data['target']}**\n"
        report += f"Kullanılan Parametreler: {data['arguments']}\n"
        report += f"<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n\n"
        report += f"Sonuç:\n"
        report += f"<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n"
        report += data['result'] + "\n"
        report += f"==================================================\n"
        return filepath, report
    elif format == "pdf":
        try:
            c = canvas.Canvas(filepath, pagesize=letter)
            textobject = c.beginText(50, 750)
            textobject.textLines(f"Tarih/Saat: {tarih_saat}\n\n")
            textobject.textLines(f"Aşama: {data['stage']}: {data.get('stage_name', '')}\n")
            textobject.textLines(f"Araç: {data['tool']}\n")
            textobject.textLines(f"Hedef: {data['target']}\n")
            textobject.textLines(f"Parametreler: {data['arguments']}\n\n")
            textobject.textLines("Sonuç:\n")
            textobject.textLines(data['result'])
            c.drawText(textobject)
            c.save()
            return filepath,None
        except Exception as e:
            return f"2001: PDF raporu oluşturulurken bir hata oluştu: {e}",None

    elif format == "docx":
        try:
            document = Document()
            document.add_heading("Siber Güvenlik Raporu", level=1)
            document.add_paragraph(f"Tarih/Saat: {tarih_saat}")
            document.add_paragraph(f"Aşama: {data['stage']}: {data.get('stage_name', '')}")
            document.add_paragraph(f"Araç: {data['tool']}")
            document.add_paragraph(f"Hedef: {data['target']}")
            document.add_paragraph(f"Parametreler: {data['arguments']}")
            document.add_paragraph("Sonuç:")
            document.add_paragraph(data['result'])
            document.save(filepath)
            return filepath,None
        except Exception as e:
            return f"2002: DOCX raporu oluşturulurken bir hata oluştu: {e}",None
    else:
        return "Geçersiz format.",None

def save_report_to_file(report_content):
    if isinstance(report_content, tuple):
        filepath = report_content[0]
        report = report_content[1]
        if isinstance(filepath, str) and (filepath.startswith("1001:") or filepath.startswith("1002:") or filepath.startswith("2001:") or filepath.startswith("2002:")) :
            print(filepath)
            input("Devam etmek için Enter'a basın...")
            return
        try:
            reports_dir = "reports"
            if not os.path.exists(reports_dir):
                os.makedirs(reports_dir)
            if report is not None:
                with open(filepath, "w", encoding="utf-8") as file:
                    file.write(report)
            print(f"Rapor {filepath} dosyasına kaydedildi.")
        except Exception as e:
            print(f"Rapor kaydedilirken bir hata oluştu: {e}")
    else:
        print(report_content)
        input