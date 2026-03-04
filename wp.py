import pandas as pd
import pywhatkit as kit
import time
import re


excel_file = 'uyeler.xlsx' 
df = pd.read_excel(excel_file)

grup_linki = "https://chat.whatsapp.com/CBfDqZ1ZY7C5hTZRBAtCn3?mode=gi_t"

def format_phone(phone):
    # Sayı olmayan her şeyi (boşluk, parantez, tire) temizle
    clean_phone = re.sub(r'\D', '', str(phone))
    
    # Eğer numara '05' ile başlıyorsa '0'ı atıp '+90' ekle
    if clean_phone.startswith('05'):
        return '+90' + clean_phone[1:]
    # Eğer direkt '5' ile başlıyorsa '+90' ekle
    elif clean_phone.startswith('5'):
        return '+90' + clean_phone
    # Eğer zaten '90' ile başlıyorsa sadece '+' ekle
    elif clean_phone.startswith('90'):
        return '+' + clean_phone
    return None

for index, row in df.iterrows():
    raw_phone = row['Telefon']
    formatted_phone = format_phone(raw_phone)
    isim = row['Ad'] 

    if formatted_phone:
        try:
            print(f"Gönderiliyor: {isim} ({formatted_phone})")
            # Mesajı gönder ve sekmeyi 2 saniye sonra kapat
            kit.sendwhatmsg_instantly(
                formatted_phone, f"UBİTEK Ailesine Hoş Geldin! 🚀 \n (Bu bir otomatik mesajdır.)\n\n {isim} Merhaba, Uzay bilimlerini ve teknolojilerini sadece bir ilgi alanı değil, onu yorumlayıp yeniden inşa etmeyi hedefleyen topluluğumuza hoş geldin. Astrobiyolojiden astrofiziğe; teorik derinliğinden mühendisliğin pratik uygulamalarına uzanan bu yolculukta, akademik disiplini ve sanayi üretimini samimiyetle birleştirerek ortak bir değer üretmeyi hedefliyoruz. Bilimsel vizyonla pekiştireceğimiz projelerimizde senin fikri katkın ve enerjin bizim için oldukça kıymetli. Süreci yakından takip etmek ve bu kozmik ekibin aktif bir parçası olmak için aşağıdaki iletişim kanalımız katılımını bekliyoruz. Gökyüzü bir limit değil,  UBİTEK ailesinin başlangıç noktasıdır. 🌌 \n \n 🔗 Grup Linki: {grup_linki}", 
                15, True, 2
            )
            # WhatsApp'ın bot olarak işaretlememesi için güvenli bekleme süresi
            time.sleep(20) 
        except Exception as e:
            print(f"Hata oluştu ({isim}): {e}")
