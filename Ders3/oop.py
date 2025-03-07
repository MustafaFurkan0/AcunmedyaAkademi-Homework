#class
#attribute (özellikler)

class Car():
    model = "" #attribute
    
    # Constructor (Yapıcı Method)
    def __init__(self, model, year=2025): # -> ilgili obje üretildiği an çalıştırılır
        self.__model = model
        self.year = year
    
    def start(self): # self -> calsın kendisini ifade eder
        print(f"{self.__model} {self.year} arabası başlatılıyor..")
    
    def increase_speed(self, amount):
        print(f"Hız artırılıyor: {amount}")
        
    def set_model(self, model): # salt-yazılabilir
        if len(model)<2:
            print("Model ismi 2 haneden az olamaz")
            return
        self.__model = model
    
    def get_model(self):   # salt-okunur
        return self.__model


car1 = Car("Toyota", 2010) # Instance(örnek)
car1.set_model("a")
car1.__model = "BMW" #KAPSÜLLEME (ENCAPSULATİON) #set
print(car1.model) # get
car1.start()
car1.increase_speed(50)

print("**************************************")


car2 = Car("Volvo")
car2.start()
car2.increase_speed(20)
