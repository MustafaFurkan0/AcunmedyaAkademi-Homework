# built-in modules -> pythona yüklü gelen (math, date)
# local modules -> projede bizim ürettiğimiz dosyalar (oop.py)
# 


#
#import math # math kütüphanesini komple import et
from math import sqrt as karekök , cos # sadece istediğimizi yüklememiz lazım
# alias -> takma ad

#import oop
import requests

#print(math.sqrt(25))
print(karekök(25))
print(cos(90))

#car1 = oop.Car("Volvo")
#car1.increase_speed(50)

response = requests.get("https://google.com")
print(response.status_code)
