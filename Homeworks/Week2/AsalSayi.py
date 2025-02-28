def asalMı(number):
    if number < 2:
        return print(f"{number} bir asal sayı değildir!!")
    for i in range(2,number,1):
        if number % i == 0:
            return print(f"{number} bir asal sayı değildir!!")      
    return print(f"{number} bir asal sayıdır!!!")

primeNum = int (input("Bir sayı giriniz: "))
asalMı(primeNum)
