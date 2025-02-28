# fonksiyonlar - methotlar
# kodun yeniden kullanabilirliğini arttırmak ve bakımı kolaylaştırmak için kullanılır

price = 100
total_price = price + (price*0.2)
print(total_price)

# fonksiyon tanımlamak
#parametrre => fonksiyon çağrılma aşamasında verilen veri

# default parameter => rate = 20 -> rate gönderilen değeri, gönderilmez ise 20'i kullan
# required parameter, default parameter 
# default parameter, required parameter
def calculate_tax(price, rate=30):
    return price + (price * (rate / 100))

print("**********")
price1 = calculate_tax(100, 10) # print
price2 = calculate_tax(200, 20) # toplam fiyatı alıp başka bir değerle (kargo fiyatı) ile topla
price3 = calculate_tax(500)

print(price1)
print(price2 + 50)

print("**********")

def sum(*args): 
    if len(args) <= 0:
        raise ArithmeticError("En az 1 argüman zorunludur") #hata yönetimi
    total = 0
    for sayi in args:
        total += sayi
    return total
print(sum(1,2,3,3,4,5,8,7,9))
print(sum(1,2))
print(sum(5))
#print(sum())


# **kwargs -> araştırma ve uygulama 

def selamla(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

selamla(ad="Mustafa", soyad="Yılmaz", yas=25)

def kullanici_bilgisi(isim, **bilgiler):
    print(f"İsim: {isim}")
    for key, value in bilgiler.items():
        print(f"{key}: {value}")

kullanici_bilgisi("Mustafa", yas=22, sehir="Bursa", meslek="Mühendis")

# lamdba fpnksiyonları 
# tek satırlık fonksiyonları kısaca tanımlama yöntemi
topla = lambda a,b: a+b
selamla = lambda isim: print(f"Merhaba, {isim}")

print(topla(3,5))
print(selamla("Mustafa"))

#