# Kullanıcının yaşını girerek kaç yıl sonra 100 yaşına ulaşacağını hesaplayan fonksiyon
from datetime import datetime

def age_100(age):
    return 100 - age

age = int(input("Lütfen yaşınızı giriniz: "))
if 0 <= age <= 120:
    years_left = age_100(age)
    current_year = datetime.now().year
    target_year = current_year + years_left
    if years_left > 0:
        print(f"100 yaşına ulaşmanıza {years_left} yıl kaldı.")
        print(f"100 yaşına {target_year} yılında ulaşacaksınız.")
    else:
        years_left < 0
        print(f"100 yaşına {abs(years_left)} yıl önce, {target_year} yılında ulaşmıştınız.")
else:
    print("Geçerli bir yaş giriniz (0-120 arası).")
