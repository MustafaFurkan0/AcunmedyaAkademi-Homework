class Vehicle():
    def __init__(self, model):
        self.model = model
    def start(self):
        print(f"{self.model} aracı başlatılıyor..")

class Car(Vehicle):
    def some_car_function(self):
        print("car function")
    def start(self):
        print("Araba başlatılıyor") #method overriding -> Polymporhism(araştır)

class Truck(Vehicle):
    def __init__(self, model,capacity):
        super().__init__(model)
        self.capacity = capacity
    
    def load_weight(self):
        print(f"Kamyonet {self.capacity} kg yükleniyor")
        
car1 = Car("Volvo")
car1.start()
car1.some_car_function()

print("**************************************")

truck1 = Truck("Scania", 500)
truck1.start()
truck1.load_weight()

# Polymporhism (Çok Biçimlilik)

class Hayvan:
    def ses_cikar(self):
        return "Bazı hayvanlar ses çıkarır."

class Kedi(Hayvan):
    def ses_cikar(self):  # Üst sınıftaki metodu eziyoruz
        return "Miyav!"

class Kopek(Hayvan):
    def ses_cikar(self):
        return "Hav hav!"

# Polymorphism kullanımı
hayvanlar = [Kedi(), Kopek(), Hayvan()]

for hayvan in hayvanlar:
    print(hayvan.ses_cikar())  # Aynı metod, farklı davranış gösteriyor
    
#OutPut
# Miyav!
# Hav hav!
# Bazı hayvanlar ses çıkarır.