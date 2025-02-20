faiz = 1.59
vade = "36"
krediAdi = "İhtiyaç Kredisi"

print(type(faiz))
print(type(vade))
print(type(krediAdi))

print(int(vade)+12)
#print(int(krediAdi))
faiz = str (faiz)
print(type(faiz))

vade = 36 #int(input("Lütfen istediğiniz vade sayısını giriniz: "))
print(type(vade))
print(vade + 12)

# string interpolation
# Sectiğiniz vade sonucu ortaya çıkan vade :
print("Sectiğiniz vade sonucu ortaya çıkan vade :" + str(vade))
print("Sectiğiniz vade sonucu ortaya çıkan vade :{vadeSayisi}".format(vadeSayisi = vade))
print(f"Sectiğiniz vade sonucu ortaya çıkan vade : {vade}")

isim = "Halit" #input("İsminizi Giriniz")
metin = "Merhaba {name}".format(name=isim)
print(metin)

# f-string
metin = f"Hoşgeldiniz {1+1}"
print(metin)

# Listeler 

dizi = ["İhtiyaç Kredisi", 10, 5.2, True]
print(dizi)

krediler = ["İhtiyaç Kredisi","Taşıt Kredisi", "Konut Kredisi"]
print(type(krediler))

print(krediler[0])

print(len(krediler)) #length
#print(krediler[3]) => hata verir

krediler.append("Özel Kredi")
print(krediler)

krediler.append("X Kredisi")
print(krediler)

krediler.pop(0)
print(krediler)

krediler.append("Taşıt Kredisi")
print(krediler)

krediler.remove("Taşıt Kredisi")
print(krediler)

krediler.extend({"Y Kredisi","Z Kredisi"})
print(krediler)

#döngüler

# for

# i=0 i<10
x=10
for i in range(x):
    print("xx")
    print(i)
    
print("******************")

#i=5 i<10
for i in range(5,10):
    print(i)
    
print("******************")

#i=0 i<51 i++10
for i in range(0,51,10):
    print(i)

print("******************")

# for i in range(0.1,0.5):
#     print(i)

krediler= ["İhtiyaç Kredisi", "Taşıt Kredisi", "Konut Kredisi"]
for kredi in krediler:
    print(kredi)

print("******************")

for i in range(len(krediler)):
    print(krediler[i])
print("******************")

# while
i = 0
while i < 10:
    print("x")
    i += 1
print("y")

print("******************")

while True:
    print("X")    
    break

print("******************")

i < 0
while i < len(krediler):
    print(i)
    if krediler[i] == "Konut Kredisi":
        break
    print(krediler[i])
    i+=1

# fonksiyonlar

fiyat = 100
indirim = 20

#definition define
def calculate():
    print(100-20)

def calculateWithParams(a,b):
    print(a-b)

def sayHello(name):
    print(f"Merhaba {name}")

calculate()
calculateWithParams(50,10)
calculateWithParams(100,30)
sayHello("Halit")
sayHello("Mustafa")
sayHello("Emine")

def calculateAndReturn(price, discount):
    return price - discount

yeniFiyat = calculateAndReturn(200,50)
print(yeniFiyat + 10)

#void
def calculatePrice(price, discount):
    print(price - discount)

def calculatePriceAndReturn(price, discount):
    return price - discount

print("*****************")
# fonk1 = calculatePrice(100,50)
# fonk2 = calculatePriceAndReturn(300,100)
# print(f"161. satır: {fonk1+100}")
# print(f"162. satır: {fonk2+100}")
print("*****************")




# döngüler

