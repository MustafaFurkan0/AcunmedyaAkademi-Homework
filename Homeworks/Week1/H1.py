print("Kodlamio")
baslik = "Taşıt Kredisi"
print(baslik)

#string => metinsel ifade
baslik = "İhtiyaç Kredisi"
print(baslik)

#int, integer => tam sayı
vade = 36
ekVade = 6 
vade2 = "36"

#float, decimal, double 
ayliködeme = 200.50

#bool boolean => True veya False
yukselisteMi = False

# matematiksel operatörler 
# +
print(5 + 5)
print(vade + 12)
print(vade + ekVade)
print(36 + 6)

# -
print(5 - 5)
print(vade - 12)
print(vade - ekVade)
print(36 - 6)

# *
print(5 * 5)
print(vade * 2)
print(vade * ekVade)
print(10 * 10)

# /
print(5 / 5)
print(vade / 2)
print(vade / ekVade)
print(10 / 2)


yeniVade = vade / 2
fiyat = 100
indirimliFiyat = fiyat - 20

print(yeniVade)
print(indirimliFiyat)

# % => mod operatör
print(10 % 2)
print(vade % 5)
print(vade % ekVade)
print(30 % 10)

# mantıksal operatörler
print(1 == 1)
print(1 == 2)

# CTRL K + CTRL C veya CTRL ö
# print(1 > 2)
# print(3 > 1)
# print(1 > 1)
# print(1 >= 1)

print(1 < 2)
print(3 < 1)
print(1 < 1)
print(1 <= 1)

print(1 != 1)
print(1 != 2)

# or and
 
# or => veya 
print(1 >2 or 5 > 2) 
print(1 > 2 and 5 > 2)
print(1 > 2 or 5 > 2 and 3 > 2)

print(1 > 2 and 5 > 2 and 3 > 2)

print(2 > 1 or 1 > 2 and 3 > 2)


# karar yapıları 

# if else
sayi1 = 15
sayi2 = 15
#sayi1 sayi2'den büyükse ekrana sayi 1 daha büyük yazdır
#condition 

#indent
if sayi1 <= sayi2:
    print("Sayi 1 Sayi 2' den büyüktür")
elif sayi1 == sayi2:
    print("İki sayı eşittir")
# eğer if ve elif bloklarında hiç birine girmez ise
else:
    print("Sati 1 Sayi 2'den büyüktür")

print("*******************************")    

if sayi1 <= sayi2:
    print("Sayi 1 Sayi 2' den büyüktür")
if sayi1 == sayi2:
    print("İki sayı eşittir")
else:
    print("Sati 1 Sayi 2'den büyüktür")

print("Burası if bloğunun dışıdır.") 
    