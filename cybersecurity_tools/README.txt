#######################################################################################################
#                                2.0 FLASH EXPERIMENTAL - MODÜLERLEŞME                                #
#                                                                                                     #
# Bu güncellemede, araçların ve aşamaların daha modüler bir yapıda organize edilmesi sağlanmıştır.     #
# Dosya yapısı aşağıdaki gibi düzenlenmiştir:                                                         #
#                                                                                                     #
# **Proje Dosya Yapısı:**                                                                            #
#                                                                                                     #
# siber_guvenlik_araci/                                                                              #
# ├── ana.py          # Ana kod dosyası (menü ve akış kontrolü)                                       #
# ├── arayuz.py       # Arayüz fonksiyonları (ekran temizleme, başlık yazdırma vb.)                   #
# └── asamalar/      # Aşamaların bulunduğu klasör                                                    #
#     ├── __init__.py # Paket tanımlama dosyası                                                       #
#     ├── kesif.py    # Keşif (Reconnaissance) aşaması                                               #
#     ├── tarama.py   # Tarama (Scanning) aşaması                                                    #
#     ├── erisim.py   # Erişim Sağlama (Gaining Access) aşaması                                       #
#     ├── hak_yukseltme.py # Hak Yükseltme (Privilege Escalation) aşaması                             #
#     ├── iz_surme.py # İz Sürmeyi Engelleme (Covering Tracks) aşaması                                #
#     └── bilgi_cikarma.py # Bilgi Çıkarma ve Kapatma aşaması                                         #
# └── araclar/       # Araçların bulunduğu klasör                                                     #
#     ├── __init__.py # Paket tanımlama dosyası                                                       #
#     ├── nmap.py    # Nmap aracı                                                                    #
#     ├── shodan.py  # Shodan aracı                                                                  #
#     ├── maltego.py # Maltego aracı                                                                 #
#     ├── nikto.py   # Nikto aracı                                                                   #
#     ├── owasp_zap.py # OWASP ZAP aracı                                                             #
#     ├── metasploit.py # Metasploit aracı                                                           #
#     └── burp_suite.py # Burp Suite aracı                                                           #
#                                                                                                     #
# **Yeni Özellikler ve Yapı:**                                                                       #
#                                                                                                     #
# 1. **Ana Modüller:**                                                                               #
#    - `ana.py`: Menü ve akış kontrolünün bulunduğu ana dosya. Kullanıcı girişi ve aşamalar buradan   #
#      kontrol edilir.                                                                                #
#    - `arayuz.py`: Ekran temizleme, başlık yazdırma ve görsel düzenleme işlemleri için kullanılır.    #
#                                                                                                     #
# 2. **Aşamalar (asamalar/):**                                                                       #
#    - Her saldırı aşaması kendi dosyasında organize edilmiştir. Bu, farklı saldırı aşamalarının      #
#      bağımsız bir şekilde yönetilmesini sağlar.                                                     #
#                                                                                                     #
# 3. **Araçlar (araclar/):**                                                                         #
#    - Nmap, Shodan, Maltego, Nikto, OWASP ZAP, Metasploit ve Burp Suite gibi araçlar kendi           #
#      dosyalarında organize edilmiştir. Bu modüler yapı, araçların farklı projelerde kolayca         #
#      yeniden kullanılmasını sağlar.                                                                #
#                                                                                                     #
# **Avantajları:**                                                                                   #
#                                                                                                     #
# 1. **Modülerlik:**                                                                                 #
#    - Kod daha düzenli ve parçalanmış hale gelir.                                                    #
# 2. **Okunabilirlik:**                                                                              #
#    - Her aracın ve aşamanın kendi dosyasında olması kodun okunabilirliğini artırır.                 #
# 3. **Yeniden Kullanılabilirlik:**                                                                  #
#    - Araçlar ve aşamalar farklı projelerde tekrar kullanılabilir.                                  #
# 4. **Bakım Kolaylığı:**                                                                            #
#    - Kodun güncellenmesi ve bakımı daha basit hale gelir.                                           #
# 5. **Genişletilebilirlik:**                                                                        #
#    - Yeni araçlar veya aşamalar kolayca eklenebilir.                                                #
#                                                                                                     #
# **Sonuç:**                                                                                         #
# - Proje dosya yapısı daha temiz, düzenli ve sürdürülebilir hale getirilmiştir.                      #
# - Kod organizasyonu ve kullanım kolaylığı açısından daha iyi bir çözüm sunulmuştur.                #
#######################################################################################################

---------

#######################################################################################################
#                                      PROJECT FILE STRUCTURE                                         #
#                                                                                                     #
# The project is organized with a modular structure for better readability, maintainability, and      #
# reusability. Below is the detailed file structure with descriptions:                                #
#                                                                                                     #
# cybersecurity_tools/                                                                                #
# ├── main.py        # Main script that handles the menu and flow control                             #
# ├── interface.py   # Interface functions (e.g., screen clearing, header formatting)                 #
# └── stages/        # Directory containing different attack stages                                   #
#     ├── __init__.py # Package initialization file                                                   #
#     ├── reconnaissance.py  # Reconnaissance phase                                                  #
#     ├── scanning.py       # Scanning phase                                                         #
#     ├── gaining_access.py # Gaining access phase                                                   #
#     ├── privilege_escalation.py # Privilege escalation phase                                       #
#     ├── covering_tracks.py # Covering tracks phase                                                 #
#     └── information_gathering.py # Information extraction and cleanup phase (more descriptive)     #
# └── tools/         # Directory containing tools                                                    #
#     ├── __init__.py # Package initialization file                                                   #
#     ├── nmap.py    # Nmap tool implementation                                                      #
#     ├── shodan.py  # Shodan tool implementation                                                    #
#     ├── maltego.py # Maltego tool implementation                                                   #
#     ├── nikto.py   # Nikto tool implementation                                                     #
#     ├── owasp_zap.py # OWASP ZAP tool implementation                                               #
#     ├── metasploit.py # Metasploit tool implementation                                             #
#     └── burp_suite.py # Burp Suite tool implementation                                             #
#                                                                                                     #
# **Advantages of the Structure:**                                                                   #
#                                                                                                     #
# 1. **Modularity:** Each tool and stage is organized in its own file, making the code more           #
#    manageable and reusable.                                                                         #
# 2. **Clarity:** The separation of concerns improves the readability and maintainability of the      #
#    codebase.                                                                                        #
# 3. **Expandability:** New tools and stages can be easily added without disrupting the existing      #
#    structure.                                                                                       #
#                                                                                                     #
# This structure ensures a clean, organized, and scalable project environment for cybersecurity       #
# tools and methodologies.                                                                            #
#######################################################################################################